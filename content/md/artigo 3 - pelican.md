Title: Criando um blog com Pelican
Date: 2015-06-30 14:50
Category: Artigos
Tags: pelican, blogging
Status: draft



Blog para programadores...
ferramenta flexível que eu conseguisse utilizar. Tentei Jekyll, mas...
Como estava tentando aprender Python, testo agora o Pelican


# Pré-requisitos

Ter python instalado.

## Instalar pip

A partir do Python 3.4, o pip está incluido na instalação padrão.
Como eu ainda não tinha o pip instalado, bastou utilizar
    :::shell
    sudo apt-get install python-pip

Mais informações sobre instalação do pip (outras plataformas) [aqui](https://pip.pypa.io/en/stable/installing.html).

## Instalando o Pelican com o pip

    :::shell
    sudo pip install pelican

Precisei usar o `sudo`.

## Começando um novo blog

No diretório que você quiser colocar o blog:

    :::shell
    pelican-quickstart


Estrutura de arquivos:

    :::shell
    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

Como configurar github...

Como usar pythonHTTPserver...

Onde colocar as páginasl

