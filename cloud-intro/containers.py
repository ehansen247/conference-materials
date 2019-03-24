from pcf.particle.aws.ecs.ecs_task_definition import ECSTaskDefinition

import logging
logging.basicConfig(level=logging.DEBUG)

for handler in logging.root.handlers:
    handler.addFilter(logging.Filter('pcf'))


# Example ECS Task Definition config json
ecs_task_def_example_json = {
    "pcf_name": "task-def",
    "flavor": "ecs_task_definition",
    "aws_resource": {
        "family": "pcf-ecs-task-def-example",
        "memory":"512",
        "cpu":"256",
        "containerDefinitions": [
            {
                "name": "pcf-ecs-task-def-example",
                "essential": True,
                "image": "anovis10/flask",
                "portMappings": [
                    {
                        "hostPort": 5000,
                        "containerPort": 5000,
                        "protocol": "tcp"
                    }
                ],

            }
        ],
        "requiresCompatibilities": ["FARGATE"],
        "networkMode":"awsvpc"
    }
}

#  Create ecs_task_definition
ecs_task = ECSTaskDefinition(ecs_task_def_example_json)
ecs_task.set_desired_state("running")
ecs_task.apply(sync=False)
print(ecs_task.state)
