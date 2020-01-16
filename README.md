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
Our team is working on the project/app generator rapidly to have a seemless app generation at developer's ease. For now we have provided an base application in the following repository so that you can get started with MoCherry. [Download Sample Application](https://github.com/techunits/mocherry-sample-app)

```sh
$ git clone https://github.com/techunits/mocherry-sample-app.git
$ cd mocherry-sample-app
$ python manage.py runserver  # start WSGI server
[12/Jan/2020:00:52:20] ENGINE Listening for SIGTERM.
[12/Jan/2020:00:52:20] ENGINE Bus STARTING
[12/Jan/2020:00:52:20] ENGINE Set handler for console events.       
[12/Jan/2020:00:52:20] ENGINE Started monitor thread 'Autoreloader'.
[12/Jan/2020:00:52:21] ENGINE Serving on http://localhost:9090
[12/Jan/2020:00:52:21] ENGINE Bus STARTED
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
