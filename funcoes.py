def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    return posicoes

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota:
        frota[navio].append(posicoes)
    else:
        frota[navio] = [posicoes]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0 for i in range(10)] for j in range(10)]
    for navio in frota:
        for posicoes in frota[navio]:
            for posicao in posicoes:
                linha, coluna = posicao
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    cont = 0
    for tipo_navio in frota.values():
        for navio in tipo_navio:
            afundou = True
            for posicao in navio:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                    break
            if afundou:
                cont += 1
    return cont
