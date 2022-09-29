import numpy as np
import os

def bus():
    assentos = np.arange(40).reshape(8, 5)
    assentos[0] = 0
    assentos[1:8, 2] = 0
    assentos[0][0] = 9
    assentos[1:8, 0] = 1
    assentos[1:8, 1] = 2
    assentos[1:8, 3] = 1
    assentos[1:8, 4] = 2

    return assentos

def mostrar(assentos):
    print(assentos)

def cord(assentos):
    mostrar(assentos)
    print("""\033[91mObservações sobre os assentos:\033[0m
    \033[94m[9]\033[0m \033[96mMOTORISTA\033[0m
    \033[94m[0]\033[0m \033[96mCORREDOR\033[0m
    \033[94m[1]\033[0m \033[96mASSENTO DISPONIVEL NA JANELA\033[0m
    \033[94m[2]\033[0m \033[96mASSENTO DISPONIVEL NO CORREDOR\033[0m
    \033[94m[6]\033[0m \033[96mASSENTO RESERVADO\033[0m
    """)
    coluna = int(input('\033[93mESCOLHA A COLUNA DESEJADA:\033[0m '))
    c= coluna - 1
    if c == 2:
       print('\033[91mESTE LUGAR NÃO PODE\033[0m')
       cord(assentos)
    elif c <= 5 and c > -1:
        pass
    else:
        os.system('cls')
        print('\033[91mNÃO TEM ESSA OPÇÃO!\033[0m')
        cord(assentos)

    linha = int(input('\033[93mEESCOLHA A LINHA DESEJADA:\033[0m '))
    l= linha - 1
    if l == 0:
        os.system('cls')
        print('\033[91mAQUI NAO PODE\033[0m')
        cord(assentos)
    elif l <= 8 and l > -1:

        if assentos[l][c] == 6:
            os.system('cls')
            print('\033[91mASSENTO NAO DISPONIVEL\033[0m')
            cord(assentos)
        else:
            print('\033[92mPARABENS!! A sua compra foi efetuada\033[0m')
            assentos[l][c] = 6
            mostrar(assentos)
            c_comprando()
    else:
        print('\033[91mESTE LUGAR NÃO PODE\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')
        cord(assentos)

def c_comprando():
    sim = int(input("""
    \033[93mVoce deseja continuar a sua compra?\033[0m 
    \033[94m[1]\033[0m \033[96mSIM\033[0m
    \033[94m[2]\033[0m \033[96mNAO\033[0m
    \033[94m[3]\033[0m \033[96mMENU\033[0m        
    \033[93mQual serviço você deseja acessar?\033[0m """))
    try:
        if sim == 1:
            os.system('cls')
            cord(assentos)

        elif sim == 2:
                os.system('cls')
                print('Obrigado pelo acesso!')
                relatorio = str(assentos)
                with open("relatorio.txt", "w") as arquivo:
                    arquivo.write(relatorio)
                    arquivo.write("""\nObservações sobre os assentos:
                        \n[9] MOTORISTA\n[0] CORREDOR\n[1] ASSENTO DISPONIVEL NA JANELA\n[2] ASSENTO DISPONIVEL NO CORREDOR\n[6] ASSENTO RESERVADO
                        """)
                exit()
        elif sim == 3:
            os.system('cls')
            menu(assentos)
        else:
            os.system('cls')
            print('\033[91m        Tente novamente\033[0m')
            cord(assentos)

    except ValueError:
        print('\033[91mSelecione uma opção válida\033[0m')
        c_comprando()

def menu(assentos):

    while True:

        print("""
        \033[93mOlá, qual serviço deseja acessar da POCCOBUS?\033[0m
        \033[94m[1]\033[0m \033[96mCOMPRAR PASSAGEM\033[0m
        \033[94m[2]\033[0m \033[96mVER DISPONIBILIDADE\033[0m
        \033[94m[3]\033[0m \033[96mFECHAR APLICATIVO\033[0m""")

        try:

            opcao = int(input('        \033[93mQual serviço você deseja acessar?\033[0m '))

            if opcao == 1:
                cord(assentos)

            elif opcao == 2:
                os.system('cls')
                mostrar(assentos)
                print('\033[91mEsses são os lugares disponiveis!\033[0m')
                vou = int(input("""
                \033[93mDeseja comprar uma passagem?\033[0m
                \033[94m[1]\033[0m SIM
                \033[94m[2]\033[0m NAO, VOLTAR PARA O MENU
                \033[93mSelecione uma opção:\033[0m """))
                if vou == 1:
                    cord(assentos)
                elif vou == 2:
                    continue
                else:
                    continue

            elif opcao == 3:
                os.system('cls')
                print('Obrigado pelo acesso!')
                relatorio = str(assentos)
                with open("relatorio.txt", "w") as arquivo:
                    arquivo.write(relatorio)
                    arquivo.write("""\nObservações sobre os assentos:
                        \n[9] MOTORISTA\n[0] CORREDOR\n[1] ASSENTO DISPONIVEL NA JANELA\n[2] ASSENTO DISPONIVEL NO CORREDOR\n[6] ASSENTO RESERVADO
                        """)
                exit()

            else:
               print('\033[91m        Tente novamente\033[0m')
        except ValueError:
            print('\033[91m        Tente novamente\033[0m')

if __name__ == "__main__":
    assentos = bus()
menu(assentos)