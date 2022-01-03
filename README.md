<<<<<<< HEAD
## My Project

TODO: Fill this README out!

Be sure to:

* Change the title in this README
* Edit your repository description on GitHub

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

=======
# Customizing CDK-Pipelines using "DefaultStackSynthesizer"
This CDK Application demonstrates how to deploy a CDK Application using the CdkPipeline (https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_pipelines.CdkPipeline.html) construct with custom deploy roles via a custom "DefaultStackSynthesizer".
CdkPipeline is NOT the default CodePipeline construct that you might already now from native cloudformation CodePipeline resources. CdkPipeline abstracts away a lot of the complexity when setting up CodePipelines. This makes setup very easy, but comes with the drawback of less control on how the pipeline is setup (e.g. what deployment roles are being used). If you want to regain some control on how the codepipeline is setup, this code will help you do that, by explicitly overwriting the "DefaultStackSynthesizer" and setting a custom codepipeline Pipeline.

The interesting parts are found in the following places in the code: 
- In `pipelines_webinar/webservice_stage.py`, we overwrite the "DefaultStackSynthesizer" by setting a custom deploy_role_arn.
- In `pipelines_webinar/pipeline_stack.py`, we overwrite the default pipeline that is created by CdkPipeline with our custom `pipeline_custom`.

Optionally, the demo can be adjusted to work for cross-account cdk deployments with minor changes.

## Prerequisites: 
For this demo to work, we assume the following:

1. Administrative access to one AWS account. This AWS account will serve as our target account for the CdkPipeline and all of its deployment.

2. Successful CDK bootstrap of target AWS account with new synthesis style, e.g via:
    ```
    export CDK_NEW_BOOTSTRAP=1 
    cdk bootstrap aws://ACCOUNT_ID/REGION
    ```

3. The source code of this folder lives in a repository in GitHub that you control.

4. You established an active GitHub CodestarConnection in your target AWS account for the repository mentioned in step 3 above. Copy and paste the CodestarConnection Arn for later use (e.g. arn:aws:codestar-connections:us-east-1:111111111111:connection/e0ee08d9-1111-1111-1111-111111111111)

## Deployment of the CDK application:

### Initial Deployment by Hand
For this demo, we assume that the initial pipeline deploy happens by hand as follows:

1. Adjust AWS account id, repository parameters and CodestarConnection Arn in the following files:
- `cdk-pipelines-demo/app.py` - set AWS account id & region
- `cdk-pipelines-demo/pipelines_webinar/pipeline_stack.py` - set repository parameters and CodestarConnection Arn
  OPTIONAL: enable cross-account deploment by setting the variables `APP_ACCOUNT_DEV` and `APP_ACCOUNT_PROD`.

2. Push the updated code to your repository.

3. Set virtual env locally
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Do CDK synth & deploy
Make sure that you have your local CLI configured to access your target AWS account. 
Run the following to synth and deploy your CDK application in the context of your target AWS account.
```
cdk synth
cdk -v deploy
```

5. Check deployment status
Now, jump into your target AWS account and watch the pipeline deployment process. 
Our CodePipeline will show up as `CdkPipeline-Custom-Demo`.
Once completed, you should see the following cloudformation stacks fully deployed:
- `PipelineStack`
- `Pre-Prod-WebService`
- `Prod-WebService`

6. You are done!
Feel free to adjust the demo to your needs


Credits: 
This demo is based on the aws-samples "AWS CDK Pipelines Demo Code" project provided here: 
https://github.com/aws-samples/cdk-pipelines-demo
>>>>>>> 3304182 (first commit)
