#!/usr/bin/env python
# encoding: utf-8

from aws_api import aws_connection_context
from list_profiles import get_list_profiles_output
from list_access_keys import get_list_access_keys


def create_access_key(conn_context):
    result = conn_context.create_access_key()
    return result


if __name__ == '__main__':
    print(get_list_profiles_output())
    profile_name = str(input('Enter profile name to be used in AWS context: '))
    iam = aws_connection_context(profile_name)

    # print list of current access keys
    list_access_keys = get_list_access_keys(conn_context=iam)

    if len(list_access_keys) >= 2:
        print('User already has maximum allowed 2 access keys. Please delete one of them before creating a new one')
    else:
        new_access_key = create_access_key(conn_context=iam)
        new_access_key_id = new_access_key.get('AccessKey').get('AccessKeyId')
        new_access_key_secret = new_access_key.get('AccessKey').get('SecretAccessKey')
        print(f'[INFO] - New Access Key created: {new_access_key_id} SecretAccessKey: {new_access_key_secret}')
