from timeit import default_timer as timer
import matplotlib.pyplot as plt

#attack time complexity vs M
#fix a k and make u bigger

n_iter = 100
max_length = 400

k ='010101010'
Times = []
for j in range(n_iter):
  times = []
  for i in range(max_length):
    u = '10'*(i+1)
    start = timer()
    substitution_attack(u)
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
#fix a u and make k bigger

u ='010101010'
Times = []
for j in range(n_iter):
  times = []
  for i in range(max_length):
    k = '10'*(i+1)
    start = timer()
    substitution_attack(u)
    end = timer()
    times.append(end-start)
  Times.append(times)
avg = []
for i in range(max_length):
  avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('attack time complexity vs K')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#signing time complexity vs M
#fix a k and make u bigger
k ='010101010'
Times = []
for j in range(n_iter):
  times = []
  for i in range(max_length):
    u = '10'*(i+1)
    start = timer()
    sign(u,k)
    end = timer()
    times.append(end-start)
  Times.append(times)
avg = []
for i in range(max_length):
  avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('signing time complexity vs M')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

#signing time complexity vs K
#fix a u and make k bigger
u ='010101010'
Times = []
for j in range(n_iter):
  times = []
  for i in range(max_length):
    k = '10'*(i+1)
    start = timer()
    sign(u,k)
    end = timer()
    times.append(end-start)
  Times.append(times)
avg = []
for i in range(max_length):
  avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('signing time complexity vs K')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')

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
    verify(x,k,t)
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
    end = timer()
    times.append(end-start)
  Times.append(times)
avg = []
for i in range(max_length):
  avg.append(sum(t[i] for t in Times)/len(Times))

plt.plot(range(len(avg)),avg)
plt.title('veryfying time complexity vs K')
plt.xlabel('length [bits]')
plt.ylabel('time [s]')
