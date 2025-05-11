def calcula_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def main():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = calcula_area_triangulo(base, altura)
    print(f"A área do triângulo é: {area:.2f}")

if __name__ == '__main__':
    main()
