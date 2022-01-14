from aws_cdk import core
from aws_cdk.core import DefaultStackSynthesizer
from .pipelines_webinar_stack import PipelinesWebinarStack


class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = PipelinesWebinarStack(
            self,
            "WebService",
            synthesizer=DefaultStackSynthesizer(
                # TODO: Customize DefaultStackSynthesizer to your liking:
                # See link for a full list of Parameters: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.core/DefaultStackSynthesizer.html
                # Here, we only customize the deploy_role_arn
                deploy_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/cicd-codepipeline-deploy-role"
                # qualifier="CUSTOMQAULIFIER123",
                # bucket_prefix="YOURCUSTOMPREFIX",
                # cloud_formation_execution_role="YOURCUSTOMCFNEXECUTIONROLE",
                # lookup_role_arn="YOURCUSTOMLOOKUPROLE",
            ),
        )

        self.url_output = service.url_output
