terraform {
  backend "s3" {
    bucket       = "jobs-mini-sentinel"
    key          = "align-jobs-lambda/terraform.tfstate"
    region       = "us-west-2"
    use_lockfile = true
    encrypt      = true
  }
}