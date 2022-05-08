# Este módulo implementa una interfaz común para muchos algoritmos seguros de resumen de mensajes y hash. 
# Se incluyen los algoritmos hash seguros de FIPS SHA1, SHA224, SHA256, SHA384 y SHA512 (definidos en FIPS 180-2), 
# así como el algoritmo MD5 de RSA (definido en Internet RFC 1321). 
import hashlib

# Inicializamos la string
print("Introduzca un texto o numero a encriptar =D")
str2hash = input()
# La función hash md5 lo codifica y luego, usando digest(), se imprime la cadena codificada equivalente en bytes.
result = hashlib.md5(str2hash.encode())

# Imprimimos el equivalente en hexadecimal
print("El equivalente hexadecimal de este hash es: ", end ="")
print(result.hexdigest())
