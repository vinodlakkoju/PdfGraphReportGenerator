#!/bin/sh
echo "Deploying Reporting service to PROD environmrnt"
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 453481562914.dkr.ecr.us-west-1.amazonaws.com
docker build -t reports-service .
docker tag reports-service:latest 453481562914.dkr.ecr.us-west-1.amazonaws.com/reports-service:latest
docker push 453481562914.dkr.ecr.us-west-1.amazonaws.com/reports-service:latest
for taskarn in $(aws ecs list-tasks --cluster compaira-service --service reports-service --desired-status RUNNING --output text --query 'taskArns'); do aws ecs stop-task --cluster compaira-service --task $taskarn; done;
echo "PROD deployment completed"

