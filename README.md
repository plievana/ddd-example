# About

Repo copied from https://github.com/CodelyTV/scala-ddd-example and translated to python

# CodelyTV HTTP API

Project showing up how you could implement a HTTP API with Python.
 
This is the first iteration of the project where you will find a very Object Oriented approach. We've followed the Ports & Adapters (or Hexagonal Architecture) Software Architecture using `trait`s as the domain contracts/ports in order to be implemented by the infrastructure adapters.

## Contents

* [Endpoints](#endpoints)
* [Environment setup](#environment-setup)


## Endpoints

One of the goals of this project is to serve as an example illustrating how to implement several concepts you would commonly find in any production application. In order to accomplish so, we have implemented the following 5 endpoints:
* `GET /status`: Application status health check.
* `POST /videos`: Create new video inserting it into the database and publishing the `video_created` domain event to the message queue.
* `GET /videos`: Obtain all the system videos.
* `POST /users`: Create new user inserting it into the database and publishing the `user_registered` domain event to the message queue.
* `GET /users`: Obtain all the system users.

## Environment setup

### Install the needed tools
1. Clone this repository: `git clone https://github.com/CodelyTV/cqrs-ddd-scala-example.git cqrs-ddd-scala-example`
2. Create virtual environment: `python3 -m venv venv`
3. Activate virtualenv: `. venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`


### Infrastructure needs:
1. Mongodb
2. rabbitmq

### Start http server
1. `export FLASK_ENV=development`
2. `export FLASK_APP="project:create_app()"`
3. `flask run`

### To run tests:
```bash
$> pytest
```
