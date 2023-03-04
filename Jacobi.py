#Primero que nada pongo esto
import numpy as np
#Importo la librería NumPy, que es una biblioteca de Python para el cálculo científico

#Aquí defino la matriz de coeficientes A del sistema de ecuaciones de 4x4
#Como una matriz NumPy de 4x4 con los valores correspondientes del sistema de ecuaciones
A = np.array([[10, 1, -1, 2], [1, 10, 2, -1], [-1, 2, 10, 1], [2, -1, 1, 10]])

#Defino el vector de términos independientes b del sistema de ecuaciones de 4x4
#Como un vector NumPy con los valores correspondientes del sistema de ecuaciones
b = np.array([12, 8, 6, 10])

#DefinO la aproximación inicial x del método de Jacobi como un vector NumPy de ceros de longitud 4
#Este vector se irá actualizando en cada iteración del método de Jacobi hasta alcanzaR
#la solución del sistema de ecuaciones
x = np.array([0, 0, 0, 0])

#Defino el número máximo de iteraciones max_iter que se permitirán en el método de Jacobi
#Si el método no converge antes de alcanzar este número de iteraciones, se interrumpe el
#Bucle while y se imprime un mensaje de error
max_iter = 100

#Defino la tolerancia "tolerance" que se utilizará para determinar si el método de Jacobi
#Ha alcanzado la solución del sistema de ecuaciones. La solución se considera alcanzada
#Cuando la distancia entre la aproximación actual y la anterior es menor que la tolerancia
tolerance = 1e-10

#Defino aquí el inicializador por asi decirlo que es el contador de iteraciones iter_count a cero
#Este contador se irá incrementando en cada iteración del método de Jacobi hasta alcanzar
#El número máximo de iteraciones
iter_count = 0

#Pues aqui va el método de Jacobi mediante un bucle while que se ejecuta mientras el número de
#Iteraciones no supere el número máximo de iteraciones max_iter
while iter_count < max_iter:
    #Calculo la nueva aproximación x_new mediante la fórmula del método de Jacobi
    #Que se utiliza para actualizar cada componente del vector x
    x_new = np.zeros_like(x)
    #El bucle for interno calcula la suma de los productos
    for i in range(len(A)):
        s = 0
        for j in range(len(A)):
            if j != i:
                s += A[i][j] * x[j]
        x_new[i] = (b[i] - s) / A[i][i]
    if np.allclose(x, x_new, atol=tolerance):
        break
    x = x_new
    iter_count += 1

#Imprimo la solución
print("La solución es:", x)
#El Fin
#Cabe aclarar que el resultado puede diferir dependiendo del numero de iteraciones
#Pero no suele ser mucho
