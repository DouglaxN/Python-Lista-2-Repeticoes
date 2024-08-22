#Baseado no problema beecrowd | 1158 (Ultrapassando Soma de Ímpares Consecutivos III)

#Imagine que você trabalha como engenheiro de redes em uma empresa de telecomunicações. Sua tarefa é otimizar a distribuição de dados entre várias torres de transmissão para melhorar a cobertura de rede em uma região específica. Para isso, você precisa calcular a capacidade de transmissão de cada torre baseada em certas configurações.

#Cada configuração de torre é representada por um par de inteiros X e Y. O inteiro X representa a capacidade inicial de transmissão, e Y indica quantas atualizações consecutivas de capacidade devem ser feitas, onde cada atualização aumenta a capacidade com números ímpares consecutivos. Sua tarefa é calcular a soma das capacidades atualizadas para determinar o aumento total necessário.

#Por exemplo, se a capacidade inicial X é 4 e são necessárias 5 atualizações, você deve somar os próximos 5 números ímpares a partir de 4. Se X fosse 7 e fossem necessárias 4 atualizações, você somaria os próximos 4 números ímpares a partir de 7.

#Entrada A primeira linha de entrada é um inteiro N que indica a quantidade de casos de teste que vêm a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

#Saída Imprima a soma dos Y números ímpares consecutivos a partir do valor X.

numero_casos = int(input("Quantidade de casos de teste: "))

for _ in range(numero_casos):
    entrada = input("Caso de teste: ")

    X = 0 
    Y = 0
    i = 0

    while i < len(entrada) and entrada[i] != ' ':
        X = X * 10 + int(entrada[i])
        i += 1
    
    i += 1

    while i < len(entrada):
        Y = Y * 10 + int(entrada[i])
        i += 1

    soma = 0
    cont = 0
    while cont < Y:
        if X % 2 != 0:
            soma += X
            cont += 1
        X += 1

    print(f"Soma dos Y números ímpares a partir de X: {soma}")
