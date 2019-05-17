# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym

# INGRESO , Datos de prueba
xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])

# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0,n,1):
    # Termino de Lagrange
    termino = 1
    for j  in range(0,n,1):
        if (j!=i):
            termino = termino*(x-xi[j])/(xi[i]-xi[j])
    polinomio = polinomio + termino*fi[i]
# Expande el polinomio
px = polinomio.expand()
# para evaluacion numérica
pxn = sym.lambdify(x,polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a,b,muestras)
fi_p = pxn(xi_p)

# Salida
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(px)
