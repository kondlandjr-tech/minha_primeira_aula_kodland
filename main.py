print("Olá! Esse programa irá ajudar a praticar palavras usadas entre os jovens atualmente!")
print("Não esqueça de digitar as palavras em letra MAIÚSCULA")


meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "PAIA": "Algo chato ou não legal",
            "HATER": "Alguém que odeia (muitas vezes sem motivo) algo ou alguém",
            }
for vezes in range(5):
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras   maiúsculas): ")

    if word in meme_dict.keys():
        # O que devemos fazer se a palavra for encontrada?
        print(meme_dict[word])
    else:
        # O que devemos fazer se a palavra não for encontrada?
        print("Tente escrever novamente essa palavra em letra MAIÚSCULA. Se mesmo assim não der certo, essa palavra não está na lista")
