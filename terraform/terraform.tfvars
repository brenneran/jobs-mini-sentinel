region               = "us-west-2"
lambda_function_name = "jobs-mini-sentinel"
schedule_expression  = "cron(0 9 ? * 2 *)" # Every Tuesday 09:00 UTC
