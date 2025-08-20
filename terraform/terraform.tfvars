region               = "us-west-2"
lambda_function_name = "align-jobs-scraper"
schedule_expression  = "cron(0 9 ? * 2 *)" # Every Tuesday 09:00 UTC
