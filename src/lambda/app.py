import boto3
import json

client = boto3.client('stepfunctions')


def lambda_handler(event, context):
    result = do_whatever_business_logic(event)
    send_task_status(event, result)


def send_task_status(event, result):
    task_token = event['token']

    if result == 'success':
        client.send_task_success(
            taskToken=task_token,
            output=json.dumps({
                'status': "Success",
                'output': {},
            })
        )
    else:
        client.send_task_failure(
            taskToken=task_token,
            cause="Task Failed",
            error='Exception'
        )


def do_whatever_business_logic(event):
    return 'error' if ('error' in event and event['error'] == 1) else 'success'
