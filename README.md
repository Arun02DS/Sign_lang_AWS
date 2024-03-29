## **Object Detection Yolov5 (AWS deploy)**

### How to run

1. conda create -n venv python=3.7 -y
2. conda activate venv
3. pip install -r requirements.txt
4. python app.py
5. open in browser: [http://localhost:8080](http://localhost:8080/)

### Project Architecture

![image](https://github.com/Arun02DS/Sign_lang_AWS/blob/a5c7fb082e2f2709c1cc598b85b936cc2f0a4673/docs/Project_flowchart.png)

### AWS Deployment with github actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

## 3. Download AWS CLI

```
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

3. AmazonS3FullAccess
```

## 3. Create ECR repo to store/save docker image

```
- Save the URI: 712567051749.dkr.ecr.us-east-1.amazonaws.com
```

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

```
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

# 6. Configure EC2 as self-hosted runner:

```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

# 7. Setup github secrets:

```
AWS_ACCESS_KEY_ID:{AWS_ACCESS_KEY_ID}

AWS_SECRET_ACCESS_KEY:{AWS_SECRET_ACCESS_KEY}

AWS_REGION = {AWS_REGION}

AWS_ECR_LOGIN_URI = {AWS_ECR_LOGIN_URI}

ECR_REPOSITORY_NAME = {ECR_REPOSITORY_NAME}

```

### 8. EC2 link:

```
http://3.86.145.99:8080/
```
