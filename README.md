# Manage EventBridge One time schedules using StepFunctions

This project contains source code for a serverless application to create, and delete Amazon EventBridge one time schedules using Step Functions.

## Blog Post

You may read more about this here: https://medium.com/@pubudusj/manage-eventbridge-schedules-using-step-functions-16c47d1f8428 

## Deploy the application

Below are the deployment details.
You need AWS CLI, SAM CLI and GIT installed in your machine.

1. Clone the repository: https://github.com/pubudusj/manage-eb-schedules-with-stepfunctions
2. Go in to the directory `manage-eb-schedules-with-stepfunctions`
3. Install dependencies with `sam build`
4. Deploy the stack with `sam deploy -g`

## Testing

1. Once the stack is deployed successfully, you can start a Step Functions execution with below payload format:
    ```
    {
      "scheduleDate": "YYYY-MM-DD",
      "scheduleTime": "hh:mm:ss",
      "error": 0
    }
    ```
2. To test the scheduled task failure scenario, set the `error` value to `1`.

## Cleanup

1. To delete the stack, use: `sam delete`
