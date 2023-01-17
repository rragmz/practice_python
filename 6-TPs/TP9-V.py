"""Un palíndromo (del griego palin dromein, volver a ir atrás)
Es una palabra, número o frase que se lee igual adelante que atrás.
Si se trata de un numeral, usualmente en notación indoarábiga, se llama capicúa.
debemos poder identificar las frases numeros o palabras que son palindromos
1°: De la cadena original , buscamos los espacios y los eliminamos.
2°: La palabra original ,le invertimos el orden de las letras
3°: Comparamos las dos cadenas y si son iguales , es un palindromo."""

def get_phrase():
    phrase = input('Ingrese una frase: ')
    return phrase

def remove_spaces(phrase):
    phrase_without_spaces = []
    for x in phrase:
        if x != ' ':
            phrase_without_spaces.append(x)
    phrase_without_spaces = "".join(phrase_without_spaces)
    return(phrase_without_spaces)

def turn_phrase(phrase):
    turned_phrase = "".join(reversed(phrase))
    return(turned_phrase)

def str_equals(str1, str2):
    if str1 == str2:
        return 1
    else:
        return 0

def system():
    phrase = get_phrase()
    phrase = remove_spaces(phrase)
    turned_phrase = turn_phrase(phrase)
    isPalindrome = str_equals(phrase, turned_phrase)
    if isPalindrome:
        print('La frase es palíndromo')
    else:
        print('La frase no es palíndromos')

system()
