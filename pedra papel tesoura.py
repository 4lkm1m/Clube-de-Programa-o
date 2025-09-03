import random
opcao = ['tesoura','pedra','papel']
    
while 1:
    comp = opcao[random.randint(0,2)]
    user = input('pedra, papel ou tesouuura')
    
    print (f'O computador escolheu {comp}')
    
    if (user == 'pedra' and comp == 'tesoura'): print ("voce ganhou!")
    elif (user =='tesoura' and comp == 'papel'): print ('voce ganhou!')
    elif (user == 'papel' and comp == 'pedra'): print ('voce ganhou!')
    elif (user == comp): print ('empate')
    else: print ('voce perdeu')
    
    sair = input('gostaria de jogar de novo?')
    if sair == 'sim': continue
    else : break
