from align_devops import fetch_jobs

def lambda_handler(event, context):
    jobs = fetch_jobs()
    if jobs:
        return {"jobs": jobs}
    else:
        return {"message": "No suitable vacancies found."}