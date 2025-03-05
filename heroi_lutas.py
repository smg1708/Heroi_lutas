heroi = input("Qual o nome do heroi? ")
print(f"classes disponiveis: MAGO, GUERREIRO, MONGE e NINJA")
while True:

    classe = input("Qual a classe do heroi? ")
    if classe == "MAGO" or "mago" or "Mago":
        print(f"Classe mago escolhida com sucesso")
        break
    if classe == "GUERREIRO" or "guerreiro" or "Guerreiro" :
        print(f"Classe guerreiro escolhida com sucesso")
        break
    if classe == "MONGE" or "monge" or "Monge":
        print(f"Classe monge escolhida com sucesso")
        break
    if classe == "NINJA" or "ninja" or "Ninja":
        print(f"Classe ninja escolhida com sucesso")
        break
    else:
        print(f"classe não liberada ou incorreta")

print("Carregando...")
ataque_mago = "magia"
ataque_guerreiro = "espada"
ataque_monge = "artes marciais"
ataque_ninja = "shuriken"
print(f"O {heroi} entrou em combate com um inimigo")
while True:
    if classe == "MAGO" or "mago" or "Mago":
        print(f"Você é um {classe} e atacou com seu {ataque_mago}")
        break
    if classe == "GUERREIRO" or "guerreiro" or "Guerreiro":
        print(f"Você é um {classe} e atacou com seu {ataque_guerreiro}")
        break
    if classe == "MONGE" or "monge" or "Monge":
        print(f"Você é um {classe} e atacou com seu {ataque_monge}")
        break
    if classe == "NINJA" or "ninja" or "Ninja":
        print(f"Você é um {classe} e atacou com seu {ataque_ninja}")
        break