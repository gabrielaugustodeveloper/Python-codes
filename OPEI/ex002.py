grupos = int(input("Digite o numero de grupos a serem analisados:\n"))


for i in range(grupos):
    pessoas = int(input(f"Quantas pessoas tem no grupo {i+1}?\n"))
    nomes = []
    saldo = {}
    for i in range(pessoas):
        nome = input(f"Digite o nome da pessoa {i+1}:\n")
        nomes.append(nome)
        saldo[nome] = 0

    for nome in nomes:
        dados = input(f"Digite os dados da pessoa {nome} (dinheiro gasto, número de amigos e os nomes dos amigos):\n").split()
        dinheiro = int(dados[0])
        num_amigos = int(dados[1])

        if num_amigos > 0:
            valor_por_amigo = dinheiro // num_amigos
            sobra = dinheiro % num_amigos

            saldo[nome] -= (dinheiro - sobra)

            for i in range(2, 2 + num_amigos):
                amigo = dados[i]
                saldo[amigo] += valor_por_amigo
    for nome in nomes:
        print(f"{nome} {saldo[nome]}")




