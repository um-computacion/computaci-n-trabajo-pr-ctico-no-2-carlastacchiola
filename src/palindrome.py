import re
def limpiar_texto(texto):
    texto = texto.lower() #convierte a minúscula
    texto = texto.replace(" ", "") #quita espacios
    texto = re.sub(r'[^a-z0-9]','', texto) #quita caracteres no alfabeto
    return texto 

def is_palindrome(texto):
    texto_limpio = limpiar_texto(texto)
    # por ahora no comparamos aún
    return texto_limpio

