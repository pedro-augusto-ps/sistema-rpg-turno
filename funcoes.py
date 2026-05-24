import random
def menu():
    print("---Bem vindo ao RPG---")
    print("Você possui 30 de HP e 3 poções e o monstro 40 de HP")
    print("Cada jogada custa 1 turno")

def atacar():
    ataque=random.randint(0, 10)
    if ataque > 7:
        print(f"Ataque crítico, causou: {ataque} de dano\n")
    elif ataque > 5:
        print(f"Ataque forte, causou: {ataque} de dano\n")
    else:
        print(f"Ataque causou: {ataque} de dano\n")
    return ataque
def monstro():

    monstro_ataque=random.randint(0,7)
    if monstro_ataque > 6:
        print(f"Ataque crítico, monstro causou: {monstro_ataque} de dano\n")
    else:
        print(f"Ataque do monstro causou: {monstro_ataque} de dano\n")
    return monstro_ataque


def pocao():
    cura_pocao = random.randint(1,10)
    print(f"Voce curou {cura_pocao} de HP\n")
    return cura_pocao



