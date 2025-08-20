variable "region" {
  type    = string
  default = "us-west-2"
}

variable "lambda_function_name" {
  type    = string
  default = "jobs-mini-sentinel"
}

variable "schedule_expression" {
  type    = string
  default = "rate(7 days)"
}

variable "bot_token" {
  type = string
}

variable "chat_id" {
  type = string
}