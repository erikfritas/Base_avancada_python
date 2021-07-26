# Base_avancada_python
## Base avançada para quem quer estudar python.

## ESTE código não possui licença então se quiser usar em um projeto próprio seu, eu não me importaria.


### Modo de uso:

<h2>Certifique-se de estar na mesma pasta que o arquivo do jogo...</h2>

<ul>
<h2>1º Passo "instalar o módulo de keyboard":</h2>
    <li>
    ° Windows:
        caso não tenha o pip instalado então execute o código no seu terminal:
             `python -m pip install -U keyboard`
        caso contrário então execute apenas:
             `pip install keyboard`
    </li>
    <li>
    ° Linux:
        aqui é muito mais fácil do que parece, então vou dar um passo à passo mais detalhado:
             caso não tenha o python instalado execute o código no seu terminal:
                  `sudo apt install python3`
             ok, agora instale o pip se vc não tiver ele:
                  `sudo apt install python-pip`
    </li>

<h2>2º Passo "executar o código em python":</h2>
    <li>
    se vc não tiver uma ide instalada, então contanto que vc já tenha pelo menos o python instalado então execute o código no seu terminal (Prompt de comando):
        ° Windows:
            `python jogo.py`
        ° Linux:
            `python3 jogo.py`
    </li>
         
<h2>3º Passo "jogar":</h2>
    <li>
    o controle padrão que eu coloquei foi:
       w -> cima
       s -> baixo
       a -> esquerda
       d -> direita
    </li>
       
<h2>4º E último passo "programar":</h2>
    <li>
    vc pode utilizar tanto a sua ide para editar o código, quanto o bloco de notas ou até mesmo o IDLE que vem junto do próprio python quando vc instala no windows.
    </li>
    <li>
        <ul>
            <h2>para vc programar usando meu código base é bem simples, segue à documentação abaixo:</h2>
            <li>
               A classe Player, como o próprio nome já diz... cria o player, então tome muito cuidado ao usá-la, tente fazer como eu fiz na função update da classe Game, pois se vc colocá-la diretamente no loop, ela ficará recriando o player toda hora na posição inicial dele.
            </li>
            <li>
               A classe Game, é a classe do jogo, basicamente é aqui que todas as classes vão ser chamadas, de acordo com a necessidade, por isso criei as funções update e render, por questões de organização das necessidades.
            </li>
        </ul>
</ul>

