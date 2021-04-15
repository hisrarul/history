import os
import logging
import sys
import argparse
from deployments import scale_deployments
from statefulsets import scale_statefulsets

# Set log level
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

parser = argparse.ArgumentParser(description='Scale the Alpha.')
parser.add_argument('--action', help='Enter action, options: up/down')
args = parser.parse_args()


if args.action == 'down':
    scale_d = scale_deployments()
    scale_d.deployment_scale_down()

    scale_sts = scale_statefulsets()
    scale_sts.statefulset_scale_down()

elif args.action == 'up':
    scale_d = scale_deployments()
    scale_d.deployment_scale_up()

    scale_sts = scale_statefulsets()
    scale_sts.statefulset_scale_up()

else:
    logging.info('Please provide the valid action: up or down')