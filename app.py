#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import DefaultStackSynthesizer

from pipelines_webinar.pipeline_stack import PipelineStack

app = core.App()

# TODO: Check if Account IDs are correct & Region!
PIPELINE_ACCOUNT = 'ACCOUNTID**REPLACEME' # Toolchain Account ID
REGION = "us-east-1"  # Toolchain Deploy Region

PipelineStack(
    app,
    "PipelineStack",
    env={
        "account": PIPELINE_ACCOUNT,
        "region": REGION,
    },
)

app.synth()
