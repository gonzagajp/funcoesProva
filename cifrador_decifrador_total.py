# Definindo o alfabeto na ordem exata do disco
ALFABETO = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def processar_cifra(mensagem, chaves, modo):
    resultado = []
    indice_chave = 0

    for char in mensagem:
        # Ignora espaços completamente, não adicionando ao resultado
        # e não avançando o índice da chave
        if char == ' ':
            continue

        char_upper = char.upper()

        # Verifica se o caractere pertence ao disco
        if char_upper in ALFABETO:
            posicao_atual = ALFABETO.index(char_upper)
            # Pega a chave correspondente à posição atual (ciclamente)
            chave_atual = chaves[indice_chave % len(chaves)]

            # Se for descriptografar, inverte a direção da chave no disco
            if modo == 'descriptografar':
                chave_atual = -chave_atual

            # Aplica a regra matemática com módulo 27
            nova_posicao = (posicao_atual + chave_atual) % len(ALFABETO)
            novo_char = ALFABETO[nova_posicao]

            # Mantém a formatação de minúscula se a original for (opcional para estética)
            if char.islower() and novo_char.isalpha():
                resultado.append(novo_char.lower())
            else:
                resultado.append(novo_char)

            # Avança o índice da chave apenas ao processar caracteres válidos
            indice_chave += 1
        else:
            # Mantém pontuações que não estejam no disco
            resultado.append(char)

    return "".join(resultado)


print("O que você deseja fazer?")
print("1 - Criptografar")
print("2 - Descriptografar")

while True:
    opcao_modo = input("Escolha uma opção (1 ou 2): ")
    if opcao_modo == '1':
        modo = 'criptografar'
        mensagem_inserida = input("\nDigite a mensagem para criptografar: ")
        break
    elif opcao_modo == '2':
        modo = 'descriptografar'
        mensagem_inserida = input("\nDigite a mensagem criptografada: ")
        break
    else:
        print("Opção inválida. Escolha 1 ou 2.")

print("\nQuantas chaves tem a cifra?")
print("1 - Uma chave")
print("2 - Duas chaves")
print("3 - Três chaves")
print("4 - Quatro chaves")

# Recebe a quantidade de chaves
while True:
    try:
        quantidade_chaves = int(input("Escolha uma opção (1-4): "))
        if 1 <= quantidade_chaves <= 4:
            break
        else:
            print("Por favor, escolha um número entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

chaves = []

# Coleta os valores exatos de cada chave
for i in range(quantidade_chaves):
    while True:
        try:
            chave = int(
                input(f"Informe o valor da regra/chave {i+1} (ex: 3 ou -2): "))
            chaves.append(chave)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Executa o processamento com base no modo escolhido
mensagem_final = processar_cifra(mensagem_inserida, chaves, modo)

print(f"\nMensagem inserida: {mensagem_inserida}")
print(f"Resultado ({modo}): {mensagem_final}")
