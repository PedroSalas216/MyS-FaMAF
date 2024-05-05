# ejercicio 1
def von_neuman():
    print("---- Ejercicio 1)a) ----")
    
    seeds = [3792,1004,2100,1234]
    for seed in seeds:
        output = [seed]
        number = seed
        for i in range(10):
            number = ((number ** 2) // 1000 )% 10000
            output.append(number)
        
    
        print(output)
    print("--------------------------------")    
    
    
def congruential_generator():
    print("---- Ejercicio 1)b) ----")
    
    seeds = [4,50]
    for seed in seeds:
        output = [seed]
        num = seed
        for i in range(10):
            num = (num*5 + 4 ) % 32
            output.append(num)
            
        print(output)
    print("--------------------------------")    
    
von_neuman()
congruential_generator()

# ejercicio 2 
import random
def game_sim():
    print("---- Ejercicio 2)a) ----")
    
    count = 0
    tests = [100,1000,10_000,100_000,1_000_000]
    
    for t in tests:
        
        for i in range(t):    
            x = 0
            u = random.random()
            if u < 0.5:
                x = random.random() + random.random()
            else:
                x = random.random() + random.random() + random.random()
            
            if x >= 1:
                count +=1
        print(f"Simulated probability with nsim = {t}: -> {count/t}")

    print("--------------------------------")    

game_sim()

# ejercicio 4 
def sim(n):
    s = 0
    for _ in range(0, n):
        u = random.random()

        if u < 0.4:
            x = expovariate(1 / 3)
        elif u < 0.32:
            x = expovariate(1 / 4)
        else:
            x = expovariate(1 / 5)
        
        if x < 4:
            s += 1

    return s/n

# ejercicio 9
def game_sim_9(nsim = 10_000):
    print("\n---- Ejercicio 9 ----")
    
    count = 0
    for _ in range(nsim):
        score = 0
        frst_dice = random.randint(1,6)
        if frst_dice == 1 or frst_dice == 6:
            score = 2* random.randint(1,6)
        else:
            score = random.randint(1,6) +  random.randint(1,6)
        
        if score > 6:
            count += 1
        
    print(f"Simulated probability of win: {count/nsim}")

game_sim_9()