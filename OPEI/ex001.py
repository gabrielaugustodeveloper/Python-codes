N = int(input("Digite o número de etapas: "))

for i in range(N):
    T = int(input("Tempo maximo em segundos:"))
    S = int(input("Distancia em metros:"))
    V = int(input("Velocidade media:"))
    tempo_necessario = S / V

    if tempo_necessario <= T:
        print("SIM")
    else:
        print("NÃO")
