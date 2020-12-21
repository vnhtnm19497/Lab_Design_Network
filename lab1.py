import numpy as np 
import matplotlib.pyplot as plt
import math

def prob_distribution(lamda, mu, c): 
    ro = [l / mu for l in lamda] 
    prob = [] 
    p0 = sum([(sum(ro)**i)/math.factorial(i) for i in range(c + 1)])**(-1)
    for capacity in range(c + 1):
        prob.append(p0 * (sum(ro)**capacity)/math.factorial(capacity)) 
    return prob

def prob_block_bytime(lamda,mu,c):
    ro = [1 / mu for l in lamda]
    return prob_distribution(lamda,mu,c)[c]

def prob_block_bycall(lamda,mu,c):
    ro = [1/mu for l in lamda]
    return [prob_block_bytime(lamda,mu,c) * l / sum(lamda) for l in lamda]

def mean(lamda,mu,c):
    ro = [1/mu for l in lamda]
    prob_n = prob_distribution(lamda,mu,c)
    return sum([prob_n[n]*n for n in range (c+1)])

#Анализ данных
c = 30
mu = 0.5
print ("Распределение вероятностей:") 
a = prob_distribution([1,15],0.5,30)
for i in range(c+1):
   print(a[i])
   
print ("Bероятность блокировки по времени:")
e = prob_block_bytime([1,15],0.5,30)
print(e)

print("Вероятность блокировки по вызовам:")
b = prob_block_bycall([1,15],0.5,30)
print(b)

print ("Beроятность блокировки по нагрузке:")
C = e
print(C)

print("Cреднее число обслуживаемых в системе запросов:")
_n = mean([1,15],0.5,30)
print(_n)

#Построение график зависимости
#lamda1 - вероятность блокировок по времении и по нагрузке (E = C)
E = [prob_block_bytime([l,15], mu, c) for l in np.linspace(1,15,200)]
plt.ylim(0, max(E))
plt.xlim(0,15)
plt.ylabel('Вероятность блокировки по времении')
plt.xlabel('Входящий поток, $\lambda_1$' )
plt.title('Вероятность блокировки по времени E запроса')
plt.plot(np.linspace(1,15,200),E)
plt.savefig('lamda-e.png')
plt.show()

#lamda - среднее число запросов в системе
num = [mean([l, 15], mu, c) for l in np.linspace(0, 15, 200)]
plt.ylim(0, c)
plt.xlim(0,15)
plt.ylabel('Среднее число запросов')
plt.xlabel('Входящий поток, $\lambda_1$' )
plt.title(r'Среднее число $\overline{N}$ обслуживаемых в системе запросов')
plt.plot(np.linspace(0, 15, 200), num)
plt.savefig('lamda-n.png')
plt.show()