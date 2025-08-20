# Jobs-Mini-Sentinel 🚀

This project is a **Python-based scraper** that checks new job postings from [Align Technology Careers](https://jobs.aligntech.com/) and filters them by country and keyword.

It can run in three ways:
1. **Manually** on your local machine (via virtual environment).
2. **Automatically** as an **AWS Lambda** deployed with **Terraform**.
3. On a schedule via **GitHub Actions + AWS free tier** Lambda (weekly).

Additionally, this project can be extended to **send results as Telegram messages** (message sender solution).

---

## 📦 Features
- Search for jobs by keyword (default: `DevOps`).
- Exclude jobs by country (default: `India`).
- Can be triggered weekly using AWS EventBridge.
- Deployable with Terraform + GitHub Actions.
- Credentials handled securely via GitHub Secrets.
- Can be extended to push notifications to **Telegram**.

---

## ⚙️ Prerequisites
- AWS account (free tier is enough).
- S3 bucket for Terraform state (or reuse an existing one).
- GitHub repository with **Secrets**:
  - `aws iam create-user --user-name jobs-mini-sentinel`
  - Get the to add them to GitHub Secrets `AWS_ACCESS_KEY_ID`
  - Get the to add them to GitHub Secrets `AWS_SECRET_ACCESS_KEY`

  - `aws s3api create-bucket \
  --bucket jobs-mini-sentinel \
  --region us-west-2 \
  --create-bucket-configuration LocationConstraint=us-west-2`

---

## 🏗️ Terraform Infrastructure

The `terraform/` folder contains:
- **IAM Module** → Lambda execution role.
- **Lambda Module** → Deploys the Python function.
- **EventBridge Module** → Weekly schedule trigger.
- **Backend** → Uses S3 for storing Terraform state.

Terraform is responsible for deploying all AWS resources.

---

## 🔄 Deployment Flow with GitHub Actions

1. Push code to `main` branch.
2. GitHub Actions workflow:
   - Installs Python dependencies.
   - Packages code into a `.zip`.
   - Runs Terraform (`terraform apply`).
3. Terraform deploys Lambda, IAM role, and EventBridge rule.
4. AWS Lambda runs weekly on schedule.
5. Scraper fetches jobs and (optionally) sends to **Telegram**.

---

## 🔑 GitHub Secrets

You must configure in **GitHub Repository → Settings → Secrets and variables → Actions**:

- `AWS_ACCESS_KEY_ID` → from your IAM user.
- `AWS_SECRET_ACCESS_KEY` → from your IAM user.

These are injected automatically into the GitHub Actions workflow to allow Terraform to deploy to AWS.

---

## 📅 Trigger Schedule

By default, EventBridge runs the Lambda **once per week**.  
Schedule expression can be adjusted in `terraform.tfvars`:

```hcl
schedule_expression = "cron(0 9 ? * 2 *)" # Every Tuesday 09:00 UTC
```

## 💻 Running Manually (Local)

You can also run the scraper locally without AWS. Example with a virtual environment:
```bash
cd ~/scripts
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4
python align-devops.py
```


## 📲 Optional: Sending Results to Telegram

This scraper can be extended to act as a message sender solution:

- Instead of printing results, use Python’s requests library to call the Telegram Bot API.
- You can send new job postings to a personal chat or group every week.

Example (inside lambda_handler):
```python
import requests

def send_to_telegram(message: str):
    token = "<your_bot_token>"
    chat_id = "<your_chat_id>"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message}
```