# aws-projects

System design solutions to ML problems from Kaggle:
- hello-world - simple hello world example to become familiar with terraform. Provisions a python lambda function & API gateway.
- mushroom-classification - classification of mushrooms based on some given features (https://www.kaggle.com/datasets/uciml/mushroom-classification).

## Requirements

- AWS account.
- Authenticated in AWS CLI.
- Terraform installed.

## Adding a new project

1. Create a new Organisational Unit in the root AWS organisation with the project name.
2. Create an AWS account with the same name under the OU. Provide your email with an alias e.g. `+aws{project name}`. You might need to move the account into the OU after.
3. In AWS Identity Center go to the AWS Accounts tab, select the account and assign your SSO user with administration priveledges.
4. Run `aws configure sso --profile {project name}-admin`. The name can be same as the profile, for the start URL and region: when in SSO, click the access keys button for administrator access in the created account. The registration scope can be set as `sso:account:access`. Follow the browser link to authenticate. Set the default CLI region to `eu-west-2`, default output format to `json`. Before running commands, set your profile to the expected profile with `export AWS_PROFILE=`.

## Removing a project

1. Switch to the project profile with `export AWS_PROFILE=`. Run `terraform destroy` to destroy any existing infrastructure.
2. From AWS organisations, close the associated account for the project. After closing the account will become unrecoverable after 90 days. Append `-deleteme` to the OU, it seems the account can not be removed from the organisation or the OU deleted until the 90 days has passed, it should be done at this time.

## Useful terraform commands

```sh
terraform init
terraform validate
terraform apply
terraform destory
```
