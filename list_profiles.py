#!/usr/bin/env python
# encoding: utf-8

import subprocess


def get_list_profiles_output():
    print('List of configured profiles:')
    try:
        process = subprocess.run(['aws', 'configure', 'list-profiles'], text=True)
        return process
    except FileNotFoundError as e:
        return e


if __name__ == "__main__":
    print(get_list_profiles_output())
