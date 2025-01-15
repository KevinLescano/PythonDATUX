#################################
## Alumno: Kevin Lescano Banda ##
#################################

## 1.Definimos el diccionario inicial de ventas
ventas = [
    {"fecha": "12-01-2023", "producto": "Producto_A", "cantidad": 50, "precio": 45.00, "promocion": True},
    {"fecha": "11-01-2023", "producto": "Producto_AX", "cantidad": 160, "precio": 12.00, "promocion": False},
    {"fecha": "10-01-2023", "producto": "Producto_D", "cantidad": 20, "precio": 15.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_C", "cantidad": 10, "precio": 140.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_D", "cantidad": 1200, "precio": 1.00, "promocion": True}
]

## 2. Desarrollo de la función para mostrar el menú interactivo definido.
def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto con más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_listado_ventas()
        elif opcion == "2":
            añadir_producto()
        elif opcion == "3":
            calcular_suma_total()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_listado_productos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente por favor.")

## 3. Desarrollo de la función para mostrar el listado de ventas
def mostrar_listado_ventas():
    print("\nListado de Ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

## 4. Función para añadir un nuevo producto al diccionario de ventas creado anteriorme.
def añadir_producto():
    fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Está en promoción? (sí/no): ").lower() == "sí"
    nueva_venta = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion}
    ventas.append(nueva_venta)
    print("Producto añadido correctamente.")

## 5. Establecimiento de función para calcular la suma total de las ventas
def calcular_suma_total():
    suma_total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    print(f"La suma total de las ventas es: {suma_total:.2f}")

## 6. Establecimiento de función para calcular el promedio de las ventas
def calcular_promedio_ventas():
    suma_total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    promedio = suma_total / len(ventas)
    print(f"El promedio de las ventas es: {promedio:.2f}")

## 7. Función para mostrar el producto con más unidades vendidas
def producto_mas_vendido():
    max_venta = max(ventas, key=lambda x: x["cantidad"])
    print(f"El producto con más unidades vendidas es: {max_venta['producto']} con {max_venta['cantidad']} unidades.")

##8. Desarrollo de la función para mostrar el listado de productos (sin duplicados para el presente caso)
def mostrar_listado_productos():
    productos = set(venta["producto"] for venta in ventas)
    print("Listado de productos:")
    for producto in productos:
        print(producto)

