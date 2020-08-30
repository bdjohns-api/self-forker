# Self Forker

A simple flask application which, provided an authenticated github user creates a fork of its own
repository in the users github account.

## Local Development

This application is configured to run via python flask on its local host under port 8080, it can
be run using either the provided Dockerfile or using a python virtual environment using Pipenv.

### Running via Docker

The attached dockerfile should configure the application to run within the container on port 8080,
to get a sample container started simply run from the root directory of the project:

```
$ docker build -t self-forker:0.0.1 .  # Create the docker instance
$ docker run --rm -p 8080:8080 self-forker:0.0.1  # Start a local session
```

### Running via Pipenv

In the case that running under Docker isn't an amenable situation the application can also be run
directly via Pipenv. To do so simply run the following commmand from the `src/` directory:

```
$ pipenv run python run.py
```

