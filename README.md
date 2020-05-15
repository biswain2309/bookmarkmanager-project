# Project title

Smart Bookmark Manager .


# Introduction

Bookmark Manager helps you extract data from database as per user's needs. It includes create and browse API that helps one to store and fetch any Customer's bookmark. Also, it allows browsing and filtration of API endpoint with the a list of query parameters.

## Prerequisites

 - Python 3.8.1
 - django 2.2.10
 - django-filter 2.2.0
 - djangorestframework 3.11.0
 - sqLite3(comes inbuilt with Django)

## Setup

**Execute commands to activate Virtual Environment**
 
 _Note - Creating Virtual environment is optional. If you want you can skip the below steps._
 
The below commands are used for managing Virtual Environments using Python3-env.
**Create new environment**

```
python -m venv ~/env

```

**Activate virtual environment**

```
source ~/env/bin/activate

```

**De-activate virtual environment**

```
deactivate

```


**Install requirements from requirements.txt**

```
pip install -r requirements.txt
```


## Execution

**Start Django development server**

```
python manage.py runserver 0.0.0.0:8000

```