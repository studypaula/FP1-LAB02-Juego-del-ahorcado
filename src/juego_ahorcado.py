import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):   
   """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """   
   cadena = cadena.lower().strip()
   cadena = cadena.replace("á", "a").replace("ä", "a")
   cadena = cadena.replace("é", "e").replace("ë", "e")
   cadena = cadena.replace("í", "i").replace("ï", "i")
   cadena = cadena.replace("ó", "o").replace("ö", "o")
   cadena = cadena.replace("ú", "u").replace("ü", "u")
   return cadena
  
def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res= ""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            res += letra
        else:
            res += "_"     
    return res          


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" in palabra_enmascarada:
      return False
    else:
      return True 

    

def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    """Devuelve la palabra enmascarada, las letras usadas hasta entonces y los intentos restantes al jugador.
    Palabra enmascarada: Las letras de la palabra hasta ahora halladas y barras que definen el resto de letras por hallar.
    Letras usadas: Las letras hasta ahora intentadas tanto las acertadas como las no acertadas.
    Intentos restantes: El número de intentos que le quedan al jugador para hallar la palabra secreta."""
    print(f"Estado:{" ".join(palabra_enmascarada)}")
    if len(letras_usadas) == 0:
        print("Letras usadas: ninguna")
    else:         
        print(f"Letras usadas: {letras_usadas}")
    print(f"Intentos restantes:{intentos_restantes}")    

def pedir_letra (letras_usadas):
    letra = input("Introduce una nueva letra")
    while letra in letras_usadas:
        print("Error. Dicha letra ya ha sido usada anteriormente.")
        letra = input("Introduce una nueva letra")
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        print("Error. Introduzca una letra")
        letra = input("Introduce una nueva letra")
    while len(letra) > 1:
        print("Error. Introduzca una única letra.") 
        letra = input("Introduce una nueva letra")
    return letra.lowwer()    

    


def jugar()

# TODO: Escribe el programa principal
