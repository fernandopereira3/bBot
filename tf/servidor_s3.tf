terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.23.1"
    }
  }
}

provider "aws" {
  profile = "default"
  region = "us-west-2"
}

resource "aws_s3_bucket" "bbot-s3" {
  bucket = "bbot-s3"

  tags = {
    Name        = "bbot"
    Environment = "Dev"
  }
}