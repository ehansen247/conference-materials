# Cloud Intro

Before you start run `pip install -r requirements.txt`. Requires python 3

## Servers

* run `python servers.py`
* <b>Note:</b> Rememeber to uncomment out terminate section when you are done

## Containers

* run `python containers.py`
* go to aws console and search for ecs task definitions
* click run task
* select fargate,
* select vpc subnet and secuirty group from server section
* run task

## Serverless

* `cd serverless`
* `chalice deploy`
* <b>Note:</b> To delete run `chalice delete`