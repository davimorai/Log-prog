def soma_valor(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma

def main():
    v1 = int(input("qual o primeiro valor? "))
    v2 = int(input("qual o segundo valor? "))
    v3 = int(input("qual o terceiro valor? "))
    resultado = soma_valor(v1, v2, v3)
    print(f"a soma dos valores é: {resultado}")

if __name__ == '__main__':
    main()
