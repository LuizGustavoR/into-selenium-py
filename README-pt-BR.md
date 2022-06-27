# intro-seleniu-py

Criei esse repositório com o objetivo de aprender sobre
automação de testes em python para aplicações web.

# Instruções de Setup

## Python Setup

- Esse projeto precisa da versão Python 3.8 ou superior.

- Também precisa de pipenv.

## Webdriver Setup

- Para o teste Web UI será necessário a versão estável mais nova do chromedriver:
[Chromedriver](https://chromedriver.chromium.org/home).

## Docker Setup

- Caso você queirax escalar testes na sua máquina utilizando docker siga as instruções abaixo:
1. Instale o docker na sua máquina.
3. Faça o "Pull" dos nodes necessários (selenium/hub, selenium/node-chrome, selenium/node-firefox).
4. Faça o "Spin up" dos nodes utilizando o comando `docker-compose up -d`
5. Execute os testes
6. Derrube os nodes com o comando `docker-compose down`.

Para mais informação utilizando docker vá para
[Escalando Testes com Docker e Python](https://luizdeaguiar.com.br/pt/2022/05/11/escalando-testes-com-docker-e-python/).

## Setup do projeto

1. Clone esse repositório.
2. Execute `cd intro-selenium-py` para entrar no projeto.
3. Execute `pipenv install` para instalar as dependências.
4. Execute `pipenv run python -m pytest` para validar que o framework consegue rodar os testes.

## Executando tests em paralelo

- O comando para executar testes em paralelo é o mesmo para executar um teste normal, mas no final do comando você deve adicionar "-n" seguido pelo número de testes, por exemplo:
- Execute `pipenv run python -m pytest -n 3`

Para mais informações executando testes em paralelo vá para
[Executando Testes em Paralelo](https://luizdeaguiar.com.br/pt/2022/03/24/executando-testes-em-paralelo/).

## Mais detalhes do setup

- Esse repositório contém o projeto feito a partir do tutorial no meu blog.
- Caso tenha dúvidas de como configurar o Python, o Pipenv ou o Webdriver na sua máquina,\
segue o link das instruções no meu blog: [Selenium Webdriver com Python](https://luizdeaguiar.com.br/?lang=pt)

# Projeto feito com Python

[![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

# Sobre o Autor
Oi, meu nome é Luiz Gustavo,\
Trabalho como QA Engineer.\
segue alguns links para contato.

- [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/luizgustavor/)
- [Blog](https://luizdeaguiar.com.br/?lang=pt)

# Agradecimentos

Esse repositório e tutorial foram feitos baseados no curso:\
[Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
ministrado por [Andrew Knight](https://www.linkedin.com/in/andrew-leland-knight/).\
Ele também possui um [Blog](https://automationpanda.com/) :D.