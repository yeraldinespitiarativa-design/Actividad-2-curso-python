class Producto:
    """
    Clase que representa un producto en el inventario.
    Atributos: nombre (str), precio (float), cantidad (int)
    """
    
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.
        Valida que el nombre no esté vacío, precio >= 0 y cantidad >= 0.
        """
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
            
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto validando que sea >= 0.
        """
        try:
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            self.precio = nuevo_precio
            print(f"Precio actualizado a ${self.precio:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError:
            print("Error: El precio debe ser un número.")
    
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto validando que sea >= 0.
        """
        try:
            nueva_cantidad = int(nueva_cantidad)
            if nueva_cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            self.cantidad = nueva_cantidad
            print(f"Cantidad actualizada a {self.cantidad} unidades.")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError:
            print("Error: La cantidad debe ser un número entero.")
    
    def calcular_valor_total(self):
        """
        Calcula y retorna el valor total del producto (precio × cantidad).
        """
        return self.precio * self.cantidad
    
    def __str__(self):
        """
        Retorna una representación legible del producto.
        """
        valor_total = self.calcular_valor_total()
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor Total: ${valor_total:.2f}"


class Inventario:
    """
    Clase que gestiona una colección de productos.
    """
    
    def __init__(self):
        """
        Constructor que inicializa una lista vacía de productos.
        """
        self.productos = []
    
    def agregar_producto(self, producto):
        """
        Añade un objeto Producto a la lista de productos.
        Valida que sea una instancia de la clase Producto.
        """
        try:
            if not isinstance(producto, Producto):
                raise TypeError("El objeto debe ser una instancia de la clase Producto.")
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado exitosamente.")
        except TypeError as e:
            print(f"Error: {e}")
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre (búsqueda exacta, insensible a mayúsculas/minúsculas).
        Retorna el producto si lo encuentra, o None si no existe.
        """
        try:
            nombre_busqueda = nombre.strip().lower()
            for producto in self.productos:
                if producto.nombre.lower() == nombre_busqueda:
                    return producto
            return None
        except AttributeError:
            print("Error: El nombre debe ser una cadena de texto.")
            return None
    
    def calcular_valor_inventario(self):
        """
        Calcula y retorna el valor total de todos los productos en el inventario.
        """
        valor_total = 0
        for producto in self.productos:
            valor_total += producto.calcular_valor_total()
        return valor_total
    
    def listar_productos(self):
        """
        Muestra todos los productos del inventario de forma formateada.
        """
        if not self.productos:
            print("\nEl inventario está vacío.")
            return
        
        print("\n" + "="*80)
        print("INVENTARIO ACTUAL")
        print("="*80)
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")
        print("="*80 + "\n")


def menu_principal(inventario):
    """
    Muestra un menú interactivo al usuario y procesa sus opciones.
    Permite agregar productos, buscar, listar y calcular valor total del inventario.
    """
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE INVENTARIO")
        print("="*50)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            agregar_producto_menu(inventario)
        elif opcion == '2':
            buscar_producto_menu(inventario)
        elif opcion == '3':
            inventario.listar_productos()
        elif opcion == '4':
            calcular_valor_total_menu(inventario)
        elif opcion == '5':
            print("\n¡Gracias por usar el Sistema de Inventario! Hasta luego.")
            break
        else:
            print("Error: Opción no válida. Por favor, selecciona una opción entre 1 y 5.")


def agregar_producto_menu(inventario):
    """
    Función auxiliar para agregar un producto desde el menú.
    Solicita al usuario los datos del producto y lo agrega al inventario.
    """
    try:
        print("\n--- Agregar Nuevo Producto ---")
        nombre = input("Nombre del producto: ").strip()
        
        if not nombre:
            print("Error: El nombre del producto no puede estar vacío.")
            return
        
        precio_str = input("Precio del producto: $")
        cantidad_str = input("Cantidad disponible: ")
        
        try:
            precio = float(precio_str)
            cantidad = int(cantidad_str)
        except ValueError:
            print("Error: El precio debe ser un número decimal y la cantidad debe ser un número entero.")
            return
        
        producto = Producto(nombre, precio, cantidad)
        inventario.agregar_producto(producto)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def buscar_producto_menu(inventario):
    """
    Función auxiliar para buscar un producto desde el menú.
    Solicita al usuario el nombre del producto y muestra sus detalles si existe.
    """
    try:
        print("\n--- Buscar Producto ---")
        nombre = input("Nombre del producto a buscar: ").strip()
        
        if not nombre:
            print("Error: El nombre del producto no puede estar vacío.")
            return
        
        producto = inventario.buscar_producto(nombre)
        
        if producto:
            print(f"\nProducto encontrado:")
            print(f"  {producto}")
        else:
            print(f"\nError: No se encontró un producto con el nombre '{nombre}'.")
            
    except Exception as e:
        print(f"Error inesperado: {e}")


def calcular_valor_total_menu(inventario):
    """
    Función auxiliar para calcular y mostrar el valor total del inventario.
    """
    try:
        valor_total = inventario.calcular_valor_inventario()
        print(f"\nValor total del inventario: ${valor_total:.2f}")
    except Exception as e:
        print(f"Error al calcular el valor total: {e}")


def main():
    """
    Función principal que inicializa el sistema de inventario.
    """
    print("Bienvenido al Sistema de Inventario\n")
    inventario = Inventario()
    menu_principal(inventario)


if __name__ == "__main__":
    main()
