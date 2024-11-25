provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = "dev"
      Project = "mushroom-classification"
    }
  }

}

resource "random_pet" "mushroom_classification_bucket_name" {
  prefix = "mushroom-classification-bucket"
  length = 4
}

resource "aws_s3_bucket" "mushroom_classification_bucket" {
  bucket = random_pet.mushroom_classification_bucket_name.id
}

resource "aws_s3_bucket_ownership_controls" "mushroom_classification_bucket" {
  bucket = aws_s3_bucket.mushroom_classification_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

/*
resource "aws_s3_bucket_acl" "mushroom_classification_bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.mushroom_classification_bucket]

  bucket = aws_s3_bucket.mushroom_classification_bucket.id
  acl    = "private"
}

resource "aws_sagemaker_notebook_instance" "eda_ni" {
  name          = "eda-notebook-instance"
  role_arn      = aws_iam_role.role.arn
  instance_type = "ml.t2.medium"

  tags = {
    Name = "foo"
  }
}
*/
