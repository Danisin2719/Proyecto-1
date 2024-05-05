import math
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def Presentacion():
    print("*" * 50)
    print("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ".center(50))
    print("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES".center(50))
    print("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS".center(50))
    print("Manejo De Elementos Gráficos En Entorno Digitales".center(50))
    print("Proyecto 1".center(50))
    print("*" * 50)
    print("\nIntegrantes:\n")
    integrantes = ["Daniel Salinas", "Anthony Garcia", "Cristell Madrid", "Ethan Martinez"]
    for i, integrante in enumerate(integrantes, start=1):
        print(f"{i}. {integrante}".center(50))
    print("\nFecha de entrega: 6 de mayo de 2024".center(50))
    print("*" * 50)


def algoritmo_DDA():
    def DDA_line(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        steps = round(steps)  # Redondea steps al entero más cercano

        # Calcula los incrementos en cada paso
        increment_x = dx / steps if steps != 0 else 0
        increment_y = dy / steps if steps != 0 else 0

        # Inicializa las coordenadas actuales
        x, y = x1, y1

        # Crea listas para almacenar las coordenadas de los puntos
        x_points, y_points = [x1], [y1]

        # Imprime las diferenciales y la pendiente si existe
        print(f"Diferencial en X (dx): {dx}")
        print(f"Diferencial en Y (dy): {dy}")
        if dx != 0:
            pendiente = dy / dx
            print(f"Pendiente: {pendiente}")

        # Calcula y almacena las coordenadas de los puntos intermedios
        for _ in range(steps):
            x += increment_x
            y += increment_y
            x_rounded, y_rounded = round(x), round(y)
            x_points.append(x_rounded)
            y_points.append(y_rounded)

        # Agrega el punto final
        x_points.append(x2)
        y_points.append(y2)

        # Imprime la tabla de puntos
        table = PrettyTable(["Punto", "Coordenada X", "Coordenada Y"])
        for i, (x, y) in enumerate(zip(x_points, y_points), start=1):
            table.add_row([i, x, y])
        print("Tabla de puntos:")
        print(table)

        # Dibuja la línea
        plt.plot(x_points, y_points, marker='o')
        plt.title('Línea trazada con el algoritmo de DDA')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    # Función principal
    def main():
        print("Ingrese las coordenadas del punto inicial:")
        x1 = float(input("Coordenada X: "))
        y1 = float(input("Coordenada Y: "))

        print("Ingrese las coordenadas del punto final:")
        x2 = float(input("Coordenada X: "))
        y2 = float(input("Coordenada Y: "))

        # Llama a la función DDA_line para dibujar la línea
        DDA_line(x1, y1, x2, y2)

    if __name__ == "__main__":
        main()


def algoritmo_Bresenham():
    # Implementación del algoritmo Bresenham aquí
    print("Algoritmo Bresenham")

def algoritmo_circunferencia():
    # Implementación del algoritmo de la circunferencia aquí
    print("Algoritmo de la circunferencia")

def algoritmo_elipse():
        
    def plot_ellipse(ax, a, b, h, k):
        # Generar puntos de la elipse
        theta = np.linspace(0, 2 * np.pi, 100)
        x = a * np.cos(theta) + h
        y = b * np.sin(theta) + k

        # Dibujar la elipse y el centro
        ax.plot(x, y, label=f'Elipse con Rx={a}, Ry={b}')
        ax.scatter([h], [k], color='red', label='Centro') 
        ax.axhline(k, color='black', linewidth=0.5)
        ax.axvline(h, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        ax.set_aspect('equal', adjustable='box')
        ax.set_title(f'Elipse con Rx={a}, Ry={b}, Centro=({h},{k})')

    def midpoint_ellipse(rx, ry, xc, yc):
        k = 0
        x, y = 0, ry
        dx, dy = 2 * ry ** 2 * x, 2 * rx ** 2 * y
        points, table1, table2 = [], PrettyTable(), PrettyTable()
        table1.field_names, table2.field_names = ["k", "Pk", "Xk", "Yk", "(X,Y)", "2ry^2x", "2rx^2y"], ["k", "P2k", "Xk", "Yk", "(Xk, Yk)", "2ry^2(Xk+1)", "2rx^2(Yk+1)"]
        
        p1 = ry ** 2 - rx ** 2 * ry + (rx ** 2) / 4
        while True:
            points.extend([(x + xc, y + yc), (-x + xc, y + yc), (x + xc, -y + yc), (-x + xc, -y + yc)])
            table1.add_row([k, p1, x, y, (x, y), 2 * ry ** 2 * x, 2 * rx ** 2 * y])
            if dx > dy:  break
            if p1 < 0:  x += 1; dx += 2 * ry ** 2; p1 += dx + ry ** 2
            else:  x += 1; y -= 1; dx += 2 * ry ** 2; dy -= 2 * rx ** 2; p1 += dx - dy + ry ** 2
            k += 1
        print(table1)
        
        k += 1
        p2 = ry ** 2 * (x + 0.5) ** 2 + rx ** 2 * (y - 1) ** 2 - rx ** 2 * ry ** 2
        while y >= 0:
            points.extend([(x + xc, y + yc), (-x + xc, y + yc), (x + xc, -y + yc), (-x + xc, -y + yc)])
            table2.add_row([k, p2, x, y, (x, y), 2 * ry ** 2 * (x), 2 * rx ** 2 * (y)])
            if p2 > 0:  y -= 1; dy -= 2 * rx ** 2; p2 += rx ** 2 - dy
            else:  y -= 1; x += 1; dx += 2 * ry ** 2; dy -= 2 * rx ** 2; p2 += dx - dy + rx ** 2
            k += 1
        print(table2)

        # Dibujar la elipse
        fig, ax = plt.subplots(figsize=(6, 6))
        plot_ellipse(ax, rx, ry, xc, yc)
        plt.show()

    # Solicitar datos de la elipse y dibujarla
    print("Bienvenido al programa de dibujo de elipses")
    while True:
        rx = float(input("Ingrese el valor del semieje Rx: "))
        ry = float(input("Ingrese el valor del semieje Ry: "))
        xc = float(input("Ingrese la coordenada X del centro: "))
        yc = float(input("Ingrese la coordenada Y del centro: "))

        midpoint_ellipse(rx, ry, xc, yc)

        continuar = input("¿Desea dibujar otra elipse? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break



def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Presentacion")
    print("2. Algoritmo DDA")
    print("3. Algoritmo Bresenham")
    print("4. Algoritmo de la circunferencia")
    print("5. Algoritmo de la elipse")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            Presentacion()
        elif opcion == "2":
            algoritmo_DDA()
        elif opcion == "3":
            algoritmo_Bresenham()
        elif opcion == "4":
            algoritmo_circunferencia()
        elif opcion == "5":
            algoritmo_elipse()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()
