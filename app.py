from bayeta import frotar

# Probamos la función pidiendo, por ejemplo, 3 frases
frases_de_prueba = frotar(3)

print("--- Probando la Bayeta de la Fortuna ---")
for i, frase in enumerate(frases_de_prueba, 1):
    print(f"{i}. {frase}")