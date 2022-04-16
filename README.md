# Tutorial Task

## Source:
- Obey the Testing Goat (OTTD): https://www.obeythetestinggoat.com/pages/book.html#toc

## Part 0: Getting Started
- Create Virtual env based on docu
- Setup inital Django
- OTTD: Chapter 1 and 2
- Write tests
- Setup Config for Visual Code to debug --> had to change to folder with main, otherwise did not work :(

## Part 1: TDD with Django
- OTTD: Chapter 3 till 8
- learning concepts: 
    - TDD - > unittest vs functional test
        - unittest structure: Setup, Exercise, Assert
    - how to create backend --> understanding of ORM
        - deeper understanding
    - Rest API:
        - what are the concepts, via is it not fully restish
        - understand conventions like: no trailing slash --> “action” URLs which modify the database.
    - Git:
        - get familiar with git status, git commit, git diff

## Part 2: Deploy with Azure DevOps
### Part 2.1: Manual deployment on a VM
- OTTD Chapter 9 - using a Azure VM (ubuntu) --> choose cheapest!!!
    - create a virtual machine and login in https://docs.microsoft.com/en-us/azure/virtual-machines/linux/mac-create-ssh-keys
    - include public dns. optional create add own dns https://docs.microsoft.com/en-gb/azure/virtual-machines/custom-domain
    - install python and replace alias https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3
- Learning Concepts:
    - Azure VM: setup, networking
    - linux commands

### Part 2.2 Automated Deployment on VM
- First task: Create pipeline for unittest
    - Connect git and azure devops
    - Use standard django template
    - Modify a bit
    - Create a stage "unittest"
        - Understand difference stages, task, steps, jobs: https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops
        - Implement stage: https://docs.microsoft.com/en-us/azure/devops/pipelines/process/stages?view=azure-devops&tabs=yaml
    - Deploy code on VM
        - https://youtu.be/zBr7cl6ASMQ
        - https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/deploy-linux-vm?view=azure-devops&tabs=java
            - erstmal mit git clone
            - dann mit copy und upload
    - create VM with terraform
        - Question: where to store terraform state

### Part 2.3 Automated deployment on Azure App
    - Adjust database

- Understand pipeline
- Understand git concepts: feature branch, PR
- Understand how to database tests


## Ideas for further parts: 
- Dependency management with poetry

