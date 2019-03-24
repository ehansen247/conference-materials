# TODO fargate example with flask container

from pcf.particle.aws.ecs.ecs_cluster import ECSCluster
from pcf.core.quasiparticle import Quasiparticle
from pcf.particle.aws.ecs.ecs_task_definition import ECSTaskDefinition
from pcf.particle.aws.ecs.ecs_task import ECSTask
from pcf.core.pcf import PCF

import logging
logging.basicConfig(level=logging.DEBUG)

for handler in logging.root.handlers:
    handler.addFilter(logging.Filter('pcf'))


# Example ECS Cluster config json
# ECS Cluster is a required parent for ECS Service
ecs_cluster_example_json = {
    "pcf_name": "pcf_ecs_cluster",  # Required
    "flavor": "ecs_cluster",  # Required
    "aws_resource": {
        "clusterName": "pcf_example"  # Required
    }
}
# Setup required parent ecs_cluster particle using a sample configuration
ecs_cluster = ECSCluster(ecs_cluster_example_json)

# Example ECS Task Definition config json
ecs_task_def_example_json = {
    "pcf_name": "task-def",
    "flavor": "ecs_task_definition",
    "aws_resource": {
        "family": "pcf-ecs-task-def-example",
        "containerDefinitions": [
            {
                "name": "pcf-ecs-task-def-example",
                "essential": True,
                "privileged": True,
                "launchType":"FARGATE",
                "image": "anovis10:flask",
                "portMappings": [
                    {
                        "hostPort": 5000,
                        "containerPort": 5000,
                        "protocol": "tcp"
                    }
                ],
            }
        ]
    }
}

ecs_task_example = {
    "flavor": "ecs_task",
    "pcf_name": "ecs_task",
    "parents":["ecs_task_definition:task-def","ecs_cluster:pcf_ecs_cluster"],
    "aws_resource":{
        "launchType":"FARGATE",
        # "taskDefinition":"arn:aws:ecs:us-east-1:196217159118:task-definition/pcf-ecs-task-def-example:1",
        "taskName":"test"
    }

}
#  Requires ecs_task_definition particle
ecs_task = ECSTaskDefinition(ecs_task_def_example_json)
ecs_task.set_desired_state("running")
ecs_task.apply(sync=False)
print(ecs_task)

# ecs_task = ECSTask(ecs_task_example)
# ecs_task.set_desired_state("running")
# ecs_task.apply()
# print(ecs_task)

# q = Quasiparticle({
#     "flavor":"quasiparticle",
#     "pcf_name":"q",
#     "particles":[
#         ecs_task_def_example_json,
#         ecs_task_example,
#         ecs_cluster_example_json
#     ]
# })
#
# q.set_desired_state("running")
# q.apply()

# example terminate
# ecs_task.set_desired_state(State.terminated)
# ecs_task.set_desired_state(State.terminated)
# ecs_task.set_desired_state(State.terminated)
# pcf.apply(sync=True, cascade=True)
# print(ecs_task.get_state())
