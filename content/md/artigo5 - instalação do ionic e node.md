Title: Instalação do Ionic e Node.js no Linux Mint
Date: 2015-10-26 18:30
Category: Artigos
Tags: programação, node, ionic

Estou aprendendo [Ionic] (http://ionicframework.com/), um excelente framework para desenvolvimento de apps móveis híbridos (para IOS e Android).

Tive alguns problemas para instalação, pois o Ionic depende do [Node.js} (https://nodejs.org/), que estava no repositório do Linux Mint com uma versão desatualizada.

Tentei baixar diretamente do [repositório no Github] (https://github.com/nodejs/node), mas lá só havia a versão de desenvolvimento, e, mesmo conseguindo instalá-la, tive problemas para instalar o Ionic mais tarde.

Achei a solução [aqui] (https://github.com/nodejs/node-v0.x-archive/wiki/Installing-Node.js-via-package-manager) e reproduzo os passos abaixo. Estou utilizando Linux Mint 17.

No terminal, configuração e instalação do Node.js:

    :::shell
    curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash -
    sudo apt-get install --yes nodejs

Instalação do Ionic:

    :::shell
    sudo npm install -g ionic

Simples, não? Espero que esse post economize sua dor de cabeça!
