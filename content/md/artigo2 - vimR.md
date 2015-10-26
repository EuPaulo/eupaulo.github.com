Title: Usando vim e R!?
Date: 2015-07-09 21:00
Category: Artigos
Tags: Vim-R-plugin, vim, R, tutorial
Authors: Paulo Miranda Moreira
Status: published


Quando comecei a aprender R (nos idos tempos de 2010), ainda usava Windows, e, até por indicação do professor da disciplina que eu estava cursando, acabei ficando com a interface gráfica para R no Windows. 
Disciplina cursada sem problemas, fiquei algum (bom) tempo sem mexer. Apesar de ter gostado, ainda não tinha noção do *poder do R*!!!

Quando precisei utilizar de novo, me lembrei que alguém na disciplina havia comentado sobre RStudio. Resolvi testar.
Descobri muitas vantagens, como auto completar funções e objetos, destaque de sintaxe, identação. Mais tarde descobri como utilizar RMardown e o pacote `Knitr` para gerar relatórios. 
Estava (e ainda estou) muito satisfeito com o RStudio - a equipe de desenvolvimento não para de criar novas funcionalidades.
Pode ser utilizado por usuários desde o nível básico (inclusive é a IDE recomendada no [curso básico](http://www.anova.biz/cursoR.html) que desenvolvi para a ANΦVA) até o avançado.

Mas senti que estava na hora de avançar um pouco mais. 
No livro "The Pragmatic Programmer", os autores recomendam que um bom programador domine *muito bem* pelo menos um editor de texto.
Levei essa ideia a sério, especialmente porque estou começando a me aprofundar em Python, e gostaria de ter uma única ferramenta para trabalhar em várias linguagens, como R, Python e Latex.
Quando precisava fazer algo em Python e LaTeX, utilizava o Pluma (gedit), o que não era muito eficiente. A tarefa que mais demorava e me angustiava era acertar a identação - na verdade eu acabava desistindo e me conformando com identação errada...

Tentei o rgedit, plugin para utilizar o R no gedit, mas não resolveria e não resolveu o meu problema com outras linguagens.

Pesquisando internet afora, pude perceber que havia duas opções indicadas por bons programadores: Emacs e Vi(m). 
Já havia tentado o Emacs (mais de uma vez), sem sucesso. Achei meio confuso cheio de comandos `M-x` que não faziam sentido para mim.
Decidi encarar o Vim, mesmo sabendo que a curva de aprendizado, quando comparada à de outros editores de texto, é assim:

<center>

![vimLearningCurve]({filename}/images/vimLearningCurve.png)

*Atenção: Isso é apenas uma brincadeira. Se você ainda receia usar o Vim por considerá-lo difícil, leia [este artigo](https://robots.thoughtbot.com/the-vim-learning-curve-is-a-myth).*

</center>


Brincadeiras à parte, não é que gostei? Fiz o tutorial que vem no editor e estou me acostumando com os comandos. Esse post está sendo escrito utilizando Vim ;)
A próxima parte seria entender como usar o R com Vim. Compartilho com você a aventura de instalar o Vim-R-plugin, aventura um tanto quanto selvagem, mas que no final valeu a pena. Não posso deixar de destacar que o Vim-R-plugin foi desenvolvido e é mantido por um brasileiro!!! A [Jakson Alves de Aquino](http://www.lepem.ufc.br/aquino.php), meu reconhecimento e agradecimento.



**Importante:** estou utilizando Linux Mint 17, vim 7.4 e Vim-R-plugin 1.2.6. Se você usa outra distribuição Linux esses passos talvez não funcionem, e se você usa outro sistema operacional, informe-se na página de [documentação](http://www.lepem.ufc.br/jaa/r-plugin.html) do plugin.


# Mãos à obra
## Instalando pré-requisitos 

### Instalação do Vim

    :::shell
    sudo apt-get install vim


Checar se Vim tem instalado os features `+libcall`, `+clientserver` e `+conceal`. No terminal:

    :::shell
    vim

E depois que o Vim abrir:
    
    :::vim
    :version
  
No meu caso faltava o `+clientserver`. Para resolver o problema bastou instalar o pacote `vim-gnome`:

    :::shell
    sudo apt-get install vim-gnome

### Instalação e configuração do R

Se você ainda não o fez, instale o [R](http://r-project.org/) (versão 3.0.0 ou superior)

Instalar o pacote vimcom no R a partir do código fonte. Para isso antes é necessário antes instalar o *X11 headers*:

    :::shell
    sudo apt-get install libx11-dev
  
Depois, no R, basta utilizar o código abaixo para instalar o pacote `vimcom`

    :::r
    download.file("http://www.lepem.ufc.br/jaa/vimr/vimcom_1.2-6.tar.gz",
                  destfile = "vimcom_1.2-6.tar.gz")
    install.packages("vimcom_1.2-6.tar.gz", type = "source",
                      repos = NULL)


O arquivo .Rprofile é um arquivo de configuração que guarda suas opções e pacotes a serem carregados ao se iniciar o R. Colocar no arquivo .Rprofile:

    :::r
    if(interactive()){
        options(vimcom.verbose = 1) # opcional
        library(vimcom)
    }
 
               
                    
### Instalação do tmux:

O tmux (terminal multiplexer) permite a utilização do editor de texto e do R na mesma janela do terminal.
  
    :::shell
    sudo apt-get install tmux
  
### Instalação wmctrl:
       
    :::shel
    sudo apt-get install wmctrl
    
### Configurações
  
Colocar no arquivo .bashrc:

    :::shell
    alias vimr="vim --servername VIM"
   
*Observação: a documentação sugere usar o alias `vim`. Escolhi `vimr` porque vou utilizá-lo para abrir arquivos `.R`. Começar nova sessão shell para o alias funcionar.

Colocar no `.vimrc`. Caso você não esteja acostumado com o vim, o arquivo `.vimrc` é um arquivo colocado no seu diretório Home que contem suas configurações do vim.

    :::vim 
    set nocompatible
    syntax enable
    filetype plugin on
    filetype indent on
    
## Instalação do Vim-R-Plugin
   
Baixar a última versão do plugin [aqui](http://www.vim.org/scripts/script.php?script_id=2628).

No diretório em que o plugin baixado está, execute no terminal:

    :::shell 
    vim Vim-R-plugin.vmb

Depois que uma tela como essa aparecer:   

<center>

<img src="/images/instalandoPlugin.png" alt="instalandoPlugin" style="width: 35em;"/>

</center>

Execute `:so %` e aperte `Enter` quantas vezes for necessário até o fim da instalação.

Quando uma tela como essa aparecer:

<center>

<img src="/images/fimInstalaçãoRPlugin.png" alt="fimInstalaçãoRPLugin" style="width: 35em;"/>

</center>

saia do vim digitando `:q`.


Parabéns! Você concluiu a instalação do Vim-R-Plugin. Agora veja abaixo como iniciar uma sessão do vim com R.
 
Para entrar, execute no terminal:

    :::shell
    tmux
    vimr novoArquivo.R

Aparecerá tela normal do Vim. Para sessão interativa do R, digite no modo normal:

    :::vim
    \rf
    
Você deverá ver a tela abaixo:

<center>

<img src="/images/finalVimR.png" alt="finalVimR" style="width: 35em;"/>

</center>


## Instalação de opcionais do Vim-R-Plugin

Alguns plugins e pacotes adicionais sugeridos na [documentação](http://www.lepem.ufc.br/jaa/r-plugin.html) podem melhorar a visualização do código no terminal.

### colorout

O output no terminal não oferece destaque de sintaxe. Você pode adicionar cor ao output utilizando o pacote colorout.

no R:

    :::R
    download.file("http://www.lepem.ufc.br/jaa/vimr/colorout_1.1-1.tar.gz",
                  destfile = "colorout_1.1-1.tar.gz")
    install.packages("colorout_1.1-1.tar.gz", type = "source", repos = NULL)

Não se esqueça de colocar `library(colorout)` no `.Rprofile`, dentro das chaves do `if(interactive())` que foi colocado anteriormente.

### setwidth

Ajusta automaticamente a largura da sessão do R no terminal de acordo com o tamanho da janela.
É um pacote que pode ser instalado do CRAN:

    :::R
    install.packages("setwidth").
    
Adicione ao arquivo `.Rprofile` o comando `library(colorout)`, dentro das chaves do `if(interactive())`.
    
### ncurses-term

Suporte para 256 cores no emulador de terminal - ncurses-term. No terminal:
    
    :::shell
    sudo apt-get install ncurses-term

### latexmk

Automatiza a compilação de documentos LaTeX para produção de relatórios utilizando `Sweave()` ou `knitr()`.

## Pronto :)

Assim você está pronto para utilizar o R com o *poder do Vim*! Em um próximo post mostrarei como uso o Vim-R-Plugin. Caso queira mais informações, não deixe de checar a [documentação](http://www.lepem.ufc.br/jaa/r-plugin.html).
