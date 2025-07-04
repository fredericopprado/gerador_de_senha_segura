import random

minusculas = list("abcdefghijklmnopqrstuvwxyz")
maiusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digitos = list("0123456789")
simbolos = list("!@#$%&*()-_+=[]{}/\\|<>,.?~^")
unica_lista = minusculas + maiusculas + digitos + simbolos

def gerar_senha(tamanho):
    senha = []
    for _ in range(tamanho):
        caracter = random.choice(unica_lista)
        senha.append(caracter)
    senha_str = "".join(senha)
    return senha_str

def senha_valida(senha):
    tem_minuscula = any(c.islower() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_digito = any(c.isdigit() for c in senha)
    tem_simbolo = any(c in simbolos for c in senha)
    return tem_minuscula and tem_maiuscula and tem_digito and tem_simbolo

def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    while True:
        try:
            tamanho = int(input("Quantos caracteres na senha? (mínimo 6) "))
            if tamanho < 6:
                print("Digite um número maior ou igual a 6.")
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        while True:
            senha = gerar_senha(tamanho)
            if senha_valida(senha):
                print("Senha gerada:", senha)
                break

        resposta = input("Quer gerar outra senha? (s/n): ").lower()
        if resposta == 'n':
            print("Obrigado por usar o gerador de senhas!")
            break

if __name__ == "__main__":
    main()
