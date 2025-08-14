class Galleta: #Clase padre para la mayoria de las demas clases
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_info(self): #Metodo para poder visualizar los atributos de la clase
        return f"Nombre: {self.nombre} -- Precio:Q{self.precio} -- Peso:{self.peso} gramos"

class GalletaChispas(Galleta): #Clase de Galleta con Chispas que hereda de la clase Galleta
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        super().__init__(nombre, precio, peso)
        self.cantidad_chispas = cantidad_chispas

    def mostrar_info(self): #Metodo para poder visualizar los atributos de la clase
        info_galleta = super().mostrar_info()
        return f"{info_galleta} -- Chispas: {self.cantidad_chispas}"

class Relleno: #Clase para el relleno que se agrega a la galleta
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno

    def describir_relleno(self): #Metodo para ver la información del relleno
        return f"El relleno de la galleta es la siguiente: {self.sabor_relleno}"

class GalletaRellena(Galleta, Relleno): #Clase de galleta con relleno
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_info(self): #Metodo para poder visualizar la información de las clases
        info_galleta2 = Galleta.mostrar_info(self)
        relleno1 = Relleno.describir_relleno(self)
        return f"{info_galleta2} -- {relleno1}"

class NombresDuplicados(Exception): #Clase para crear la excepción personalizada
    pass

class RegistrarGalleta: #Clase para registrar las galletas con sus funciones
    def __init__(self):
        self.lista_galletas = [] #Lista para guardar las galletas

    def verificar_nombres_duplicados(self, nombre): #Metodo que se une a la excepción personalizada
        for galleta in self.lista_galletas:
            if galleta.nombre.lower() == nombre.lower():
                return True
        return False

    def agregar_galleta_basica(self): #c
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            if self.verificar_nombres_duplicados(nombre):
                raise NombresDuplicados("Ya existe una galleta con este nombre")
            precio = float(input("Ingrese el precio de la galleta: "))
            peso = float(input("Ingrese el peso de la galleta: "))
            if precio < 0 or peso < 0:
                raise ValueError("No se admiten números negativos, vuelva a intentar")
            else:
                self.lista_galletas.append(Galleta(nombre, precio, peso))
                print("Se ha registrado la galleta")
        except ValueError:
            print("No se admiten números negativos, vuelva a intentar")
        except NombresDuplicados as e:
            print(f"{e}")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    def agregar_galleta_chispas(self): #Metodo para agregar la información de la galleta con chispas
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            if self.verificar_nombres_duplicados(nombre):
                raise NombresDuplicados("Ya existe una galleta con este nombre")
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
        except NombresDuplicados as e:
            print(e)
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    def agregar_galleta_relleno(self): #Metodo para agregar la información de la galleta con relleno
        try:
            nombre = input("Ingrese el nombre de la galleta: ")
            if self.verificar_nombres_duplicados(nombre):
                raise NombresDuplicados("Ya existe un nombre duplicado")
            precio = float(input("Ingrese el precio de la galleta: "))
            peso = float(input("Ingrese el peso de la galleta: "))
            sabor_relleno = input("Ingrese una breve descripción del relleno: ")
            if precio < 0 or peso < 0:
                raise ValueError("No se admiten números negativos, vuelva a intentar")
            else:
                self.lista_galletas.append(GalletaRellena(nombre, precio, peso, sabor_relleno))
                print("Se ha agregado la galleta")
        except ValueError:
            print("No se admiten números negativos, vuelva a intentar")
        except NombresDuplicados as e:
            print(e)
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    def ver_galletas(self): #Metodo para poder ver todas las galletas agregadas
        if not self.lista_galletas:
            print("No hay galletas registradas")
        else:
            for i, galletas in enumerate(self.lista_galletas, start=1):
                print(f"{i} -- {galletas.mostrar_info()}")

    def buscar_galleta(self): #Metodo para buscar alguna galleta en la lista
        nombre_galleta = input("Ingrese el nombre dee la galleta a buscar: ")
        for galleta in self.lista_galletas:
            if galleta.nombre.lower() == nombre_galleta.lower():
                print(f"Se ha encontrado la galleta {nombre_galleta}")
                return
        print("Galleta no encontrada")

    def eliminar_galleta(self): #Metodo para poder eliminar una galleta de la lista
        nombre_galleta = input("Ingrese el nombre de la galleta a eliminar: ")
        for galleta in self.lista_galletas:
            if galleta.nombre.lower() == nombre_galleta.lower():
                self.lista_galletas.remove(galleta)
                print("Se ha eliminado la galleta del registro")
                return
        print("Galleta no encontrada")

galletas = RegistrarGalleta() #Variable para poder acceder a la clase con sus metodos

while True: #Bucle para que se mantenga el menu hasta que el usuario quiera parar el programa
    print("---- Menú ----")
    print("1.- Registrar galleta básica")
    print("2.- Registrar galleta con chispas")
    print("3.- Registrar galleta rellena")
    print("4.- Lista de galletas")
    print("5.- Buscar galleta por su nombre")
    print("6.- Eliminar galleta")
    print("7.- Salir")
    menu_option = input("Ingrese el número de la opción que quiera realizar: ") #Variable para guardar el numero de opción del menu
    print()
    match menu_option: #Match para verificar la variable del menu
        case "1":
            print("Registrar galleta básica")
            galletas.agregar_galleta_basica()
            print()
        case "2":
            print("Registrar galleta con chispas")
            galletas.agregar_galleta_chispas()
            print()
        case "3":
            print("Rregistrar galleta rellena")
            galletas.agregar_galleta_relleno()
            print()
        case "4":
            print("Lista de galletas")
            galletas.ver_galletas()
            print()
        case "5":
            print("Buscar galleta por su nombre")
            galletas.buscar_galleta()
            print()
        case "6":
            print("Eliminar galleta")
            galletas.eliminar_galleta()
            print()
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
            print()