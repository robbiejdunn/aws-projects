# mushroom-classification

ML system design for the Kaggle dataset https://www.kaggle.com/datasets/uciml/mushroom-classification.

## Setup

Have currently manually created a sagemaker notebook, & associated IAM role.

## Useful commands

To view the contents of the created S3 bucket:

```sh
aws s3 ls $(terraform output -raw s3_bucket_name)
```

## Teardown

Ensure you are on the correct AWS CLI SSO profile and then run:

```sh
terraform destroy
```

Remember to stop notebooks after use to avoid costs.
