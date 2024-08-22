#Com os conhecimentos que está adquirindo no pensamento computacional e na programação, você resolveu começar a desenvolver um aplicativo financeiro para ajudar a monitorar e analisar seus gastos diários e aproveitar melhor o seu escasso recurso monetário. Para facilitar o uso, o aplicativo deve permitir que você insira diversos valores de despesas ao longo do dia e, ao final, identificar a despesa única mais alta. Isso é especialmente útil para você rapidamente saber qual foi seu maior gasto do dia, permitindo-lhe ajustar seu orçamento de forma mais eficaz.

#Sendo assim, desenvolva um algoritmo que solicite uma série de valores, representando quantias gastas em diferentes itens ou serviços ao longo do dia. O programa deve continuar recebendo os valores até que você digite o número 0 (zero), que serve como sinal para terminar a entrada de dados. Após a conclusão da entrada, o programa deve analisar os números fornecidos e exibir o maior valor, representando a maior despesa do dia.

#Lembre-se: O programa deve aceitar uma quantidade indefinida de entradas de números até que o usuário digite 0, que indica o fim da entrada. O algoritmo deve identificar e exibir o maior número entre as entradas fornecidas, excluindo o zero final que é usado para terminar a entrada. O programa deve ser capaz de lidar com uma variedade de entradas, incluindo a possibilidade de todos os números serem negativos ou o usuário inserir apenas o zero.

gastos = []

while True:
    gasto = float(input("Informe os gastos do dia:"))
    if gasto == 0:
        break
    gastos.append(gasto)

if gastos:
    maior_gasto = max(gastos)
    print(f"O seu maior gasto hoje foi de R$ {maior_gasto:.2f}")

else:
    print("Você não teve gastos hoje!")