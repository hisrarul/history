## Vault Agent Templating and PKI Workflow (HVD)
Consumer track for Vault Agent templates and PKI certificates

This track leads individuals who own applications through the process of using pre-configured Vault Agent templates and PKI secrets engines.

* Vault Agent's templating functionality allows secrets to be rendered to files or environment variables.
* Vault Agent templating can automatically renew and fetch secrets from Vault.
* The KV secrets engine is a generic Key-Value store used to store arbitrary secrets, with version 2 being able to retain a configurable number of secret versions.

#### Introduction
Vault Agent provides a seamless method for integrating secrets management into any new or legacy applications you may be responsible for. For legacy applications, Vault Agent eliminates the need for application upgrades or modifications, as the agent is capable of authenticating with Vault, retrieving secrets, and injecting those secrets into the required location for the application. Agent templates bridge the gap between a secret's format in Vault and the input format expected by the application.

Templates may be generated for you by a system administrator, or you may be required to create your own. In this first challenge, you will explore how to use a pre-configured template to fetch static secrets from a KV-v2 secrets engine.

#### Review the preconfigured agent file
```json
pid_file = "./pidfile"

vault {
   address         = "https://127.0.0.1:8200/"
   tls_skip_verify = true
}

auto_auth {
   method {
      type = "token_file"
      config = {
         token_file_path = "./.vault-agent-token"
      }
   }
   sink {
      type = "file"
      config = {
         path = "./.vault-token-via-agent"
         mode = 0640
      }
   }
}

template_config {
    static_secret_render_interval = "5m"
}

template {
    source      = "/opt/vcdl/files/secret-template.ctmpl"
    destination = "/opt/vcdl/files/secrets.txt"
}
```

Open `agent-config.hcl` file. The top portion of the file provides the configuration options required for Vault Agent to authenticate with Vault, as well as the specification for how frequently to re-render secrets (static_secret_render_interval).

