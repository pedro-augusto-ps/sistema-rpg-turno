import funcoes

vida_jogador=30
vida_monstro=40
qtd_pocao=3

funcoes.menu()

while True:
    print(f"---Jogador HP: {vida_jogador}---")
    print(f"---Monstro HP: {vida_monstro}---\n") 
    print("---[1] ATACAR ---")
    print("---[2] POÇÃO ---")        

    jogada_escolhida=int(input("Insira sua jogada: "))
    print("\n")

    if jogada_escolhida==1:
        print("---ATAQUE---")
        dano = funcoes.atacar()
        vida_monstro = vida_monstro - dano
 
    elif jogada_escolhida==2:
        print("---POÇÃO---")
        if qtd_pocao==0:
            print("--- Sem poções---")
            print("--- Escolha outra jogada ---")
            continue
        cura = funcoes.pocao()
        qtd_pocao -= 1
        vida_jogador = vida_jogador + cura
    else:
        print("Jogada Inválida")
        continue
    
    print("---Turno do MONSTRO---")
    monstro_dano = funcoes.monstro()
    vida_jogador = vida_jogador - monstro_dano
    
    if vida_jogador<=0:
        print("--- O Jogo acabou, jogador morreu---")
        break
    elif vida_monstro<=0:
        print("---O Jogo acabou, Jogador VENCEU!---")
        break
    else:
        continue

