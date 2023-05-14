import matplotlib.pyplot as plt
import numpy as np
import random
import time
from timeit import default_timer as timer

attempt_m = []
attempt_k = []

def sign(u, k):
    u_int = int(u, 2)
    k_int = int(k, 2)
    s_u = sum_digits(u_int)
    s_k = sum_digits(k_int)
    s = s_u * s_k
    t = str(bin(s))[2:]
    return u, t

def sum_digits(n):
    n = str(n)
    s_n = 0
    for i in n:
        s_n += int(i)
    return s_n    

def verify(x, k, t):
    _, t_prime = sign(x, k)
    return t == t_prime

def substitution_attack(u):
    u_fake_int = str(int(u,2)*10)
    u_fake_bin = str(bin(int(u_fake_int)))[2:]
    return u_fake_bin


def task_1(u, k):
    x, t = sign(u, k)
    print(verify(x, k, t))


def task_2(u, k):    
    u, t = sign(u, k)
    #attack ---
    u_fake_bin = substitution_attack(u)
    #end of attack ---
    print(f"Il messaggio è {u_fake_bin}|{t}")
    print(f"Il messaggio è accettato? {verify(u_fake_bin, k, t)}") 

def task_3(f_u, k, flag):
    attempt = 0
    dict = {}
    found = 0
    #generazione dizionario
    for i in range(2 ** len(k), 2 ** (len(k) + 1) - 1):   
        s_k = sum_digits(i)
        if s_k in dict:
            dict[s_k] += 1
        else:
            dict[s_k] = 1
    #tentativi di trovare un sk uguale a quello vero
    while dict:
        max_value = max(dict.values())
        guesses = [key for key, value in dict.items() if value == max_value]
        guess = guesses[0]
        dict.pop(guess)
        k_bin = str(bin(guess))[2:]
        attempt += 1
        k_int = int(k, 2)
        if guess == sum_digits(k_int):
            f_u, f_t = sign(f_u, k_bin)
            found = 1
            #print(f"Attacco riuscito in {attempt} tentativi con la chiave {k_bin} il cui s_k vale {guess}")
            break
    if flag == 1:
        if found == 1:
            attempt_m.append(1/attempt)
        else:
            attempt_m.append(0)
    if flag == 0:
        if found == 1:
            attempt_k.append(1/attempt)
        else:
            attempt_k.append(0)
'''
#attack time complexity vs M
#fix a k and make u bigger
n_iter = 100
n_iter = 200
max_length = 400
#signing time complexity vs M
#fix a k and make u bigger

k ='010101010'
Times = []
for i in range(max_length):
    u = '10'*(i+1)
    start = timer()
    substitution_attack(u)
    sign(u,k)
    end = timer()
    times.append(end-start)
Times.append(times)
avg = []

for i in range(max_length):
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('attack time complexity vs M')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#attack time complexity vs K
#signing time complexity vs K
#fix a u and make k bigger

u ='010101010'
Times = []
for j in range(n_iter):
    times = []
    for i in range(max_length):
        k = '10'*(i+1)
        start = timer()
        substitution_attack(u)
        sign(u,k)
        end = timer()
        times.append(end-start)
    Times.append(times)
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('attack time complexity vs K')
plt.title('signing time complexity')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#signing time complexity vs M
plt.legend(['vs M','vs K'])
plt.show()
#veryfying time complexity vs M
#fix a k and make u bigger

k ='010101010'
Times = []
for j in range(n_iter):
    times = []
    for i in range(max_length):
        u = '10'*(i+1)
        x,t = sign(u,k)
        start = timer()
        sign(u,k)
        verify(x,k,t)
        end = timer()
        times.append(end-start)
    Times.append(times)
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('signing time complexity vs M')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#signing time complexity vs K
#veryfying time complexity vs K
#fix a u and make k bigger
u ='010101010'
Times = []
for j in range(n_iter):
    times = []
    for i in range(max_length):
        k = '10'*(i+1)
        x,t = sign(u,k)
        start = timer()
        sign(u,k)
        verify(x,k,t)
        end = timer()
        times.append(end-start)
    Times.append(times)
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('signing time complexity vs K')
plt.title('verifying time complexity')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')
plt.legend(['vs M','vs K'])
plt.show()

#veryfying time complexity vs M
#attack time complexity vs M
#fix a k and make u bigger

k ='010101010'
Times = []
for j in range(n_iter):
    times = []
    for i in range(max_length):
        u = '10'*(i+1)
        x,t = sign(u,k)
        start = timer()
        verify(x,k,t)
        substitution_attack(u)
        end = timer()
        times.append(end-start)
    Times.append(times)
avg = []

for i in range(max_length):
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('veryfying time complexity vs M')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#veryfying time complexity vs K
#attack time complexity vs K
#fix a u and make k bigger

u ='010101010'
Times = []
for j in range(n_iter):
    times = []
    for i in range(max_length):
        k = '10'*(i+1)
        x,t = sign(u,k)
        start = timer()
        verify(x,k,t)
        substitution_attack(u)
        end = timer()
        times.append(end-start)
    Times.append(times)
    avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('veryfying time complexity vs K')
plt.title('attack time complexity')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')
plt.legend(['vs M','vs K'])
plt.show()          
            
'''
def main():
    task_1('100011', '1001110')
    task_2('100011', '1001110')
    time_m = []
    time_k = []
    dimension = np.arange(1, 21, 1)
    for i in dimension:
        #vario m
        #creo u casuale in base alla lunghezza
        u = '1'
        k_x = '1'
        for _ in range(6 - 1):
            bit_k = random.randint(0, 1)
            k_x += str(bit_k)
        for _ in range(i - 1):
            bit = random.randint(0, 1)
            u += str(bit)
        #eseguo la task misurando il tempo
        start_time = time.time()
        task_3(u, k_x, 1)
        end_time = time.time()
        time_m.append(end_time - start_time)
    for j in dimension:
        #vario k
        #creo k casuale in base alla lunghezza
        k = '1'
        for _ in range(j - 1):
            bit = random.randint(0, 1)
            k += str(bit)
        #eseguo la task misurando il tempo
        start_time = time.time()
        task_3('101101', k, 0)
        end_time = time.time()
        time_k.append(end_time - start_time)
    fig, ax = plt.subplots(ncols=2)
    ax[0].plot(dimension, time_m)
    ax[0].set_xlabel("Lunghezza messaggio")
    ax[0].set_ylabel("Tempo impiegato")
    ax[0].set(ylim=(0, max(time_k)))
    ax[1].plot(dimension, time_k)
    ax[1].set_xlabel("Lunghezza chiave")
    ax[1].set_ylabel("Tempo impiegato")
    ax[1].set(ylim=(0, max(time_k)))
    plt.show()
    fig, ax = plt.subplots(ncols=2)
    ax[0].plot(dimension, attempt_m)
    ax[0].set_xlabel("Lunghezza messaggio")
    ax[0].set_ylabel("Probabità")
    ax[0].set(ylim=(0, 1.1))
    ax[1].plot(dimension, attempt_k)
    ax[1].set_xlabel("Lunghezza chiave")
    ax[1].set_ylabel("Probabilità")
    ax[1].set(ylim=(0, 1.1))
    plt.show()

if __name__ == "__main__":
    main()