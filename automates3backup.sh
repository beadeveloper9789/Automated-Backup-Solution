#!/bin/bash

# Define the source directory to be backed up
SOURCE_DIR="terraform-script/vpc.tf"

# Define the S3 bucket and path to store backups
S3_BUCKET="testbuk73"
S3_PATH="/backups"

# Upload the backup to S3
aws s3 cp "$SOURCE_DIR" "s3://$S3_BUCKET$S3_PATH/"
