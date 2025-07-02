# Serverless File Upload Pipeline

This project demonstrates a fully serverless file upload and metadata processing pipeline using AWS services: S3, Lambda, and DynamoDB.

## 🛠️ Services Used
- AWS S3: File storage
- AWS Lambda (Python): Metadata extraction and processing
- AWS DynamoDB: Metadata storage
- AWS CloudWatch: Logging

## 📌 Architecture
![Serverless-Architecture](https://github.com/user-attachments/assets/ff045f7f-e69e-4d87-b43a-3e43a774fa56)


1. User uploads file to S3
2. S3 triggers Lambda on upload (PUT)
3. Lambda extracts metadata (file name, size, content type)
4. Metadata is stored in DynamoDB

## ✅ Features

- Real-time processing of uploaded files
- Automatic metadata extraction
- Serverless, scalable design
