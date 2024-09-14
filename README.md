# aws-projects

## Adding a new project

1. Create a new Organisational Unit in the root AWS organisation with the project name.
2. Create an AWS account with the same name under the OU. Provide your email with an alias e.g. `+aws{project name}`. You might need to move the account into the OU after.
3. In AWS Identity Center go to the AWS Accounts tab, select the account and assign your SSO user with administration priveledges.
4. Run `aws configure sso --profile {project name}-admin`. The name can be same as the profile, for the start URL and region: when in SSO, click the access keys button for administrator access in the created account. The registration scope can be set as `sso:account:access`. Follow the browser link to authenticate. Set the default CLI region to `eu-west-2`, default output format to `json`. Before running commands, set your profile to the expected profile with `export AWS_PROFILE=`.

## Useful terraform commands

```sh
terraform init
terraform validate
terraform apply
terraform destory
```