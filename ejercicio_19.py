class Galleta:
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_info(self):
        print("Información de las galletas")
        print(f"Nombre: {self.nombre} -- Precio:Q{self.precio} -- Peso:{self.peso}")

class RegistrarGalleta:
    def __init__(self):
        self.lista_galletas = []

    def agregar_galleta(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            precio = float(input("Ingrese el precio de la galleta: "))
            peso = float(input("Ingrese el peso de la galleta: "))
            if precio < 0 and peso < 0:
                ValueError("No se admiten números negativos, vuelva a intentar")
            else:
                self.lista_galletas.append(Galleta(nombre, precio, peso))
                print("Se ha registrado la galleta")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")


while True:
    print("---- Menú ----")
    print("1.- Registrar galleta básica")
    print("2.- Registrar galleta con chispas")
    print("3.- Registrar galleta rellena")
    print("4.- Lista de galletas")
    print("5.- Buscar galleta por su nombre")
    print("6.- Eliminar galleta")
    print("7.- Salir")
    menu_option = input("Ingrese el número de la opción que quiera realizar")
    print()
    match menu_option:
        case "1":
            print("Registrar galleta básica")
        case "2":
            print("Registrar galleta con chispas")
        case "3":
            print("Rregistrar galleta rellena")
        case "4":
            print("Lista de galletas")
        case "5":
            print("Buscar galleta por su nombre")
        case "6":
            print("Eliminar galleta")
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")