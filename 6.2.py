def calcula_idade(ano_nascimento):
    idade = 2025 - ano_nascimento
    return idade
def main():
    ano = int(input("qual o ano de nascimento? "))
    idade = calcula_idade(ano)
    print(f"Sua idade em 2025 é: {idade} anos")
if __name__ == '__main__':
    main()
