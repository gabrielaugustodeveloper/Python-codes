alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
N = int(input("Insira o valor de N: "))
wordlist = []
numeros = [0] * 26
i = 0

while N != 0:
    word = input("Digite a palavra:")
    wordlist = list(word)
    for i in range(len(numeros)):
        if alfabeto[i] in wordlist[i]:
            numeros[i] = i + 1
            i = i + 1

    N = N - 1

for i in alfabeto:
    print(i, numeros)

