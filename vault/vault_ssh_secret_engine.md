## Vault SSH Secret Engine
Leverage Vault to secure SSH access to machines

The Vault SSH secrets engine provides secure authentication and authorization for access to machines via the SSH protocol. The Vault SSH secrets engine helps manage access to machine infrastructure, providing several ways to issue SSH credentials. This track walks you through setting up Vault SSH access in two ways:
* [Signed SSH Certificates](https://developer.hashicorp.com/vault/docs/secrets/ssh/signed-ssh-certificates)
* [One-time SSH Passwords](https://developer.hashicorp.com/vault/docs/secrets/ssh/one-time-ssh-passwords)

## In this challenge we will enable Vault's SSH engine for signing keys. The signed SSH certificates option is the simplest and most powerful in terms of setup complexity and in terms of being platform agnostic. By leveraging Vault's CA capabilities and functionality built into OpenSSH, clients can SSH into target hosts using their own local SSH keys.

#### Enable the SSH Engine
First we need to enable the SSH secrets engine within Vault. Vault is already deployed and your token is configured as an environment variable.

Use this command to enable the SSH secrets engine:
```bash
vault secrets enable ssh
```

Once enabled you can configure Vault with a CA for signing client keys using the /config/ca endpoint
```bash
vault write ssh/config/ca generate_signing_key=true
```

Then we will create a named Vault role for signing client keys
```bash
vault write ssh/roles/my-role -<<"EOH"
{
  "algorithm_signer": "rsa-sha2-256",
  "allow_user_certificates": true,
  "allowed_users": "*",
  "allowed_extensions": "permit-pty,permit-port-forwarding",
  "default_extensions": [
    {
      "permit-pty": ""
    }
  ],
  "key_type": "ca",
  "default_user": "ubuntu",
  "ttl": "30m0s"
}
EOH
```

You can see we're defining a few parameters within the role. You can see a full list of available parameters and their descriptions here [SSH secrets engine (API) ](https://developer.hashicorp.com/vault/api-docs/secret/ssh#parameters-2)

## In this challenge we will use the SSH secrets engine we set up in the previous step to sign a user's public key and use that signed public key to SSH into a target machine.

#### Sign Key with SSH Engine and SSH to Target
First, navigate to the "Target Instance" terminal. This is the machine we will be using Vault to SSH into.

Once there, use the following command to save Vault's public key as trusted-user-ca-keys.pem
```bash
curl -o /etc/ssh/trusted-user-ca-keys.pem http://base:8200/v1/ssh/public_key
```

As you can see, Vault does not require a token to interact with this endpoint. These steps are often automated using configuration management tools.

Next we will add the path where the public key contents are stored to the SSH configuration file as the TrustedUserCAKeys option.
```bash
echo "TrustedUserCAKeys /etc/ssh/trusted-user-ca-keys.pem" >> /etc/ssh/sshd_config
```

Lastly on this terminal, lets restart the SSH service so it can pick up the change
```bash
sudo systemctl restart sshd
```

#### Generate a SSH keypair
```bash
ssh-keygen -t rsa -f vault -N "" -C "user@example.com"
```


Now let's use Vault to sign the public key we just made and save it as signed-cert.pub
```bash
vault write -field=signed_key ssh/sign/my-role \
    public_key=@vault.pub > signed-cert.pub
```

Then change the permissions for signed-cert.pub we just created
```bash
chmod 400 signed-cert.pub
```

And, lastly SSH into the host machine using the signed key
```bash
ssh -o StrictHostKeyChecking=no -i signed-cert.pub -i vault ubuntu@target-instance
```
Great! You now successfully used Vault to get a local SSH key signed that allowed you to SSH into a target machine. Let now set up and test a one-time password SSH workflow.


## In this challenge we will create a role for using the one-time password SSH method. The One-Time SSH Password (OTP) SSH secrets engine type allows a Vault server to issue a One-Time Password every time a client wants to SSH into a remote host using a helper command on the remote host to perform verification.

#### Add a One Time Password Role
In order to leverage Vault's One-Time Password SSH functionality we will need to create a SSH role with a key_type of otp. Since we already enabled the SSH engine on the default path, we can create this role on the existing path.

Use this command to create a role named otp_key_role with key_type set to otp
```bash
vault write ssh/roles/otp_key_role key_type=otp \
  default_user=ubuntu \
  cidr_list=0.0.0.0/0
```
You can also do things like setting TTLs for the OTPs, restrict the allowed users, add a list of allowed domains and more. You can see the full list of available parameters here -
https://www.vaultproject.io/api/secret/ssh#parameters-2

That's it! Now we need to install the Vault-SSH-Helper on any target machines and you're ready to use Vault's OTP for SSH access.

## In this challenge we will install vault-ssh-helper on the remote host and SSH into the remote host using a one-time password generated by Vault.
#### Install vault-ssh-helper and SSH to Target
First, navigate to the "Target Instance" terminal. There you will download the Vault-SSH-Helper which will make a call back to Vault to verify the OTPs being used and mark them as being used in Vault so they are no longer valid.

Use this command in the "Target Instance" terminal to download and unzip the vault-ssh-helper
```bash
wget https://releases.hashicorp.com/vault-ssh-helper/0.2.0/vault-ssh-helper_0.2.0_linux_amd64.zip && sudo unzip -q vault-ssh-helper_0.2.0_linux_amd64.zip -d /usr/local/bin
sudo chmod 0755 /usr/local/bin/vault-ssh-helper
sudo chown root:root /usr/local/bin/vault-ssh-helper
sudo mkdir /etc/vault-ssh-helper.d/
sudo tee /etc/vault-ssh-helper.d/config.hcl <<EOF
vault_addr = "http://base:8200"
tls_skip_verify = true
ssh_mount_point = "ssh"
allowed_roles = "*"
EOF
```

You can see all of the configuration options for the vault-ssh-helper here - [vault-ssh-helper](https://github.com/hashicorp/vault-ssh-helper)

Then disable common-auth.
```bash
sudo sed -i 's/@include common-auth/# @include common-auth/' /etc/pam.d/sshd
```

Add authentication verification through the vault-ssh-helper.
```bash
echo -e "\nauth requisite pam_exec.so quiet expose_authtok log=/var/log/vault-ssh.log /usr/local/bin/vault-ssh-helper -dev -config=/etc/vault-ssh-helper.d/config.hcl
auth optional pam_unix.so not_set_pass use_first_pass nodelay" | sudo tee -a /etc/pam.d/sshd
```

Enable ChallengeResponseAuthentication
```bash
sudo sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/' /etc/ssh/sshd_config
```

Restart the sshd
```bash
sudo systemctl restart sshd
```

On machine for target machine. With a single command you can create a new OTP and SSH into the remote host using sshpass.
```bash
vault ssh -role otp_key_role -mode otp -strict-host-key-checking=no ubuntu@target-instance
```
