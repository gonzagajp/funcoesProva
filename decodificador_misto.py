# Definindo o alfabeto na ordem exata do disco da imagem
ALFABETO = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def processar_cifra(mensagem, chaves, modo):
    resultado = []
    indice_chave = 0

    for char in mensagem:
        if char == ' ':
            continue

        char_upper = char.upper()

        if char_upper in ALFABETO:
            posicao_atual = ALFABETO.index(char_upper)
            chave_atual = chaves[indice_chave % len(chaves)]

            # Se for descriptografar, inverte a direção da chave no disco
            if modo == 'descriptografar':
                chave_atual = -chave_atual

            nova_posicao = (posicao_atual + chave_atual) % len(ALFABETO)
            novo_char = ALFABETO[nova_posicao]

            if char.islower() and novo_char.isalpha():
                resultado.append(novo_char.lower())
            else:
                resultado.append(novo_char)

            indice_chave += 1
        else:
            resultado.append(char)

    return "".join(resultado)


mensagem_inserida = input("Digite a mensagem criptografada: ")

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

mensagem_decifrada = decifrar_multiplas_chaves(mensagem_inserida, chaves)

print(f"\nMensagem inserida: {mensagem_inserida}")
print(f"Mensagem decifrada: {mensagem_decifrada}")
