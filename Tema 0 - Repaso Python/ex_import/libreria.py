def f():
    print("Esto es la función f")

def suma(x, y):
    return x + y
print(f'Libreria: {__name__=}')

if __name__ == "__main__":
    print('Inicio de testeos de la librería')
    assert suma(1, 2) == 3