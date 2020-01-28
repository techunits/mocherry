
# MoCherry
MoCherry is built around CherryPy & mongoengine to support REST webserivces with very low memory footprint, support for MongoDB ORM, built-in WSGI server and faster initilization.

# Features
  - In-built REST webservice support
  - MongoDB ORM support with MongoEngine plugin
  - Similar usability & file system structure like Django to reduce the learning curve
  - Low memory footprint
  - In-built CherryPy WSGI server
  - Built-in basic encryption support
  - MIT licensed

# Installation
Currently MoCherry is not deployed to python pip repository. We will soon deploy it there for developers' convenience. In the meantime following steps can be followed to install mocherry to your development environment. The following command will download and install MoCherry and all it's required dependencies to your system or virtualenv.
```sh
$ pip install git+https://github.com/techunits/mocherry.git
```

# Create First Application
Now MoCherry consists of a cli script which will enable developers to create a sample project / app from command-line without manually download it from github. Steps as follows:
### Create project skeleton
```sh
$ mocherry-cli startproject "my_project_001"
Downloading sample project: https://github.com/techunits/mocherry/blob/mocherry/resources/samples/project.zip?raw=true
Creating new project: my_project_001
$ cd my_project_001
$ python manage.py runserver  # start WSGI server
[20/Jan/2020:00:52:20] ENGINE Listening for SIGTERM.
[20/Jan/2020:00:52:20] ENGINE Bus STARTING
[20/Jan/2020:00:52:20] ENGINE Set handler for console events.       
[20/Jan/2020:00:52:20] ENGINE Started monitor thread 'Autoreloader'.
[20/Jan/2020:00:52:21] ENGINE Serving on http://localhost:9090
[20/Jan/2020:00:52:21] ENGINE Bus STARTED
```

### Create applicaiton skeleton
Lets assume you have already created a project by following above steps, then you have to go inside that project and create app skeleton as per your requirements.
```sh
# Application name: app_001
$ mocherry-cli startapp "app_001"
Downloading sample app: https://github.com/techunits/mocherry/blob/develop/mocherry/resources/samples/app.zip?raw=true
Creating new app: app_001

# Application name: app_002
$ mocherry-cli startapp "app_002"
Downloading sample app: https://github.com/techunits/mocherry/blob/develop/mocherry/resources/samples/app.zip?raw=true
Creating new app: app_002

$ python manage.py runserver  # start WSGI server
[20/Jan/2020:00:52:20] ENGINE Listening for SIGTERM.
[20/Jan/2020:00:52:20] ENGINE Bus STARTING
[20/Jan/2020:00:52:20] ENGINE Set handler for console events.       
[20/Jan/2020:00:52:20] ENGINE Started monitor thread 'Autoreloader'.
[20/Jan/2020:00:52:21] ENGINE Serving on http://localhost:9090
[20/Jan/2020:00:52:21] ENGINE Bus STARTED
```


# MoCherry Management Commands
MoCherry framework also support custom management commands to enhance its CLI capabilities. With the framework sample code we have provided a test command to verify how it works

```sh
$ python manage.py test
Success: This is a test command
```

# Sample Applications
 - https://github.com/techunits/mocherry-sample-app
 - https://github.com/techunits/mocherry-sample-rest-app
