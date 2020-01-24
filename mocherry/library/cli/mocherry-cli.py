#!/usr/bin/env python
from zipfile import ZipFile
import sys
import os
import argparse


PROJECT_ZIP     =   "project.zip"
APP_ZIP         =   "app.zip"


def main():
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
    if None == project_name:
        print ("Error: Must provide a project name.")
        return None

    if os.path.isabs(project_name) is False:
        target_path = os.path.join(os.getcwd(), project_name)

    # Source path to create project
    source_path = os.path.dirname(os.path.abspath(__file__)) + "/../../resources/samples/" + PROJECT_ZIP

    # Extract zip to create project
    with ZipFile(source_path, 'r') as zip_obj:
        print('Creating new project: {}'.format(project_name))
        zip_obj.extractall(target_path)


def create_new_app(app_name=None):
    # Validation for App Name
    if None == app_name:
        print ("Error: Must provide a app name.")
        return None

    if os.path.isabs(app_name) is False:
        target_path = os.path.join(os.getcwd(), app_name)

    # Source path to create app
    source_path = os.path.dirname(os.path.abspath(__file__)) + "/../../resources/samples/" + APP_ZIP

    # Extract zip to create app
    with ZipFile(source_path, 'r') as zip_obj:
        print('Creating new app: {}'.format(app_name))
        zip_obj.extractall(target_path)



if __name__ == "__main__":
    main()
