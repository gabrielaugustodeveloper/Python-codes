palavra = input("Qual palavra deseja usar como base? ")
tentativas = int(input("Digite o número de tentativas: "))
palavralist = list(palavra)
novalist = []



if 1 <= tentativas <= 1000:
    while tentativas != 0:
        novalist = []
        nova = input("Digite a nova palavra:")
        novalist = list(nova)
        numletra = 0
        errado = 0
        for numletra in range(len(palavra)):
            if palavralist[numletra] != novalist[numletra]:
                errado = errado + 1
                numletra = numletra + 1

        tentativas -= 1
        if errado > 2:
            print("NÃO")
        elif errado <= 2:
            print("SIM")
