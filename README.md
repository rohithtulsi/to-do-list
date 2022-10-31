# To-Do-List-App
A To Do List App was created using django, which helps in noting down all tasks required to complete in one place.

This app has User Authentication with multiple lists where each list has a title and description.
Under each list there are respective Tasks and each task has title, description, complete status, priority, and due date.
The user will be able to search a task, filter tasks based on priority or complete status.
The user will be able to view all this tasks with respective due dates on the calendar view.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rohithtulsi/to-do-list.git
$ cd to-do-list
```

Create a virtual environment to install dependencies in and activate it:
  
```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/users/`.
