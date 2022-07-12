#!/usr/bin/env python
# encoding: utf-8

import boto3


def aws_connection_context(profile_name):
    session = boto3.Session(profile_name=profile_name)
    return session.client('iam')


if __name__ == '__main__':
    aws_connection_context(profile_name='default')
