variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2" # Ohio
}

variable "project_name" {
  type        = string
  description = "Project name"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "backend_bucket" {
  type = string
}

variable "dynamodb_table" {
  type = string
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}