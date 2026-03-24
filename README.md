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

---

## 🧠 Author
Rexford SA

Built as a portfolio project to demonstrate senior-level Cloud / DevOps engineering capabilities.
