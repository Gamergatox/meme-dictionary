meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("El significado de", word, "es", meme_dict[word])
        # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("No se encuentra esa palabra en el diccionario")
        # ¿Qué hacer si no se encuentra la palabra?
