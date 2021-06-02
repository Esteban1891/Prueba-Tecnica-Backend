<h1 align="center"> Welcome to Backend Sisben office! </h1>

![logo](https://miro.medium.com/max/2800/0*8sdbucqAT-9dkwG8)

## Introduction :notebook:

This repository contains all the technical test to validate skills in the backend

## Table of Contents :open_file_folder:

* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Author](#author)

## About
You are on your way to getting to know the backend

1. **python/django installation:** :black_nib:
* How to install django
* How to run a virtual environment
* How to install third party packages
* How to run current packages
* How to handle django commands


## Requirements

* Ubuntu 20.04 LTS | WSL 2 on Windows | MacOS 10.15.7
* python 3.9.1
* Django 3.1.6
* pip 21.0.1
* All programs were run on a Vagrant(ubuntu/trusty64) (Virtualbox) environment

## Installation

![drf](https://www.azulschool.net/wp-content/uploads/2021/04/Creacion-y-consumo-de-APIs-con-Django-REST-Framework.png)
In your terminal, git clone the directory with the following command:

```sh
git clone https://github.com/Esteban1891/Prueba-Tecnica-Backend
```

#### Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv env`
4. Activate the virtual environment by running `source env/bin/activate`

- On Windows use `env\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

7. Migrate existing db tables by running `python manage.py migrate`

8. Run the django collectstatic `python manage.py collectstatic`

9. Run the django development server using `python manage.py runserver 3000`



## Information to admin django
```python
python manage.py createsuperuser
```
| user | password | Description |
| ----- | ----- | ------ |
| admin | admin123 | Admin |


## Author 

[Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)
