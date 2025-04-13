def is_palindrome(texto):
    texto = texto.lower() #convierte a minúscula
    texto = texto.replace(" ", "") #quita espacios
    return texto == texto[::-1] #da vuelta la palabra
if __name__ == "__main__":
    texto = input("Escriba una palabra o frase: ")
    if is_palindrome(texto):
        print(f'"{texto}" es un palíndromo')
    else:
        print(f'"{texto}" no es un palíndromo')






