def limitChecker(speed):
    if speed > 120:
        print("Você foi multado em R$200")
    elif speed > 100 and speed <= 120:
        print("Você foi multado em R$100")
    else:
        print("Tudo certo, você pode seguir viagem")
