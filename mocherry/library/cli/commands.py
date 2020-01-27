#!/usr/bin/env python
from zipfile import ZipFile
import sys
import os
import argparse
import requests
import io

PROJECT_ZIP     =   'https://github.com/techunits/mocherry/blob/develop/mocherry/resources/samples/project.zip?raw=true'
APP_ZIP         =   'https://github.com/techunits/mocherry/blob/develop/mocherry/resources/samples/app.zip?raw=true'

def execute_command():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('action', metavar='action', type=str, 
                        help='Action name: startproject, startapp')
    parser.add_argument('value', metavar='params', type=str, nargs='+',
                        help='project name / application name')

    args = parser.parse_args()
    if 'startproject' == args.action.lower():
        create_new_project(args.value[0])
    elif 'startapp' == args.action.lower():
        create_new_app(args.value[0])
    else:
        print('Not a valid action: {}'.format(args.action))


def create_new_project(project_name=None):
    # Validation for Project Name
    if project_name is None:
        print ('Error: Must provide a project name.')
        return None

    if os.path.isabs(project_name) is False:
        target_path = os.path.join(os.getcwd(), project_name)

    # download and create the project from sample
    print('Downloading sample project: {}'.format(PROJECT_ZIP))
    r = requests.get(PROJECT_ZIP)
    with ZipFile(io.BytesIO(r.content)) as zip_obj:
        print('Creating new project: {}'.format(project_name))
        zip_obj.extractall(target_path)

    # override project name settings
    with open(os.path.join(target_path, 'manage.py'), 'r') as fp:
        contents = fp.read().replace('{{app_name}}', project_name)

    with open(os.path.join(target_path, 'manage.py'), 'w') as fp:
        fp.write(contents)
    

def create_new_app(app_name=None):
    # Validation for App Name
    if app_name is None:
        print ('Error: Must provide a app name.')
        return None

    if os.path.isabs(app_name) is False:
        target_path = os.path.join(os.getcwd(), app_name)

    # Source path to create app
    # source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources', 'samples', APP_ZIP)

    # Extract zip to create app
    # with ZipFile(source_path, 'r') as zip_obj:
    #     print('Creating new app: {}'.format(app_name))
    #     zip_obj.extractall(target_path)

    import tempfile
    print(tempfile.gettempdir())
