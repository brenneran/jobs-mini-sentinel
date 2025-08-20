resource "aws_lambda_function" "this" {
  function_name = var.lambda_function_name
  role          = var.role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.11"

  filename         = "${path.root}/../package.zip"
  source_code_hash = filebase64sha256("${path.root}/../package.zip")

  timeout     = 30
  memory_size = 256

  environment {
    variables = {
      SEARCH_TERM      = "DevOps"
      FILTER_COUNTRIES = "India,China"
      BOT_TOKEN        = var.bot_token
      CHAT_ID          = var.chat_id
    }
  }
}