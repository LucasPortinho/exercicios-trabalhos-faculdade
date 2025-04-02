while True:
    # Estou considerando que o algoritmo irá receber apenas números inteiros, para evitar complexidade com try/except
    valor_centavos = int(input('Insira o valor em centavos (valores nulos ou negativos fecharão o programa): ').strip())

    if valor_centavos <= 0:
        print('Valores inválidos!')
        break
    

    moedas = [100, 50, 25, 10, 5, 1]

    resposta = 'Você precisa de:\n'

    for moeda in moedas:
        if valor_centavos == 0:
            print(resposta)
            break

        if valor_centavos >= moeda:

            quantidade_moeda = valor_centavos // moeda
            valor_centavos -=  (moeda * quantidade_moeda)
            resposta += f' {quantidade_moeda} {"moeda" if quantidade_moeda == 1 else "moedas"} de {moeda if moeda < 100 else 1} {"centavos" if moeda < 100 else "real"}\n'

