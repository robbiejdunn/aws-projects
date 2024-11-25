# Output value definitions

output "s3_bucket_name" {
  description = "Name of the S3 bucket used to store the CSV data."

  value = aws_s3_bucket.mushroom_classification_bucket.id
}
