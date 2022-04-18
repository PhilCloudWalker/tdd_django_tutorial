# Tutorial Task

# Goal
- 1-month tutorial to understand test driven development with Python and deployment via Azure DevOps
- you will be guided through the workshop. Nevertheless, it is not fully scripted on purpose. Sometimes you will encounter errors or that things behave differently than expected. use problems to read documentations, google stuff, try, fail and finally succeed. these will be the most important and rewarding moments ;) 

## Source:
- Obey the Testing Goat (OTTD): https://www.obeythetestinggoat.com/pages/book.html#toc

## Part 0: Getting Started
Get to now django and write the first test
- Task: Finish Django Tutorial
    - Link: https://tutorial.djangogirls.org/en/
    - Goals: First understanding of django, VSCode Setup, understanding of virtual envs
    - Subtasks: 
        - Install VSCode
        - Check which python do you have --> what is the command?
        - Setup Virtual Env using venv package https://docs.python.org/3/library/venv.html

- Task: Finish OTTD Chapter 1 and 2
    - Goals: Writing first unittest and get to know test driven development
    - Subtask
        - Setup Config for Visual Code to debug via "python manage.py test"

## Part 1: TDD with Django
Develop a django app using test driven development locally
- Task: Finish OTTD Chapter 3 till 8
- Goals: understand testing, familiarize with git, learn console commands, learn more about ORM, get to know rest concepts 
- Subtasks
    - TDD - > unittest vs functional test
        - unittest structure: Setup, Exercise, Assert
    - how to create backend --> understanding of ORM
    - Rest API:
        - when does a API follows the rest principles?
        - understand conventions like: no trailing slash --> “action” URLs which modify the database.
    - Git:
        - get familiar with git status, git commit, git diff

## Part 2: Deploy with Azure DevOps
### Part 2.1: Manual deployment on a VM
Deploy Django app on a Linux Machine with Microsoft Azure
- Task: Finish OTTD Chapter 9 using a Azure VM (ubuntu) 
- Goals: get to know Azure portal, setup and configure a linux vm, deploy django app manually, networking
- Subtasks
    - create a virtual machine and login in https://docs.microsoft.com/en-us/azure/virtual-machines/linux/mac-create-ssh-keys --> choose cheapest!!!
    - install python and replace alias https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3


### Part 2.2 Automated Deployment on VM
Deploy Django app via CICD Pipeline
- Task: Finish DevOps Tutorial
    - Task Phillip P. to find a short tutorial for pipeline (not self-created)
    - Goal: Implement a first pipeline on your own
- Task: Run django unittest in the pipeline automatically
    - Goal: understand pipeline concepts
    - Subtasks: 
        - Understand difference stages, task, steps, jobs: https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops
        - Implement stage: https://docs.microsoft.com/en-us/azure/devops/pipelines/process/stages?view=azure-devops&tabs=yaml

- Task: Deploy code on VM
    - Goal: understand difference between build and deployment stage
    - Sources
        - https://youtu.be/zBr7cl6ASMQ
        - https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/deploy-linux-vm?view=azure-devops&tabs=java

- Task: Create VM via Terraform and include in pipeline
    - Goals: get to know IaC, include in pipeline
    - Subtasks
        - handle terraform state correctly


### Part 2.3 Automated deployment on Azure Apps

- Task: use a azure service to replace sqlite by azure sql db or postgres
- Task: create a azure web app and deploy the django app
- Task: deploy django as web app via devops pipeline
- Task: compare differences between VM and Azure Apps

## Ideas for further parts: 
- Dependency management with poetry

