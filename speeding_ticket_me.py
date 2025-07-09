def limitChecker(speed):
    if speed > 120:
        print("Você foi multado em R$200")
    elif speed > 100 and speed <= 120:
        print("Você foi multado em R$100")
    else:
        print("Tudo certo, pode seguir viagem")

def main():
    from test_data import LIMIT_CASES
    for speed in LIMIT_CASES[0]:
        print(f"Verificando velocidade: {speed} km/h")
        limitChecker(speed)

main()