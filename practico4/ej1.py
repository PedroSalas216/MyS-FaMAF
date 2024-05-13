# Ejercicio 1
import numpy as np
nsims = [100, 1000, 10_000, 100_000, 10_000_000]
r = 10

for nsim in nsims:
    suma_exitos = 0
    suma_cuadrado = 0
    
    for _ in range(nsim):            
        perm = np.random.permutation(np.arange(100))
        comp = perm[:r] == np.arange(r)
        exito = True
        for c in comp:
            exito = exito and c
        suma_exitos += exito
        suma_cuadrado += exito
    
    print(f"n: {nsim}, \tE(x):{suma_exitos/nsim}, \tV(x): {(suma_cuadrado-(suma_exitos**2))/nsim}")



