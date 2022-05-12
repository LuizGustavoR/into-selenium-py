# intro-seleniu-py

I've created this repository with the objective to learn about python test automation for web applications.

# Setup Instructions

## Python Setup

- This project needs python version 3.8 or above.

- Also needs pipenv.

## Webdriver Setup

- For this UI Web test it will be necessary the chromedriver latest stable release:
[Chromedriver](https://chromedriver.chromium.org/home).

## Docker Setup

- If you want to scale tests in you machine using docker follow the steps below:
1. Intall docker in your machine.
3. Pull the needed nodes (selenium/hub, selenium/node-chrome, selenium/node-firefox).
4. Spin up nodes with the command "docker-compose up -d"
5. Run the tests
6. Shut down nodes with the command "docker-compose down".

For more information using docker go to
[Scaling Tests with Docker and Python](https://luizdeaguiar.com.br/2022/05/11/scaling-tests-with-docker-and-python/).

## Project Setup

1. Clone this repository.
2. Run `cd intro-selenium-py` to enter into the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to check that the framework can run the testes.

## More setup details

- This repository have the project made from my blog tutorial.
- In case you have any doubt on how to setup Python, Pipenv or Webdriver in your machine,\
follow my blog link with the instructions: [Selenium Webdriver with Python](https://luizdeaguiar.com.br)

# Project made with Python

[![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

# About the Author
Hi, My name is Luiz Gustavo,\
I work as a QA Engineer.\
Follow some contact links.

- [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/luizgustavor/)
- [Blog](https://luizdeaguiar.com.br)

# Thanks

This repository and tutorial were made based in the following course:\
[Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
administred by [Andrew Knight](https://www.linkedin.com/in/andrew-leland-knight/).\
He also have a [Blog](https://automationpanda.com/) :D.