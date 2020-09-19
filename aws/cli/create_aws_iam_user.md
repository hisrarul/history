## Create IAM user with console access

#### 1. create an iam user
```
aws iam create-user --user-name yourusername
```

#### 2. generate skeleton for login profile
```
aws iam create-login-profile --generate-cli-skeleton > create-login-profile.json
```

#### 3. update the username and password in create-login-profile.json

#### 4. create an iam profile 
```aws iam create-login-profile --cli-input-json file://create-login-profile.json```

#### 5. attach policy to an iam user
```
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --user-name yourusername
```
