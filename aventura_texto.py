import time

def intro():
    print("Você acorda em uma sala escura e fria. Você não sabe como chegou aqui ou o que está acontecendo.")
    time.sleep(2)
    print("De repente, você ouve uma voz misteriosa...")
    time.sleep(2)
    print("Voz misteriosa: 'Bem-vindo ao meu jogo, jogador. Você tem duas opções: tentar escapar desta sala ou desistir e ficar aqui para sempre.'")
    time.sleep(2)
    print("Voz misteriosa: 'A escolha é sua, mas lembre-se, há consequências para suas escolhas.'")
    time.sleep(2)
    print("Voz misteriosa: 'Boa sorte, jogador.'")
    time.sleep(2)
intro()

def sala_principal():
    print("Você está na sala principal. Há três portas à sua frente.")
    time.sleep(2)
    print("Porta 1: é feita de madeira velha e rangente.")
    time.sleep(2)
    print("Porta 2: é feita de ferro sólido e parece muito pesada.")
    time.sleep(2)
    print("Porta 3: é feita de pedra e parece muito antiga.")
    time.sleep(2)
    escolha = input("Qual porta você escolhe? (1/2/3): ")
    if escolha == "1":
        print("Você escolheu a porta de madeira. Ela se abre com um guincho alto e você entra em uma sala escura.")
        sala_1()
    elif escolha == "2":
        print("Você escolheu a porta de ferro. Ela não se abre. Parece que está trancada.")
        sala_principal()
    elif escolha == "3":
        print("Você escolheu a porta de pedra. Ela se abre com um som pesado e você entra em uma sala empoeirada.")
        sala_2()
    else:
        print("Por favor, escolha uma das opções.")
        sala_principal()

def sala_1():
    print("Você está em uma sala vazia.")
    time.sleep(2)
    escolha = input("O que você faz? (ir para a sala principal/continuar explorando a sala): ")
    if escolha == "ir para a sala principal":
        sala_principal()
    elif escolha == "continuar explorando a sala":
        print("Você encontra uma passagem secreta no fundo da sala e decide segui-la.")
        sala_secreta()
    else:
        print("Por favor, escolha uma das opções.")
        sala_1()

def sala_2():
    print("Você está em uma sala empoeirada. Há uma estante de livros antigos e uma escrivaninha.")
    time.sleep(2)
    escolha = input("O que você faz? (examinar a estante de livros/verificar a escrivaninha): ")
    if escolha == "examinar a estante de livros":
        print("Você examina a estante de livros e encontra um livro antigo com uma chave escondida em suas páginas.")
        time.sleep(2)
        escolha2 = input("O que você faz? (ir para a sala principal/continuar explorando a sala): ")
        if escolha2 == "ir para a sala principal":
            sala_principal()
        elif escolha2 == "continuar explorando a sala":
            print("Você encontra uma porta secreta atrás da estante de livros e decide abri-la.")
            sala_secreta()
        else:
            print("Por favor, escolha uma das opções.")
            sala_2()
    elif escolha == "verificar a escrivaninha":
        print("Você verifica a escrivaninha e encontra um mapa antigo que mostra uma passagem secreta.")
        time.sleep(2)
        escolha3 = input("O que você faz? (ir para a sala principal/continuar explorando a sala): ")
        if escolha3 == "ir para a sala principal":
            sala_principal()
        elif escolha3 == "continuar explorando a sala":
            print("Você encontra a passagem secreta que leva a um túnel subterrâneo.")
            sala_secreta()
        else:
            print("Por favor, escolha uma das opções.")
            sala_2()
    else:
        print("Por favor, escolha uma das opções.")
        sala_2()

def tesouro():
    print("Você entrou na sala do tesouro e encontra um baú de ouro.")
    time.sleep(2)
    escolha = input("O que você faz? (abrir o baú/voltar para a sala secreta): ")
    if escolha == "abrir o baú":
        print("Você abre o baú e encontra uma joia rara.")
        time.sleep(2)
        escolha2 = input("O que você faz? (ir para a sala principal/voltar para a sala secreta): ")
        if escolha2 == "ir para a sala principal":
            sala_principal()
        elif escolha2 == "voltar para a sala secreta":
            sala_secreta()
        else:
            print("Por favor, escolha uma das opções.")
            tesouro()
    elif escolha == "voltar para a sala secreta":
        sala_secreta()
    else:
        print("Por favor, escolha uma das opções.")
        tesouro()

def sala_secreta():
    print("Você está em uma sala secreta. Há uma mesa e um baú no centro da sala.")
    time.sleep(2)
    escolha = input("O que você faz? (examinar a mesa/abrir o baú): ")
    if escolha == "examinar a mesa":
        print("Você examina a mesa e encontra um diário antigo que conta a história da construção do prédio.")
        time.sleep(2)
        escolha2 = input("O que você faz? (ir para a sala principal/continuar explorando a sala secreta): ")
        if escolha2 == "ir para a sala principal":
            sala_principal()
        elif escolha2 == "continuar explorando a sala secreta":
            print("Você encontra uma porta secreta que leva a uma sala de tesouros.")
            tesouro()
        else:
            print("Por favor, escolha uma das opções.")
            sala_secreta()
    elif escolha == "abrir o baú":
        print("Você abre o baú e encontra uma chave dourada.")

sala_principal()
sala_1()
sala_2()
sala_secreta()