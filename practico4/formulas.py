import numpy as np
import math

class Formulas:
    
    
    def transformada_inversa(self, probabilidades: list[tuple[any,float]] ):
        
        if sum([prob[1] for prob in probabilidades]) != 1:
            raise ValueError("suma de probabilidades distinta de 1")
        
        acumulada = 0
        u = np.random.random()
        for value, prob in probabilidades:
            acumulada += prob
            if acumulada >= u:
                break
        return value
    
    def udiscreta_0_n(self, n=1):
        return int(np.random() * n) + 1
    
    def udiscreta_n_m(self, n=0, m=1):
        return int(np.random() * (m-n+1)) + m
    
    def geometrica(self, p:float):
        if not 0 <= p <=1:
            raise ValueError( "p = PROBABILIDAD; BOTTTTTTTTTTTT")
        u = 1- np.random.random()
        return int(math.log(1-u) / math.log(1-p)) + 1
    
    def poissssssssson(self, lmbd:float):
        u = np.random.random()
        i = 0
        p = math.exp(-lmbd)
        F = p
        
        while u >= F:
            i += 1
            p *= lmbd/i
            F += p
        
        return i
    
    def binomial_n_p(self,n: int, p: float):

        acum = (1-p)**n
        f = acum
        n_exitos = 0
        u = np.random.random()
        while u >= f:
            acum *= p/ (1 - p) * (n - n_exitos) / (n_exitos + 1)        
            f += acum
            n_exitos += 1
        
        return n_exitos
    def urna(self, probabilidades: dict[any,float], k: int):
        a = []
        for key,value in probabilidades:
            for i in range(int(value*k)):
                a.append(key)
        
        return a[int(np.random.random() * k)]
    
    def aceptacion_y_rechazo_u (self, probabilidades_x:dict[any,float], sample_s:int):
        sample = []
        
        while len(sample) <= sample_s:
            
            y_pos = random.randint(1, len(probabilidades_x.keys()))
            y_value = list(probabilidades_x.keys())[y_pos - 1]
            y_prob = probabilidades_x.get(y_value)
            
            u = random.random()
            if u < y_prob:
                sample.append(y_value)
        
        return sample

    
p = [("caca", 0.1),
    ("pedo", 0.7),
    ("pis",  0.2)]
f = Formulas()

# for i in range(20):
#     print(f.transformada_inversa(p))
    
# print(f.geometrica(0.1))
# print(f.poissssssssson(0.25))
# print(f.binomial_n_p(10,0.9))
print(f.aceptacion_y_rechazo(probabilidades_x, probabilidades_y, sample_s))
