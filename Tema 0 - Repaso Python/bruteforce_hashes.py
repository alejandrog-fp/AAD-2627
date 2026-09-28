import base64
import hashlib


def generar_sha1_b64(texto: str) -> str:
    # 1. Convertir el texto a bytes (UTF-8)
    datos_bytes = texto.encode("ascii")

    # 2. Calcular el hash SHA-1
    hash_sha1 = hashlib.sha1(datos_bytes).digest()

    # 3. Codificar los bytes del hash a Base64 y decodificar a string
    return base64.b64encode(hash_sha1).decode("ascii")

def romper_hash(hash):
    for i in range(10**4):
        n = str(i).zfill(4)
        if generar_sha1_b64(n) == hash:
            return n

def main():
    with open("hashes.txt", "r") as fichero:
        hashes = fichero.readlines()

    for hash in hashes:
        hash_limpio = hash.strip()
        contrasena = romper_hash(hash_limpio)
        print(f'La contraseña asociada al hash {hash_limpio} es {contrasena}')


if __name__ == "__main__":
    main()
