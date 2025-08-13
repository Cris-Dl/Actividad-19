class Galleta:
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_info(self):
        print("Información de las galletas")
        print(f"Nombre: {self.nombre} -- Precio:Q{self.precio} -- Peso:{self.peso}")

class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        super().__init__(nombre, precio, peso)
        self.cantidad_chispas = cantidad_chispas

    def mostrar_info(self):
        info_galleta = super().mostrar_info()
        print(f"{info_galleta} -- Chispas: {self.cantidad_chispas}")

class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno

    def describir_relleno(self):
        print(f"El relleno de la galleta es la siguiente: {self.sabor_relleno}")

class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_info(self):
        info_galleta2 = Galleta.mostrar_info(self)
        relleno1 = Relleno.describir_relleno(self)
        print(f"{info_galleta2} -- {relleno1}")

class RegistrarGalleta:
    def __init__(self):
        self.lista_galletas = []

    def agregar_galleta_basica(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            precio = float(input("Ingrese el precio de la galleta: "))
            peso = float(input("Ingrese el peso de la galleta: "))
            if precio < 0 or peso < 0:
                raise ValueError("No se admiten números negativos, vuelva a intentar")
            else:
                self.lista_galletas.append(Galleta(nombre, precio, peso))
                print("Se ha registrado la galleta")
        except ValueError:
            print("No se admiten números negativos, vuelva a intentar")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    def agregar_galleta_chispas(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            precio = float(input("Ingrese el precio de la galleta: "))
            peso = float(input("Ingrese el peso de la galleta: "))
            cantidad_chispas = int(input("Ingrese la cantidad de chispas para la galleta: "))
            if cantidad_chispas < 0 or precio < 0 or peso < 0:
                raise ValueError("No se admiten números negativos, vuelva a intentar")
            else:
                self.lista_galletas.append(GalletaChispas(nombre, precio, peso, cantidad_chispas))
                print("Se ha agregado la galleta")
        except ValueError:
            print("No se admiten números negativos, vuelva a intentar")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")


class MostrarGalletas:
    def __init__(self, lista_galletas):
        self.lista_galletas = lista_galletas

    def mostrar_lista(self):
        print("Lista de galletas")
        for galleta in self.lista_galletas:
            galleta.mostrar_info()

galletas= RegistrarGalleta()

while True:
    print("---- Menú ----")
    print("1.- Registrar galleta básica")
    print("2.- Registrar galleta con chispas")
    print("3.- Registrar galleta rellena")
    print("4.- Lista de galletas")
    print("5.- Buscar galleta por su nombre")
    print("6.- Eliminar galleta")
    print("7.- Salir")
    menu_option = input("Ingrese el número de la opción que quiera realizar: ")
    print()
    match menu_option:
        case "1":
            print("Registrar galleta básica")
            galletas.agregar_galleta_basica()
        case "2":
            print("Registrar galleta con chispas")
            galletas.agregar_galleta_chispas()
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