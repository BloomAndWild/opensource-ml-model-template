# opensource-ml-model-template

This is an example application to accompany the Code & Wild blog post [Building a Machine Learning Orchestration Platform: Part 1](https://www.bloomandwild.com).

This application is just a very dummy example that shows how to build a simple Python application with some pip dependencies, package it as a Docker image and push it
to an ECR repository in AWS so it can then be run via ECS Fargate.

An example GitHub repository that can be combined with this application can be found in our public GitHub profile, under the name [terraform-aws-ml-model](https://github.com/BloomAndWild/terraform-aws-ml-model).
That other repository is a Terraform module that will provision an opinionated set of AWS artefacts so the application can be packaged and run on AWS.
