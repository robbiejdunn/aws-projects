# hello-world

Simple hello world lambda deployed through terraform.

## Usage

```sh
terraform init
terraform validate
terraform apply
aws lambda invoke --region=eu-west-2 --function-name=$(terraform output -raw function_name) response.json
terraform destroy
```
