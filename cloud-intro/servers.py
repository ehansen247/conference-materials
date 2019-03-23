import logging
import json
import os

from pcf.core.quasiparticle import Quasiparticle
from pcf.particle.aws.vpc.vpc_instance import VPCInstance
from pcf.particle.aws.vpc.subnet import Subnet
from pcf.particle.aws.vpc.security_group import SecurityGroup
from pcf.particle.aws.ec2.ec2_instance import EC2Instance
from pcf.particle.aws.iam.iam_role import IAMRole

logging.basicConfig(level=logging.DEBUG)

for handler in logging.root.handlers:
    handler.addFilter(logging.Filter('pcf'))

# set up core infrastructure
vpc_definition = {
    "flavor": "vpc_instance",
    "aws_resource": {
        "custom_config": {
            "vpc_name": "jit-vpc",
        },
        "CidrBlock":"10.0.0.0/16"
    }
}

subnet_definition = {
    "flavor": "subnet",
    "parents":["vpc_instance:ec2-example"],
    "aws_resource": {
        "custom_config": {
            "subnet_name": "jit-subnet",
        },
        "CidrBlock":"10.0.0.0/24"
    }
}

# allow for public access
security_group_definition = {
    "flavor": "security_group",
    "parents":["vpc_instance:ec2-example"],
    "aws_resource": {
        "custom_config":{
            "IpPermissions":[
                {
                    "FromPort": 80,
                    "IpProtocol": "tcp",
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                    "ToPort": 80,
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ]
        },
        "GroupName":"jit-sg",
        "Description":"jit-sg"
    }
}

dir_path = os.path.dirname(os.path.realpath(__file__))
ec2_definition = {
    "flavor": "ec2_instance",
    "parents":["security_group:ec2-example","subnet:ec2-example","vpc_instance:ec2-example"],
    "aws_resource": {
        "custom_config": {
            "instance_name": "jit-ec2",
            "userdata_template_file": dir_path + "/userdata.sh.j2",
            "userdata_bash": True,
        },
        "ImageId": "$lookup$ami$ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20180912",
        "InstanceType": "t2.nano",
        "MaxCount": 1,
        "MinCount": 1,
        "NetworkInterfaces": [
        {
            'DeviceIndex': 0,
            "SubnetId":"$inherit$subnet:ec2-example$SubnetId",
            "SecurityGroupIds": ["$inherit$security_group:ec2-example$GroupId"],
            'AssociatePublicIpAddress': True
        }],
    }
}

# example quasiparticle that contains all required infrastructure.
example_definition = {
    "pcf_name": "ec2-example",  # Required
    "flavor": "quasiparticle",  # Required
    "particles": [
        vpc_definition,
        security_group_definition,
        subnet_definition,
        ec2_definition
    ]
}

# create ec2 server and required infrastructure
quasiparticle = Quasiparticle(example_definition)

# start example
quasiparticle.set_desired_state("running")
quasiparticle.apply(sync=True)
print(quasiparticle.get_state())
ec2 = quasiparticle.get_particle("ec2_instance","ec2-example")
print(ec2.current_state_definition.get("PublicDnsName"))

# terminate example (uncomment below to terminate)
# quasiparticle.set_desired_state("terminated")
# quasiparticle.apply(sync=True)
# print(quasiparticle.get_state())
