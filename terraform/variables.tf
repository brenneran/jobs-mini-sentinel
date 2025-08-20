variable "region" {
  type    = string
  default = "us-east-1"
}

variable "lambda_function_name" {
  type    = string
  default = "align-jobs-scraper"
}

variable "schedule_expression" {
  type    = string
  default = "rate(7 days)"
}