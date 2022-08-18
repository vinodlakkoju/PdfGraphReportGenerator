#!/bin/sh
echo "Deploying to DEV environmrnt"
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 453481562914.dkr.ecr.us-west-1.amazonaws.com
docker build -t reports-service-dev .
docker tag reports-service-dev:latest 453481562914.dkr.ecr.us-west-1.amazonaws.com/reports-service-dev:latest
docker push 453481562914.dkr.ecr.us-west-1.amazonaws.com/reports-service-dev:latest
for taskarn in $(aws ecs list-tasks --cluster compaira-service-dev --service reports-service-dev --desired-status RUNNING --output text --query 'taskArns'); do aws ecs stop-task --cluster compaira-service-dev --task $taskarn; done;
echo "DEV deployment completed"
