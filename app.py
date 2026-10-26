import json
import random
import time
import itertools
import sys
import threading

print("-"*20)
print("       \33[36mTTT\33[0m")
print("-"*20)
print("Joque Termo no terminal")
while True:
    escolha = input("Iniciar?[S/N]: ").upper()
    if escolha == "S":
        with open('TTT/palavras.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
        embaralha = random.choice(dados)
        for quadro in itertools.cycle(["", ".", "..", "..."]):
            print(f"\rCriando{quadro}   ", end="", flush=True)
            time.sleep(0.5)
            if quadro == "...":
                break
        print("\rFrase criada")
        time.sleep(0.2)
        print("Que começe o Jogo!")
        print("Você tem 10 Tentativas")
        time.sleep(0.1)
        secreto = embaralha
        for tentativa in range(10):
            print(f"Tentativa: {tentativa + 1}/10")
            chute = input("Letra: ").upper()
            result = ""
            if chute == "EXIT":
                print("Obrigado por usar o programa")
                break
            if len(chute) == 5:
                if chute == secreto:
                    print(chute)
                    print("🟩🟩🟩🟩🟩")
                    print("Acertou!")
                    break
                else:
                    for posicao in range(5):
                        if chute[posicao] == secreto[posicao]:
                            result += "🟩"
                        elif chute[posicao] in secreto:
                            result += "🟨"
                        else:
                            result += "🟥"
                    print(result)
            else:
                print("A palavra deve ter 5 letras")
        else:
            print(f"Suas tentativas acabaram! A palavra era {secreto}.")
    elif escolha == "N":
        print("Fique a vontade quando quiser jogar")
        break
    else:
        print("Escolha s ou n")
