import random

jogarNovamente = int(input("Deseja jogar novamente? [1-sim,2-não]: "))
jogadas = 0
jogador = 1 #Sendo: 1 = jogador, 2 = Máquina
maximoJogadas = 9
vitoria = False #Para verificar se há vitória
mesa = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
]

#Função para desenhar o tabuleiro do jogo da velha
def desenho():
    global mesa
    global jogadas
    print("Colunas:   0   1   2")
    print()
    print("Linha 0:  ",mesa[0][0] + " | " + mesa[0][1] + " | " + mesa[0][2])
    print("          -----------")
    print("Linha 1:  ",mesa[1][0] + " | " + mesa[1][1] + " | " + mesa[1][2])
    print("          -----------")
    print("Linha 2:  ",mesa[2][0] + " | " + mesa[2][1] + " | " + mesa[2][2])
    print()
    print("Jogadas:",jogadas)

#Função para quando for a vez do jogador
def vezJogador():
    global jogadas
    global jogador
    global maximoJogadas
    global mesa
    if jogador == 1 and jogadas < maximoJogadas:
        linha = int(input("Qual linha?: "))
        coluna = int(input("Qual coluna?: "))
        while mesa[linha][coluna] != " ":
            linha = int(input("Qual linha?: "))
            coluna = int(input("Qual coluna?: "))
        mesa[linha][coluna] = "X"
        jogador = 2
        jogadas = jogadas + 1

#Função para quando for a vez da máquina
def vezMaquina():
    global jogadas
    global jogador
    global maximoJogadas
    global mesa
    if jogador == 2 and jogadas < maximoJogadas:
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while mesa[linha][coluna] != " ":
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
        mesa[linha][coluna] = "O"
        jogador = 1
        jogadas = jogadas + 1

#Função para verificar se houve vencedor
def verificaVitoria():
    global mesa
    verifica = False
    xo = ["X","O"]
    for i in xo:
        verifica = False
#Verificando por linha
        linhas = 0
        colunas = 0
        while linhas < 3:
            soma = 0
            colunas = 0
            while colunas < 3:
                if (mesa[linhas][colunas]==i):
                    soma = soma + 1
                colunas = colunas + 1
            if soma == 3:
                verifica = i
                break
            linhas = linhas + 1
        if verifica != False:
            break
#Verificando por colunas
        linhas = 0
        colunas = 0
        while colunas < 3:
            soma = 0
            linhas = 0
            while linhas < 3:
                if mesa[linhas][colunas]== i:
                    soma = soma + 1
                linhas = linhas + 1
            if soma == 3:
                verifica = i
                break
            colunas = colunas + 1
        if verifica != False:
            break
#Verificar agora por diagonais
#Diagonal 1        
        soma = 0
        diagonal = 0
        while diagonal < 3:
            if mesa[diagonal][diagonal] == i:
                soma = soma + 1
            diagonal = diagonal + 1
        if soma == 3:
            verifica == i
            break
#Diagonal 2
        soma = 0
        diagonallinha = 0
        diagonalcoluna = 2
        while diagonalcoluna >= 0:
            if mesa[diagonallinha][diagonalcoluna] == i:
                soma = soma + 1
            diagonallinha = diagonallinha + 1
            diagonalcoluna = diagonalcoluna - 1
        if soma == 3:
            verifica == i
            break
    return verifica

#Função para zerar o jogo
def zerar():
    global mesa
    global jogadas
    global jogador
    global maximoJogadas
    global vitoria
    jogadas = 0
    jogador = 1
    maximoJogadas = 9
    vitoria = False
    mesa = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
    ]
        
        
#Para jogar novamente
while jogarNovamente == 1:    
    while True:
        desenho()
        vezJogador()
        vezMaquina()
        vitoria = verificaVitoria()
        if vitoria != False or jogadas >= maximoJogadas:
            desenho()
            break
    print("FIM")
    if vitoria == "X" or vitoria == "O":
        print("Resultado: Jogador",vitoria+","" venceu!")
    else:
        print("Resultado: Empate")
    jogarNovamente = int(input("Deseja jogar novamente? [1-sim,2-não]: "))
    zerar()
        