It is worth highlighting the template block for application owners. The template block has multiple configuration options but will almost always include a source and destination parameter (a source parameter is not necessary in very specific cases, and is discussed further in the [Agent documentation](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/template#template-configurations)).

The source parameter specifies the path on disk to be used as the input template. In this case, the input template is located at the path /opt/vcdl/files/secret-template.ctmpl. The destination parameter specifies the path on disk where the rendered secrets should be created. If the parent directories do not exist, Vault Agent will attempt to create them.

If you explore the file explorer of the current tab, you will notice the `secret-template.ctmpl` file. This file provides an example of a template that retrieves a generic secret from Vault's KV-v2 secrets engine:

`{{ with secret "secret/data/login_credentials" }}` designates the path in Vault where the secret is being retrieved from.
Username: `{{ .Data.data.username }}` and Password: `{{ .Data.data.password }}` describe the format in which the secrets will be rendered. username and password are the keys for the values that will be pulled from Vault.
{{ end }} marks the end of the template file.

#### Run Vault Agent
```bash
vault agent -config=agent-config.hcl
```

Vault Agent will have placed the formatted secrets into the `secrets.txt` file that was assigned as the destination value in the `agent-config.hcl` file.
You can either run cat secrets.txt to output the file contents in the Terminal tab, OR
Navigate back to the Code Editor tab and select the secrets.txt file in the file explorer.
`secrets.txt` should show the following results:
```bash
Username: dns_server
Password: ahBgrt54dreUhit
```

#### API call to Vault
```bash
curl --header "X-Vault-Token: $(cat /root/.vault-token)" https://127.0.0.1:8200/v1/secret/data/login_credentials | jq .
```

[Various configuration parameters](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/template#global-configurations) can be used to handle potential drift or secret misconfiguration, including but not limited to: exit_on_retry_failure, error_on_missing_key, and lease_renewal_threshold.

You should also be aware of the different behaviors Vault Agent exhibits when dealing with different types of secrets or tokens. You can [review these behaviors in the documentation](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/template#renewals-and-updating-secrets).

## Vault Agent will inject secrets referenced in the env_template configuration blocks as environment variables into the command specified in the exec block as part of process supervisor mode.
* Process supervisor mode requires at least one env_template block and exactly one top level exec block.

#### Introduction
In some cases, it may be up to the application developer to create their own Vault Agent templates for the secrets their application(s) require. This is where the [generate-config tool](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/generate-config) comes in.

generate-config is part of the Vault Agent's binary, and can help you create a basic configuration file. Currently, the tool can only be used to generate a config file with environment variable templates for running Vault Agent in [process supervisor mode](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/process-supervisor).

Environment variable templates are configured via the env_template block, which maps the template specified in the contents field to the environment variable named in the title of the block. In the example:

```bash
env_template "CREDENTIAL_PASSWORD" {
  contents             = "{{ with secret \"secret/data/credential\" }}{{ .Data.data.password }}{{ end }}"
  error_on_missing_key = true
}
```

`CREDENTIAL_PASSWORD` is the name of the environment variable that stores the value associated with the key password. If the secret secret/data/credential does not have a key password, then Vault Agent will exit with an error, as specified by `error_on_missing_key = true`.

#### Step 1: Configuration Customization
The `generate-config` tool has a few specific parameters associated with it, along with the [standard set of flags](https://developer.hashicorp.com/vault/docs/commands) included in all commands:

`type`: A required string that specifies the type of configuration file to generate; currently, only env-template is supported.
`path`: The path to a kv-v1 or kv-v2 secret.
`exec`: The command to execute in process supervisor mode; defaults to "env" if nothing is specified.

You can have multiple -path parameters in the generate-config tool. If a -path ends with /*, the tool will attempt to recurse through the secrets tree rooted at the given path, and generate env_template entries for each encountered secret.

1. Starting in the Terminal tab, run the agent command:
```bash
vault agent generate-config \
-type="env-template" \
-exec="./kv-dev.sh" \
-path="secret/connection_string" \
agent-config.hcl
```
agent-config.hcl is the name of the agent file that will result. If this were not specified, the default configuration file would be named agent.hcl.

2. Look for the output
3. Navigate to the agent-config.hcl
```json
auto_auth {

  method {
    type = "token_file"

    config {
      token_file_path = "/root/.vault-token"
    }
  }
}

template_config {
  static_secret_render_interval = "5m"
  exit_on_retry_failure         = true
}

vault {
  address = "https://127.0.0.1:8200/"
}

env_template "CONNECTION_STRING_DNS_CONNECTOR" {
  contents             = "{{ with secret \"secret/data/connection_string\" }}{{ .Data.data.dns_connector }}{{ end }}"
  error_on_missing_key = true
}

exec {
  command                   = ["./kv-dev.sh"]
  restart_on_secret_changes = "always"
  restart_stop_signal       = "SIGTERM"
}
```
The key parts of the `agent-config.hcl` file are the env_template block and the exec block: - The env_template defines the environment variable `CONNECTION_STRING_DNS_CONNECTOR`. - The exec block defines what child process to run once the environment variable(s) are present. In this case, once CONNECTION_STRING_DNS_CONNECTOR is retrieved from Vault, then the script kv-dev.sh will run.
kv-dev.sh
```bash
#!/bin/sh
echo
echo "=== KV DEV ==="
echo "Connection String = ${CONNECTION_STRING_DNS_CONNECTOR}"
echo
```

#### Rerun the vault agent
```bash
vault agent -config=agent-config.hcl
```

If you wanted Vault Agent to continue running in process supervisor mode, you would need to keep the child process running. This is because [Vault Agent will naturally mirror the child process](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/process-supervisor#functionality) specified in the exec block.

## An application appropriate for a development environment has been prepared for you prior to the start of the challenge.
* HTTPS is the secure version of HTTP and is the dominant protocol used to send information between a web browser and a website.

#### Introduction
The PKI secrets engine can generate dynamic X.509 certificates. With this secrets engine, applications can obtain certificates without undergoing a lengthy authentication and authorization process. A certificate authority is a trusted entity that stores, signs, and issues digital certificates for SSL/TLS communication. Vault can act as a root and/or intermediate certificate authority (CA) based on the needs of an organization.

When Vault is properly configured, application developers can issue leaf certificates from an intermediate CA for their application(s). They can then transition their application(s) over to the HTTPS communication protocol.

#### Step 1: Generate a leaf certificate
An intermediate CA has been configured at the path pki_int in Vault. You will now use this endpoint to generate a leaf certificate.

1. Use the Terminal tab to run the command:
```bash
vault write pki_int/issue/city-dev-app common_name="city.devapp.com" ttl="12h" > certificate-dev.txt
```
The command redirects the output to a file called certificate-dev.txt and should produce no other text.
certificate-dev.txt
```text
cat certificate-dev.txt 
Key                 Value
---                 -----
ca_chain            [-----BEGIN CERTIFICATE-----
MIIDoDCCAoigAwIBAgIUPvaBnJjlmWmTD8dMw7tx1Ao99UAwDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAxMHYXBwLmNvbTAeFw0yNDEwMDIwNjM4MzJaFw0yNDEwMDMw
NjM5MDJaMCkxJzAlBgNVBAMTHmFwcC5jb20gSW50ZXJtZWRpYXRlIEF1dGhvcml0
eTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMkZsSkElepYku3JMHv4
1M6Drvok4kKSFd0SaG2jvorpztFVpQ9PCZxrTJomyhO/kR5CKG2XedeQ9HtWllV/
fMby9zylxckEY8kvNTra1f2yxB9utGGq94+87jmmF8BZGEf12fh/24APwG1a1is6
ErDDisf5LnzA80YYh8m1U9kU+KmDF2BycwDxAv811wHm5tYTXcgQmCWO+/rCgx3a
9DEmxYbFVoFssrW9Z2Py9NFZBv95vkZRkf9DiI2PdmRcJQmU9Y0jK0Q7kTKLOqJa
x58TRpBc7iV1OpmlewX8M1ik2q2xBxrsVsiQ0MGVvrhNdAtjpkC58AbUJkMfZKhq
ATMCAwEAAaOB1jCB0zAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAd
BgNVHQ4EFgQUVCuhOQIeCpM2v0kW4x4oWgw09bEwHwYDVR0jBBgwFoAUAGZ9BbNk
9kYpwH8jL7nXcmq/RUcwPAYIKwYBBQUHAQEEMDAuMCwGCCsGAQUFBzAChiBodHRw
czovLzEyNy4wLjAuMTo4MjAwL3YxL3BraS9jYTAyBgNVHR8EKzApMCegJaAjhiFo
dHRwczovLzEyNy4wLjAuMTo4MjAwL3YxL3BraS9jcmwwDQYJKoZIhvcNAQELBQAD
ggEBAI6EgRKk+NSBSHIR2i9D5zHF3BzoeVgfy8UDQff3RcDpC9vmmprSe+QkyRrX
8/hfUpQVgpZweL1Ty1H56/j167ivLMVUpUXukTno/6qhqk1kZrtgTlgbLmRQbuoY
Qvcfk93hLwP7FgIo7rOzu95Yjl8aKN+NdDqVs4GWxKsWEDHj+ynrRBai3dE4iQiS
eykq4kCcqEVu1ZvStnpJPCtjN/YRd/sPxwQZagYdkfsFNvRmKNpyQoRzEV4LpMRf
QrW5aELOdJnvAsfJKNonWB0PgRUNFPSrBHekCc1UtuSjYsgukTT6PNHp/2KUQS6n
QTiPWtU67SzlFYYzxSvt1+qRZus=
-----END CERTIFICATE----- -----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUE4B6UoR80jnWSbMkujDUVEYcI/4wDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAxMHYXBwLmNvbTAeFw0yNDEwMDIwNjM4MzFaFw0yNDEwMDUw
NjM5MDFaMBIxEDAOBgNVBAMTB2FwcC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQC1HEYzDrLF5O+5jQEpzUmp19MCT2R4FkGWDKXpkWg26hNG3HsW
dVQdTYMoZnoO0Yapb6fSEra04D6YnlqRTgGZ/t5FM93oOr21BmxBT6qbcEyO8JvK
gxk+JFq4V3UyPhS2Pkpmqmtr8luBAY2Mla0JIPuVI1GCfiliMJlWVA+1aetm0YEl
S/3o9X1P1JJ76IBjVDSUFpboWx+Bma2nwCL9kbVbgWVtgU7Sy+WNgWOmha9y7CAE
99o4e/frsYPCkox7z4KNz9WKVYViLMOsDCmO1I9AnuPB78Wr4G0YA0topjQAR7o1
wlDjqu9J6l2etAQFanq4Smwh08y6IYtUdxx1AgMBAAGjdzB1MA4GA1UdDwEB/wQE
AwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBQAZn0Fs2T2RinAfyMvuddy
ar9FRzAfBgNVHSMEGDAWgBQAZn0Fs2T2RinAfyMvuddyar9FRzASBgNVHREECzAJ
ggdhcHAuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQBMCkxyqxF/iCC7lSjO+UueaCjq
wJZ9Vbe5zRH7zIDX+nzzjvK5FkYddOgkFjjeCdrrL9WAs1S9AS7cq6VdfydgMQPZ
7puKSpp8rVsUdcFYOdR+Xjj76blY5gm5Sbe7wSBj62gEnKB3N8LcvqYdrmAeM7W0
nC4Yv2odZdhrOs3bs6BSI2wX5d50v6yv1zsm/zVHQHLEQMlLi0mdy1AP2fWVvHNQ
DoJJ1R9sOilHMP6mEeTTbiT2HU3FYXilBO0GYILFIKse1Tl052V06Ckr1OvWLXtF
oMp2ithoA+1pX9ku3l896VRliSZgmwyv7OUee9kTKNCrk5kyv1JJA9elG/IW
-----END CERTIFICATE-----]
certificate         -----BEGIN CERTIFICATE-----
MIID2jCCAsKgAwIBAgIUN4v4hS6W09/Jf4JmnePnZ8JuPCUwDQYJKoZIhvcNAQEL
BQAwKTEnMCUGA1UEAxMeYXBwLmNvbSBJbnRlcm1lZGlhdGUgQXV0aG9yaXR5MB4X
DTI0MTAwMjA2NDI0MFoXDTI0MTAwMjE4NDMwOVowGjEYMBYGA1UEAxMPY2l0eS5k
ZXZhcHAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAubawAkdZ
JN3KQZFf3d/AhnDSMMXZivUpBGxSDv/NxFw6m7MvKfysZpA6RgaNHPqV964THxQp
tkKEFEGumtF30ozlVxdsnC2ZKkKEytgj/RGsNIP16ee1CSy3YSS6tBRxB3xZ7sBw
KoyDVvdz8TqmrQm51IemMFSLwyyPdVMvnuSrS8hphKYIYL9hmXhA3al+P3Q3KsUu
67ZvSHTQS29747vbMV1LarHC+dqkNXPrCoeIpNEnLEo1U3CvaayGZZEfv6wkD/Fx
UNiIjRgdMIuQxIB7BAt0pPOAm8IYgqFh+WrVTUoDD7RJMrTJyCc+h7JB/qS+DbiJ
rYGaiTyzH1cjLQIDAQABo4IBBzCCAQMwDgYDVR0PAQH/BAQDAgOoMB0GA1UdJQQW
MBQGCCsGAQUFBwMBBggrBgEFBQcDAjAdBgNVHQ4EFgQUdEFJwCLlsFgGitxEMD80
uPqjccYwHwYDVR0jBBgwFoAUVCuhOQIeCpM2v0kW4x4oWgw09bEwPwYIKwYBBQUH
AQEEMzAxMC8GCCsGAQUFBzAChiNodHRwOi8vMTI3LjAuMC4xOjgyMDAvdjEvcGtp
X2ludC9jYTAaBgNVHREEEzARgg9jaXR5LmRldmFwcC5jb20wNQYDVR0fBC4wLDAq
oCigJoYkaHR0cDovLzEyNy4wLjAuMTo4MjAwL3YxL3BraV9pbnQvY3JsMA0GCSqG
SIb3DQEBCwUAA4IBAQCIOwPRnXIda+Dgy/s6WdqfJleErYMNRn3sNR6u8F487FYA
V+LTw7/lMWi6GIYnm3JadJJW2Q8gWW0oW/0ui7rYvmY3JHoShd6YzF0qTTKjpLSn
co/q8OOTA5oUSEmsTYwAEilrAaDuHIL4nS58aC7RXUxDZaWvdwdDI+wZPCtqEDCT
TJ3W7sYXhImrINJ42hvYw34cNdoJ9/rwj4hQHr1o4QD5X0dUgdpBv7Dc7ElQVA61
O49X1kmJTNd9Yw53V8MqY57ERHeQY98ietT8W2Eup4EKfXHRprXfPovSV+bdzjMD
YKbLhbIVegHn5xdkbkS6q+t/MUJsPim7qnqXZQ0d
-----END CERTIFICATE-----
expiration          1727894589
issuing_ca          -----BEGIN CERTIFICATE-----
MIIDoDCCAoigAwIBAgIUPvaBnJjlmWmTD8dMw7tx1Ao99UAwDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAxMHYXBwLmNvbTAeFw0yNDEwMDIwNjM4MzJaFw0yNDEwMDMw
NjM5MDJaMCkxJzAlBgNVBAMTHmFwcC5jb20gSW50ZXJtZWRpYXRlIEF1dGhvcml0
eTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMkZsSkElepYku3JMHv4
1M6Drvok4kKSFd0SaG2jvorpztFVpQ9PCZxrTJomyhO/kR5CKG2XedeQ9HtWllV/
fMby9zylxckEY8kvNTra1f2yxB9utGGq94+87jmmF8BZGEf12fh/24APwG1a1is6
ErDDisf5LnzA80YYh8m1U9kU+KmDF2BycwDxAv811wHm5tYTXcgQmCWO+/rCgx3a
9DEmxYbFVoFssrW9Z2Py9NFZBv95vkZRkf9DiI2PdmRcJQmU9Y0jK0Q7kTKLOqJa
x58TRpBc7iV1OpmlewX8M1ik2q2xBxrsVsiQ0MGVvrhNdAtjpkC58AbUJkMfZKhq
ATMCAwEAAaOB1jCB0zAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAd
BgNVHQ4EFgQUVCuhOQIeCpM2v0kW4x4oWgw09bEwHwYDVR0jBBgwFoAUAGZ9BbNk
9kYpwH8jL7nXcmq/RUcwPAYIKwYBBQUHAQEEMDAuMCwGCCsGAQUFBzAChiBodHRw
czovLzEyNy4wLjAuMTo4MjAwL3YxL3BraS9jYTAyBgNVHR8EKzApMCegJaAjhiFo
dHRwczovLzEyNy4wLjAuMTo4MjAwL3YxL3BraS9jcmwwDQYJKoZIhvcNAQELBQAD
ggEBAI6EgRKk+NSBSHIR2i9D5zHF3BzoeVgfy8UDQff3RcDpC9vmmprSe+QkyRrX
8/hfUpQVgpZweL1Ty1H56/j167ivLMVUpUXukTno/6qhqk1kZrtgTlgbLmRQbuoY
Qvcfk93hLwP7FgIo7rOzu95Yjl8aKN+NdDqVs4GWxKsWEDHj+ynrRBai3dE4iQiS
eykq4kCcqEVu1ZvStnpJPCtjN/YRd/sPxwQZagYdkfsFNvRmKNpyQoRzEV4LpMRf
QrW5aELOdJnvAsfJKNonWB0PgRUNFPSrBHekCc1UtuSjYsgukTT6PNHp/2KUQS6n
QTiPWtU67SzlFYYzxSvt1+qRZus=
-----END CERTIFICATE-----
private_key         -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAubawAkdZJN3KQZFf3d/AhnDSMMXZivUpBGxSDv/NxFw6m7Mv
KfysZpA6RgaNHPqV964THxQptkKEFEGumtF30ozlVxdsnC2ZKkKEytgj/RGsNIP1
6ee1CSy3YSS6tBRxB3xZ7sBwKoyDVvdz8TqmrQm51IemMFSLwyyPdVMvnuSrS8hp
hKYIYL9hmXhA3al+P3Q3KsUu67ZvSHTQS29747vbMV1LarHC+dqkNXPrCoeIpNEn
LEo1U3CvaayGZZEfv6wkD/FxUNiIjRgdMIuQxIB7BAt0pPOAm8IYgqFh+WrVTUoD
D7RJMrTJyCc+h7JB/qS+DbiJrYGaiTyzH1cjLQIDAQABAoIBAHY9aGarAojEZUfF
xSHAmhV+s3S2I0GjwY+9X6mJGHtStUX4majD5QgP/+ohtaqjqOPfAvGgpsYSJ4G2
J/MONpnpdwMyOMZfCcusOlvjrVYs8FUnR2S7T7odrEu/VNfew/AeLiwifce5Ws3+
EuWdkA1Pye8Uxqyyx6FmN5hddE5W9xi9i8FfgCT/ZIY4p3lfpYVMEUIM9NbnOo0r
vAQ4OJdxKKqo0Zh7oZg36FLKso1m97lWDA9G2CDmUAfx6K7tdrlnc6qTCrmu3dd2
JHX4iPuzwtSutPqqMQQWQOCEsI2xkv9GuPd9H7ruvLUntozvUGWyPlzWr2iCM5Cn
+mDRp0kCgYEA4liLk/R65Jkmj6WNSHUxpFDycRNPhVknX3a0xY7Uwn4Mmk/oOIs+
Cnt9lt9mUU+ug8ET68HHS1o9wAcFtfFD8dIkvJx9qbFrFeJwk1GSyM9SQh6dMBXR
yOoHXC+UgZ75h91VNEaf251e4XmwlVuJ/hoL1EtImBFaw23++PXlqNMCgYEA0gte
rF2IWYJelk7iYgIQUcKFBab5cUBrZQxHYOm1mpzOKYfvSV7clYkqI2s2qWYS19rb
UrjQ+5IpIA+a5U8e8jn2AQp/g8MmSCKMw8ZgJGPhdF5le/O+KzHskpZuL/ZNUjFt
acw4cmSeZEOW2SVyNiTOF92SwPZXrS9eGk8Qg/8CgYAg2gkoKEvN8gyOvNCMu7XA
y57kmpDoIdB9IpWKNvjaYcEihIaH7m3Kx7GqvDH1i0MhDFz/0thCL47W2C4UAjiC
WKXMWkpC3uVT/9GnECflzXF690aJPCF+r7jxwFYlmhVNiupa9AUvst+aijb+9pJI
ty8QWPzoVVx/EO/44ne60QKBgHl7OfZW4lVioXItjaFBsE6ZQnZSbFKj/3kh8OaM
RQx3RIWgqTS2OL4D5us1RxgSgTN20QK3Aad+kWqJm/ykFjHic/WGLNn4NFvkH6Xb
Rh/F5M95CRj3kDVLWpgtiO0UdwPisnVOOBdxOmqi7MwKbFQEVW5YKFiSIYN4seRl
dhfhAoGAEWdX1p/cT8Sqf4DwX6LVrRzxurgt+2cc/IaSVPkw4C28j09cBFo2g6WJ
L6/qGZQ0izX46dFyeIMNR2FvQTBu248DqY6yRW9jkg7E9AO39DoUfylMiNW4dOBY
VpoyyRjD5dSTYbEYRYmgBA03iplD2BtnVIEdspUtvg/K7A9ijlA=
-----END RSA PRIVATE KEY-----
private_key_type    rsa
serial_number       37:8b:f8:85:2e:96:d3:df:c9:7f:82:66:9d:e3:e7:67:c2:6e:3c:25
```

#### Step 2: Move the HTTP to HTTPS communication
You will use the contents of certificate-dev.txt to transition a pre-configured application to HTTPS communication. The steps you perform here will be automated in Challenge 4 and should also be automated in your real-world application(s). This manual procedure allows you to review the components of TLS certificates and understand what happens behind the scenes when enabling HTTPS communication.
1. Open `certificate-dev.txt`
2. Copy the entirety of the text from `-----BEGIN RSA PRIVATE KEY-----` to `-----END RSA PRIVATE KEY-----`
3. Open the folder dev_application in the file explorer on the left of the Code Editor and select the key.pem file.
4. Paste the RSA Key text into this file `key.pem`.
5. Move back to the certificate-dev.txt file.
6. Copy the entire value for the key ca_chain:
7. Paste the contents into the dev_application/cert.pem file.
8. Return to the certificate-dev.txt file and copy the value assigned to the certificate key:
9. Paste the contents into the dev_application/cert.pem file, below the existing content.

#### HTTPS communication testing
1. Start the app
```bash systemctl start dev-app ```

## An application appropriate for a development environment has been prepared for you prior to the start of the challenge.

#### Introduction
In Challenge 1, you saw Vault secrets written to a text file for use by a theoretical application. While some applications may operate using this pattern, others might have Vault secrets injected directly into memory. This can be accomplished using an exec block that is part of the template block. This exec block is distinct from the one used in Challenge 2, as it cannot be used in process supervisor mode.

#### Step 1: Secret Creation
Developers may find themselves needing to write secrets into Vault that will then be consumed by an application. For example, if your application relies upon a database, you may need to save the database connection string into Vault.

1. Select the Vault UI tab and use the USER_TOKEN to log into Vault:
2. Select the secret/ secrets engine under the section labeled Secrets engines.
3. Select the button Create secret + to the right of the screen.
4. For the Path for this secret, enter minneapolis.
5. For the first key, enter name. For the value, write Minneapolis.
6. Press the Add button.
7. For the second key, enter population. For the value, write 425096.
8. Press the Add button.
9. For the final key, enter funds. For the value, write 1.83B.
10. Press the Save button.

#### Automating PKI creation Injection
As mentioned in Challenge 3, the configuration and integration of PKI certificates should ideally be an automated process. Vault Agent makes this automation process seamless. You can use template files to easily fetch leaf certificates from a designated PKI secrets engine, and then inject those certificates into the portion of your application that handles HTTPS communication.

As mentioned in Challenge 3, the configuration and integration of PKI certificates should ideally be an automated process. Vault Agent makes this automation process seamless. You can use template files to easily fetch leaf certificates from a designated PKI secrets engine, and then inject those certificates into the portion of your application that handles HTTPS communication.

Opening the `Code Editor` tab, you should select the file `pki-cert.tpl`. This is a template file that will fetch a leaf certificate from the same intermediate certificate authority you used in Challenge 3.
Select the `agent-city-config.hcl` file next. Look for the template block with a nested exec block.
This template will use the `pki-cert.tpl` template as its source, and direct the result of the call to Vault to the file `pki-cert.pem`. In order for Vault Agent to utilize the `pki-cert.pem` file to inject a certificate into an application, you must update the exec block.
For the exec block, replace the comment # Configure this block with the lines:

-+- `copy-key.sh` -+-

```bash
#!/bin/bash

echo "Executing copy-key script"

# Declare files as variables
input_file="pki-cert.pem"
output_file="private-key.pem"
app_key_file="/opt/vcdl/files/int_application/key.pem"
app_cert_file="/opt/vcdl/files/int_application/cert.pem"

# Create key file
touch private-key.pem

# Move private key to a separate file
sed -n '/^-----BEGIN RSA PRIVATE KEY-----$/,/^-----END RSA PRIVATE KEY-----$/p' "$input_file" > "$output_file"
sed -i '/^-----BEGIN RSA PRIVATE KEY-----$/,/^-----END RSA PRIVATE KEY-----$/d' "$input_file"

# Remove blank spaces at top of cert file
sed -i '/./,$!d' "$input_file"

# Copy over files from the /opt/vcdl/files directory to the application directory
cp "$output_file" "$app_key_file"
cp "$input_file" "$app_cert_file"
```

copy-key.sh is a local file that describes how to separate the contents in pki-cert.pem and inject them appropriately into the designated application. When Vault Agent renders the template for the first time or retrieves a different output at any point, then copy-key.sh will run. If copy-key.sh fails to finish in under 30 seconds, then Vault Agent will timeout.


```bash
command = ["./copy-key.sh"]
timeout = "30s"
```

```bash
pid_file = "./pidfile"

vault {
   address         = "https://127.0.0.1:8200/"
   tls_skip_verify = true
}

auto_auth {
   method {
      type = "token_file"
      config = {
         token_file_path = "./.vault-agent-token"
      }
   }
   sink {
      type = "file"
      config = {
         path = "./.vault-token-via-agent"
         mode = 0640
      }
   }
}

template_config {
  static_secret_render_interval = "5m"
}

template {
  source      = "/opt/vcdl/files/pki-cert.tpl"
  destination = "/opt/vcdl/files/pki-cert.pem"
  exec {
   command = ["./copy-key.sh"]
   timeout = "30s"
  }
}

template {
  source      = "/opt/vcdl/files/city.json.ctmpl"
  destination = "/opt/vcdl/files/int_application/main.html"
}
```

#### Secret Injection
In Challenge 1, you saw how secrets can be written to a text file. In the second template block of the agent-city-config.hcl file, you are now rendering secrets specified in the city.json.ctmpl file directly into the application's HTML. A similar format can be followed for your own application, with the appropriate template and destination configured.

You can review the city.json.ctmpl file if you are curious about the configuration, or move on to Step 4.

`city.json.ctmpl`

```html
<head>
    <style>
        table {
            border-collapse: collapse;
            border: 2px solid rgb(140 140 140);
            font-family: sans-serif;
            font-size: 0.8rem;
            letter-spacing: 1px;
        }

        th {
        border: 1px solid rgb(160 160 160);
        padding: 8px 10px;
        }    
    </style>
</head>

<body>
    <table>
        <tr>
            <th>City Name</th>
            <th>City Population</th>
            <th>City Funds</th>
        </tr>
        <tr>
        {{ with secret "secret/data/minneapolis" }}
            <th> "{{ .Data.data.name }}" </th>
            <th> "{{ .Data.data.population }}" </th>
            <th> "{{ .Data.data.funds }}" </th>
        {{ end }} 
        </tr>
    </table>
</body>
```

#### Start the vault agent
```bash
vault agent -config=agent-city-config.hcl
```

#### Launch the application
You need to create your application to visualize completely.

```bash
systemctl start int-app
```
