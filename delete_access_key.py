#!/usr/bin/env python
# encoding: utf-8

import sys
from aws_api import aws_connection_context
from list_profiles import get_list_profiles_output
from list_access_keys import get_list_access_keys


def delete_access_key_id(conn_context, access_key_id):
    delete_access_key = conn_context.delete_access_key(AccessKeyId=access_key_id)
    return delete_access_key


if __name__ == '__main__':
    print(get_list_profiles_output())
    profile_name = str(input('Enter profile name to be used in AWS context: '))
    iam = aws_connection_context(profile_name)

    # print list of current access keys
    get_list_access_keys(conn_context=iam)

    access_key_id_delete = str(input('Enter AccessKeyId to be deleted: '))
    try:
        deleted_access_key = delete_access_key_id(conn_context=iam, access_key_id=access_key_id_delete)
    except iam.exceptions.NoSuchEntityException as err:
        print(f'ERROR - {err}')
        sys.exit()

    response_code = deleted_access_key.get('ResponseMetadata').get('HTTPStatusCode')

    if response_code == 200:
        print(f'INFO - AccessKey {access_key_id_delete} has been deleted')
    else:
        print(f'Error: {deleted_access_key}')
        sys.exit()

    get_list_access_keys(conn_context=iam)
