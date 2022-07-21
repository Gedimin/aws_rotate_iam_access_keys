#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import configparser
from subprocess import Popen, PIPE
import shlex
import json


def _get_sts_token_response():
    """Returns response of command getting aws sts token"""
    mfa_arn = '' # put here ARN of your MFA Devicce
    aws_profile = 'mfa' # put here your value of aws profile to get token
    mfa_code = str(input('Enter CODE from MFA device:'))
    command = f'aws sts get-session-token --serial-number {mfa_arn} --token-code {mfa_code} --profile {aws_profile}'
    args = shlex.split(command)
    try:
        process = Popen(args, stdout=PIPE)
        output, err = process.communicate()
        exit_code = process.wait()
        if err is not None or exit_code != 0:
            print(f'ERROR executing command: {command}')
        return output
    except FileNotFoundError as e:
        print(f'{e}\nCheck if awscli is installed')
        sys.exit(65)


def _parse_aws_response(sts_token_response):
    """Parses response of command getting aws sts token"""
    response_dict = dict()
    try:
        response_dict = json.loads(sts_token_response)
    except Exception as e:
        print(e)
    return response_dict

def _write_aws_credentials(aws_access_key_id, aws_secret_access_key, aws_session_token):
    """Writes AccessKeyId, SecretAccessKey, SessionToken to $HOME/.aws/credentials file to default profile"""
    aws_credentials_file = os.environ['HOME'] + '/.aws/credentials'
    config = configparser.ConfigParser()
    config.read(aws_credentials_file)
    config['default']['aws_access_key_id'] = aws_access_key_id
    config['default']['aws_secret_access_key'] = aws_secret_access_key
    config['default']['aws_session_token'] = aws_session_token
    with open(aws_credentials_file, 'w') as configfile:
        config.write(configfile)
    print('AWS config has been updated successfully')

def get_sts_token():
    """Returns aws sts token"""
    sts_token_response = _get_sts_token_response()
    resp_dict = _parse_aws_response(sts_token_response=sts_token_response)
    if len(resp_dict) > 0:
        aws_access_key_id = resp_dict['Credentials'].get('AccessKeyId')
        aws_secret_access_key = resp_dict['Credentials'].get('SecretAccessKey')
        aws_session_token = resp_dict['Credentials'].get('SessionToken')
        _write_aws_credentials(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
    else:
        print('ERROR - no access key obtained')


if __name__ == '__main__':
    get_sts_token()
