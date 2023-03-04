# Matriz-por-Jacobi
Una vez dado un sistema de matrices con su vector solución, es decir un sistema de ecuaciones de 4x4, resuelve por medio de método Jacobi.

El código viene con un sistema de ecuaciones por defecto:

>10x + y  - z + 2w  = 12

>x  + 10y + 2z - w  = 8

>-x + 2y  + 10z + w = 6

>2x  - y + z + 10w = 10

El cual se denota en Python como:

A = np.array

>([[10, 1, -1, 2],

>[1, 10, 2, -1]

>[-1, 2, 10, 1]

>[2, -1, 1, 10]])

Y el vector solución que es:

b = np.array

>([12, 8, 6, 10])

Con iteraciones de:

x = np.array

>([0, 0, 0, 0])

El usuario puede editar "A","b" y "x" dependiendo de la ecuacioón que busca resolver. 
