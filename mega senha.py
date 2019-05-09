#define a função jogo
def jogo():
    #gera a senha
    import random
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(n)
    #posições
    p1 = random.choice(n)
    p2 = random.choice(n)
    p3 = random.choice(n)
    p4 = random.choice(n)
    p5 = random.choice(n)
    #número de vidas
    v = 10
    #variavel dicas vazia
    dicas = ' '
    #para repetir o codigo enquanto há vidas 
    while v > 0 and v <= 10:
        dicas = ' '
        # variavel para um número digitado pelo usuario
        n1 = int(input())
        #o número deve ser menor que 10
        if n1 >= 0 and n1 < 10:
            #se o número for valido irá executar para ver se o n1 é igual a p1 
            if n1 == p1:
                # se o número for igual dicas será igual a +1
                dicas = dicas + '+1 '
            #se o n1 é diferente de p1 ele irá verificar se n1 é igual as outras posições
            elif n1 == p2 or n1 == p3 or n1 == p4 or n1 == p5:
                # se n1 for igual a qualquer outra posição dicas será igual a 0
                dicas = dicas + '0 '
            # se n1 não está em nenhuma posição
            else:
                #dicas será igual a -1
                dicas = dicas + '-1 '
        else:
            print("numero invalido")
        n2 = int(input())
        if n2 >= 0 and n2 < 10:           
            if n2 == p2:
                dicas = dicas + '+1 '
            elif n2 == p1 or n2 == p3 or n2 == p4 or n2 == p5:
                dicas = dicas + '0 '
            else:
                dicas = dicas + '-1 '
        else:
            print ("numero invalido")
        n3 = int(input())
        if n3 >= 0 and n3 < 10:
            if n3 == p3:
                dicas = dicas +'+1 '
            elif n3 == p1 or n3 == p2 or n3 == p4 or n3 == p5:
                dicas = dicas +'0 '
            else:
                dicas = dicas + '-1 '
        else:
            print("numero invalido")
        n4 = int(input ())
        if n4 >= 0 and n4 < 10:
            if n4 == p4:
                dicas = dicas + '+1 '
            elif n4 == p1 or n4 == p2 or n4 == p3 or n4 == p5:
                dicas = dicas +'0 '
            else:
                dicas = dicas + '-1 '
        else:
            print("numero invalido")
        n5 = int(input())
        if n5 >= 0 and n5 < 10:
            if n5 == p5:
                dicas = dicas + '+1 '
            elif n5 == p1 or n5 == p2 or n5 == p3 or n5 == p4:
                dicas = dicas + '0 '
            else:
                dicas = dicas + '-1 '
        else:
            print("numero invalido")
        # vai mostrar todas as dicas na tela 
        print (dicas)
        # se todas as dicas forem +1
        if n1 == p1 and n2 == p2 and n3 == p3 and n4 == p4 and n5 == p5:
            #vai mostrar na tela a mensagem
            print ("você ganhou! PARABÉNS")
        # se as dicas forem diferente de +1
        elif 'n1, n2, n3, n4, n5 ' != 'p1, p2, p3, p4, p5':
            #vai mostrar na tela a mensagem
            print ("tente de novo")
        #para as vidas diminuirem     
        v-=1
        #dicas vazias para tentar de novo
        dicas=''
#pergunta se o usuario quer jogar        
qj = input(" Quer adivinhar a senha? (S/N)")
#se a resposta for s
if qj == 's' or qj == 'S':
    #vai iniciar a função
    jogo()


