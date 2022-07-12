#!/usr/bin/env python
# encoding: utf-8

from list_profiles import get_list_profiles_output
from aws_api import aws_connection_context
from datetime import datetime, timezone


def get_list_access_keys(conn_context):
    now = datetime.now(timezone.utc)
    list_access_keys = conn_context.list_access_keys().get('AccessKeyMetadata')
    for key in list_access_keys:
        username = key.get('UserName')
        access_key_id = key.get('AccessKeyId')
        created_date = key.get('CreateDate')
        print(f'[INFO] - AccessKey: Username: {username}, AccessKeyId: {access_key_id} Created: {created_date}, Age: {now - created_date}')
    return list_access_keys


if __name__ == '__main__':
    print(get_list_profiles_output())
    profile_name = str(input('Enter profile name to be used in AWS context: '))
    iam = aws_connection_context(profile_name)

    # print list of current access keys
    get_list_access_keys(conn_context=iam)
