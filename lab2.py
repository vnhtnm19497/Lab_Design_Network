import numpy as np 
import matplotlib.pyplot as plt
import math

def prob_distribution(lamda, mu, g,c): 
    ro = [l / mu for l in lamda] 
    prob = [] 
    p_1g = sum([(sum(ro)**i)/math.factorial(i) for i in range(g + 1)])
    p_gc = sum([((sum(ro)**g)*(ro[0]**(n-g)))/math.factorial(n) for n in range(g+1,c+1)])
    p0 = (p_1g + p_gc)**(-1)
    for j in range(g + 1):
        prob.append(p0 * (sum(ro)**j)/math.factorial(j))
    for k in range(g+1,c+1):
        prob.append(p0 * ((sum(ro)**g)*(ro[0]**(k-g)))/math.factorial(k))
    return prob

def prob_block_bytime1(lamda,mu,g,c):
    ro = [1 / mu for l in lamda]
    return prob_distribution(lamda,mu,g,c)[c]

def prob_block_bytime2(lamda,mu,g,c):
    ro = [1/mu for l in lamda]
    e2 = sum(prob_distribution(lamda,mu,g,c)[i] for i in range(g,c+1))
    return e2

def mean(lamda,mu,g,c):
    ro = [1/mu for l in lamda]
    prob_n = prob_distribution(lamda,mu,g,c)
    return sum([prob_n[n]*n for n in range (c+1)])

#Анализ данных
c = 30
g = 10
mu = 0.5
print ("Распределение вероятностей:") 
Pn = prob_distribution([1,15],0.5,10,30)
for i in range(c+1):
   print(Pn[i])
   
print ("Bероятность блокировки по времени 1-го: ")
E1 = prob_block_bytime1([1,15],0.5,10,30)
print(E1)

print ("Bероятность блокировки по времени 2-го: ")
E2 = prob_block_bytime2([1,15],0.5,10,30)
print(E2)

print("Cреднее число обслуживаемых в системе запросов:")
_n = mean([1,15],0.5,10,30)
print(_n)

#Построение график зависимости
#lamda1 - вероятность блокировок по времении 1-ого типа (E1)
E1 = [prob_block_bytime1([1,l], mu,g, c) for l in np.linspace(0,15,100)]
E2 = [prob_block_bytime2([1,l], mu,g, c) for l in np.linspace(0,15,100)]
plt.figure(figsize=(10,7), dpi=80)
plt.ylabel('Вероятность блокировки по времении')
plt.xlabel('Входящий поток, $\lambda_2$' )
plt.title(r'Вероятность блокировки по времени E запроса'+ '\n' + r'где C=30, $\lambda_1=1$, $\lambda_2=[0, 15]$, g=10 и $\mu=0.5$')
plt.plot(np.linspace(0,15,100),E1,'r-',label='Вероятность блокировки E1')
plt.plot(np.linspace(0,15,100),E2,'b-',label='Вероятность блокировки E2')
plt.legend(loc='best')
plt.show()

#lamda - среднее число запросов в системе
num = [mean([1, l], mu,g, c) for l in np.linspace(0, 15, 200)]
plt.ylim(0, c)
plt.ylabel('Среднее число запросов')
plt.xlabel('Входящий поток, $\lambda_2$' )
plt.title(r'Среднее число $\overline{N}$ обслуживаемых в системе запросов')
plt.plot(np.linspace(0, 15, 200), num)
plt.show() 
