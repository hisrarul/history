## Create credentials

```groovy
import jenkins.model.Jenkins
import com.cloudbees.plugins.credentials.domains.Domain
import com.cloudbees.plugins.credentials.CredentialsScope
import com.datapipe.jenkins.vault.credentials.common.VaultUsernamePasswordCredentialImpl

def store = Jenkins.get().getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()
def domain = Domain.global()

def credentialMapping = [
    "avengers" : "spiderman"
]

credentialMapping.each { credId, passKey ->
    
    // First, remove existing credential with same ID (to avoid duplicates)
    def existing = store.getCredentials(domain).find { it.id == credId }
    if (existing) {
        store.removeCredentials(domain, existing)
        println "Removed existing credential: ${credId}"
    }

    // Create new Vault-backed Username/Password credential
    def vaultCred = new VaultUsernamePasswordCredentialImpl(
        CredentialsScope.GLOBAL, 
        credId, 
        "Vault-backed token for ${credId}"   // description
    )

    // Configure Vault-specific settings
    vaultCred.setNamespace("<your_namespace>")
    vaultCred.setPath("<kv_secrets/path_to_token>")
    vaultCred.setUsernameKey("<your_username>")
    vaultCred.setPasswordKey(passKey)
    vaultCred.setEngineVersion(1)   // Use 2 if you are on KV v2

    // Optional but recommended
    vaultCred.setPrefixPath("")     // usually empty

    store.addCredentials(domain, vaultCred)

    println "Successfully created: ${credId} (passwordKey = ${passKey})"
}

println "\nAll credentials processed."
```

## Retreive credentials
```groovy
import com.cloudbees.plugins.credentials.*
import com.datapipe.jenkins.vault.credentials.common.VaultStringCredentialImpl

def creds = CredentialsProvider.lookupCredentials(
    VaultStringCredentialImpl.class,
    Jenkins.instance,
    null,
    null
)

def myCred = creds.find { it.id == '<your_jenkins_creds_id>' }

if (myCred) {
    // This forces the plugin to connect to Vault and return the plaintext
    println "Secret Value: " + myCred.getSecret().getPlainText()
} else {
    println "Credential ID 'gitlab_svc_vault' not found."
}
```
