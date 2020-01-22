#!/usr/bin/env python
from zipfile import ZipFile
import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('action', metavar='action', type=str, 
                        help='Action name: startproject, startapp')
    parser.add_argument('value', metavar='params', type=str, nargs='+',
                        help='project name / application name')

    args = parser.parse_args()
    if 'startproject' == args.action.lower():
        create_new_project(args.value[0])
    else:
        print('Not a valid action: {}'.format(args.action))

def create_new_project(target_path=None):
    if os.path.isabs(target_path) is False:
        target_path = os.path.join(os.getcwd(), target_path)

    # with ZipFile('resources/samples/project.zip', 'r') as zip_obj:
    #     print('Creating new project: {}'.format(target_path))
    #     zip_obj.extractall(target_path)

if __name__ == "__main__":
    main()
