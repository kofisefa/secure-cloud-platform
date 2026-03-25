# Secure Cloud Platform (Terraform + AWS + Python Automation)

## 📌 Overview

This project demonstrates a production-grade cloud platform built using Terraform (Infrastructure as Code) and Python-based automation tooling. It focuses on security, reliability, and operational excellence aligned with modern DevOps and SRE practices.

---

## 🏗️ Architecture

* AWS (us-east-2 / Ohio region)
* VPC with public and private subnets
* NAT Gateway for controlled outbound traffic
* EC2 (t3.medium) with IAM-based access (no SSH)
* SSM Session Manager for secure instance access
* Remote Terraform state (S3 + DynamoDB locking)

---

## 🔐 Security Features

* No inbound access (SSH disabled)
* IAM roles with least privilege
* Instance access via SSM (auditable, keyless)
* Encrypted Terraform state
* Segmented network architecture

---

## ⚙️ Infrastructure as Code (Terraform)

* Modular design:

  * VPC module
  * EC2 module
  * IAM module
* Environment-based structure (dev/staging/prod ready)
* Remote state management
* Parameterized configuration (no hardcoding)

---

## 🐍 Python Automation Layer

Located in `platform-tools/`

### Tools Implemented:

* **IAM Auditor**

  * Detects wildcard (`*`) permissions in IAM policies

* **EC2 Auditor**

  * Identifies running instances (foundation for cost optimization)

### Features:

* CLI interface (`click`)
* AWS integration via `boto3`
* Structured codebase (modular design)
* Unit testing with `pytest`

---

## 🧪 Testing

```bash
pytest
```

* Ensures reliability of automation tools
* Demonstrates test-driven engineering practices

---

## 🖥️ Secure Access (SSM)

No SSH or key pairs required:

```bash
aws ssm start-session --target <instance-id>
```

---

## 🚀 Skills Demonstrated

* Terraform (advanced, modular IaC)
* AWS networking (VPC, subnets, NAT)
* Cloud security (IAM, least privilege, no SSH)
* Python automation (boto3, CLI tooling)
* Testing (pytest)
* DevOps best practices

---

## 🔜 Upcoming Enhancements

* Observability (CloudWatch / Prometheus)
* Incident response automation (`incident_bot.py`)
* Cost optimization tooling
* CI/CD pipeline (GitHub Actions)
* EKS deployment

---

## 📂 Project Structure

```
terraform/
  modules/
  environments/

platform-tools/
  aws/
  utils/
  tests/
```
# 🔷 Phase 5 — Observability & Incident Response (Cloud-Native, Event-Driven)

## 🎯 Objective
Extend the secure cloud platform with production-grade observability, alerting, and automated incident response using AWS-native services and Python.

---

## 🧱 Architecture

CloudWatch Metrics + Logs → CloudWatch Alarm → SNS → Lambda (Incident Bot) → CloudWatch Logs

---

## ⚙️ Components Implemented

### 📊 Monitoring (CloudWatch)
- EC2 CPU utilization monitoring
- Custom metrics via CloudWatch Agent:
  - Memory utilization
  - Disk usage
- Log ingestion from:
  - `/var/log/messages`

---

### 🚨 Alerting (CloudWatch Alarms + SNS)
- High CPU alarm:
  - Threshold: 80%
  - Evaluation periods: 2
- SNS topic (`incident-alerts`) for alert distribution

---

### 🤖 Incident Automation (AWS Lambda)

**Function:** `incident-bot`

**Trigger:** SNS (CloudWatch Alarm notifications)

**Capabilities:**
- Parses alarm payload
- Extracts EC2 instance ID
- Queries EC2 API for instance state
- Generates structured incident report

Example output:

```
===== INCIDENT DETECTED =====
{
  "incident": "HighCPU",
  "instance": "i-xxxxxxxxxxxx",
  "state": "running"
}
============================
```

---

### 🔐 Security Design
- No SSH access (SSM-only architecture)
- IAM least privilege:
  - EC2 role with SSM + S3 read
  - Lambda role with:
    - CloudWatch read
    - EC2 read
    - Basic execution logging
- Encrypted state and segmented VPC

---

### 🧪 Failure Simulation

Simulated real-world incidents using SSM:

- CPU exhaustion:
  ```
  yes > /dev/null &
  ```
- Triggered CloudWatch alarm → SNS → Lambda pipeline

---

### 🔍 Observability Validation

Verified:
- Alarm state transitions (OK → ALARM → OK)
- SNS message delivery
- Lambda invocation
- CloudWatch log generation

---

## 🧠 Key Skills Demonstrated

- AWS Observability (CloudWatch Metrics, Logs, Alarms)
- Event-driven architecture (SNS → Lambda)
- Incident response automation
- Python (boto3) for cloud operations
- Secure access patterns (SSM, no SSH)
- Real-world failure simulation & validation

---

## 🚀 Outcome

Built a fully automated, serverless incident detection and response pipeline that:

- Detects infrastructure anomalies
- Triggers alerts in real-time
- Executes automated incident enrichment
- Produces structured logs for analysis

---

## 🔮 Future Enhancements

- Slack / email alert formatting
- Log ingestion + anomaly detection
- Severity classification (P1/P2/P3)
- Terraform automation for Lambda + SNS
- Dead-letter queues (SQS) for resilience

## 🧠 Author
Rexford SA

Built as a portfolio project to demonstrate senior-level Cloud / DevOps engineering capabilities.
