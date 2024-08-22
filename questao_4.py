#Baseado no problema beecrowd | 1478 (Matriz Quadrada II)

#Imagine que você foi convidado a participar de uma competição nacional de programação, onde o desafio final envolve uma tarefa crucial para a sobrevivência de uma cidade futurista.

#A cidade de Matrizópolis é conhecida por suas impressionantes estruturas tecnológicas e por seu sistema de energia que depende de uma complexa rede de matrizes. No coração da cidade, existe um supercomputador responsável por controlar essa rede, garantindo que a energia flua eficientemente para todas as áreas, desde residências até hospitais.

#Recentemente, houve uma falha no sistema, e a cidade está enfrentando quedas de energia intermitentes. Os engenheiros de Matrizópolis descobriram que a solução para esse problema está em reconfigurar as matrizes de controle. No entanto, o algoritmo original foi perdido, e eles precisam de alguém com habilidades excepcionais em pensamento computacional para recriá-lo.

#Você, um dos programadores mais promissores, foi chamado para essa missão. Sua tarefa é escrever um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente à ordem de uma matriz M de inteiros, e construa a matriz de acordo com um padrão específico.

#Para complicar ainda mais, a entrada consiste de vários inteiros, um valor por linha, correspondendo às ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0). Para cada inteiro da entrada, você deve imprimir a matriz correspondente, com os valores formatados de maneira específica.

#O futuro de Matrizópolis está em suas mãos. Use sua lógica, habilidades de programação e criatividade para resolver este enigma e garantir que a cidade continue a brilhar. Abaixo está a descrição da tarefa em detalhes:

#Entrada A entrada consiste de vários inteiros, um valor por linha, correspondendo às ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0). Saída Para cada inteiro da entrada, imprima a matriz correspondente, de acordo com o exemplo. Após a impressão de cada matriz deve ser deixada uma linha em branco.

X = int(input("Valor de X: "))

while True: 
    Z = int(input("Valor de Z: "))
    if Z > X:
        break


soma = 0
quantidade = 0
atual = X

while soma <= Z:
    soma += atual
    atual += 1
    quantidade += 1

print(f"Quantidade de nuemros que devem ser somados: {quantidade}")
