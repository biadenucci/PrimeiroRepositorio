#print('Ctrl+Play)

#print('O que acontece se você passra o valor 0 para o segundo argumento de int()?')
# x = input('Digite seu numero: ')
# y = input('Digite outro numero:  ')

#print(int(x)/int(y))

#try:
    #f = open('arquivo.txt', 'w')
    #f.write('tente escrever isso')
#except IOError:
     # Isso so ira verificar  se ha uma exceção IOError e,
     # em seguida, executra essa declaração de impressão
    #print('Erro: não foi possivel encontrar o arquivo')
#else:
    #print('Conteudo gravado com sucesso')
    #f.close()


#f = open('arquivo.txt', 'w')
#f.write('tente escrever isso')
#print:('Conteudo gravado com sucesso')
#f.close()

def perguntaNumero():
    numero = 1
    while True:
        try:
            val = int(input("Digite um numero inteiro: "))
        except:
            print("Parece que você não digitou um numero inteiro!")
            continue
        else:
            print("Obrigado por digitar um numero inteiro!")
            break
        finally:
            print(f"Tentativa numero: {numero}")
            numero += 1
    print(val)

perguntaNumero()

