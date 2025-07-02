# Serverless File Upload Pipeline

This project demonstrates a fully serverless file upload and metadata processing pipeline using AWS services: S3, Lambda, and DynamoDB.

## 🛠️ Services Used
- AWS S3: File storage
- AWS Lambda (Python): Metadata extraction and processing
- AWS DynamoDB: Metadata storage
- AWS CloudWatch: Logging

## 📌 Architecture

1. User uploads file to S3
2. S3 triggers Lambda on upload (PUT)
3. Lambda extracts metadata (file name, size, content type)
4. Metadata is stored in DynamoDB

## ✅ Features

- Real-time processing of uploaded files
- Automatic metadata extraction
- Serverless, scalable design

## 📁 Folder Structure

serverless-file-upload-pipeline/
├── lambda/
│ └── handler.py
└── README.md


## 🔒 IAM Permissions
Ensure Lambda role has:
- `AmazonS3ReadOnlyAccess`
- `AmazonDynamoDBFullAccess`
- `AWSLambdaBasicExecutionRole`

## 📸 Screenshots
