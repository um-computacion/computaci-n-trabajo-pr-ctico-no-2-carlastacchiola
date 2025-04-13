import re
def limpiar_texto(texto):
    texto = texto.lower() #convierte a minúscula
    texto = texto.replace(" ", "") #quita espacios
    texto = re.sub(r'[^a-z0-9]','', texto) #quita caracteres no alfabeto
    return texto == texto[::-1] #compara con el mismo al revés

def is_palindrome(texto):
    texto_limpio = limpiar_texto(texto)
    return texto_limpio


if __name__ == "__main__":
    texto = input("Escriba una palabra o frase: ")
    if is_palindrome(texto):
        print(f'"{texto}" es un palíndromo')
    else:
        print(f'"{texto}" no es un palíndromo')
