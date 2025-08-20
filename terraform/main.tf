provider "aws" {
  region = var.region
}

module "iam" {
  source               = "./modules/iam"
  lambda_function_name = var.lambda_function_name
}

module "lambda" {
  source               = "./modules/lambda"
  lambda_function_name = var.lambda_function_name
  role_arn             = module.iam.lambda_role_arn
  region               = var.region
  bot_token            = var.bot_token
  chat_id              = var.chat_id
}

module "eventbridge" {
  source               = "./modules/eventbridge"
  lambda_function_name = var.lambda_function_name
  schedule_expression  = var.schedule_expression
  lambda_arn           = module.lambda.lambda_arn
}