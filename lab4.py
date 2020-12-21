import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fct

C = 10
g = 8
b1 = 1
b2 = 1
lamda1 = 0.25
lamda2 = 7
m = 1
r1 = lamda1/m
r2 = lamda2/m
#Пространство состояния
X = []
for  n1 in range(g+1):
    X.append([n1,0])
for n1 in range(g+1):
    for n2 in range(1,C+1):
        if (b1*n1+b2*n2 <= C):
            X.append([n1,n2])
print('Пространство состояния = ', X)
print('Размер пространства состояния = ', len(X))
#Множество блокировок 
B1 = []
for n2 in range(C+1):
    if (b1*n1+b2*n2 <=C):
        B1.append([g,n2])
for n1 in range(g):
    for n2 in range(1,C+1):
        if (b1*n1+b2*n2 == C):
            B1.append([n1,n2])
B2 = []
for n1 in range(g+1):
    for n2 in range(C+1):
        if (b1*n1+b2*n2 == C):
            B2.append([n1,n2])
print('Множество блокировок 1-ого типа = ', B1)
print('Множество блокировок 2-ого типа =', B2)
#Множество приема
S1 = []
for n1 in range(g):
    for n2 in range(C+1):
        if (b1*n1+b2*n2 < C):
            S1.append([n1,n2])
S2 = []
for n1 in range(g+1):
    for n2 in range(C+1):
        if (b1*n1+b2*n2 < C):
            S2.append([n1,n2])
print('Множество приема 1-ого типа = ', S1)
print('Множество примеа 2-ого типа = ', S2)

#Функции для анализа характеристик модели
def p_zero(C,r1,r2):
    return sum([((r1**n1)/fct(n1))*((r2**n2)/fct(n2)) for n1 in range(g+1)  for n2 in range(C+1) if (n1+n2 <=C)]) ** (-1)

def p_n(C,r1,r2):
    p_00 = p_zero(C,r1,r2)
    return [[p_00*((r1**n1)/fct(n1))*((r2**n2)/fct(n2))  for n2 in range(C+1) if (n1+n2 <=C)] for n1 in range(g+1)]
print("Распределение вероятностей: ", p_n(C,r1,r2))

def p_block1(C,r1,r2):
    prob_n = p_n(C,r1,r2)
    b_1 = []
    for n2 in range(C):
        if (g+n2 <=C):
            b_1.append(prob_n[g][n2])
    for n1 in range (g):
        for n2 in range(1,C+1):
            if (b1*n1+b2*n2 == C):
                b_1.append(prob_n[n1][n2])
    return sum(b_1)
print("Вероятность блокировки 1-ого типа:", p_block1(C,r1,r2))

def p_block2(C,r1,r2):
    prob_n = p_n(C,r1,r2)
    b_2 = []
    for n1 in range (g+1):
        for n2 in range(C+1):
            if (b1*n1+b2*n2 == C):
                b_2.append(prob_n[n1][n2])
    return sum(b_2)
print("Вероятность блокировки 2-ого типа:", p_block2(C,r1,r2))

def avg_n1(C,r1,r2):
    N1 = []
    prob_n = p_n(C,r1,r2)
    for n1 in range(g+1):
        for n2 in range(C+1):
            if (b1*n1+b2*n2 <=C):
                N1.append(n1*prob_n[n1][n2])
    return sum(N1)
print("Среднее число обслуживаемых в системе запросов 1-ого типа:", avg_n1(C,r1,r2))

def avg_n2(C,r1,r2):
    N2 = []
    prob_n = p_n(C,r1,r2)
    for n1 in range(g+1):
        for n2 in range(C+1):
            if (b1*n1+b2*n2 <=C):
                N2.append(n2*prob_n[n1][n2])
    return sum(N2)
print("Среднее число обслуживаемых в системе запросов 2-ого типа:", avg_n2(C,r1,r2))

def avg_n(C,r1,r2):
    N1 = avg_n1(C,r1,r2)
    N2 = avg_n2(C,r1,r2)
    N = N1+N2
    return N
print("Среднее число обслуживаемых в системе", avg_n(C,r1,r2))

lamda = np.arange(0.25,10,0.01)
ro = lamda/0.5
p_b1 = [p_block1(C, ri, r2) for ri in ro]
p_b2 = [p_block2(C, ri, r2) for ri in ro]
plt.figure(figsize=(10, 7), dpi=80)
plt.ylabel('Вероятность блокировки обслуживания запроса')
plt.xlabel('Интенсивность поступления запросов')
plt.title('График зависимости вероятности блокировки от интенсивности поступления запросов')
plt.plot(lamda, p_b1,'r-',label='Вер. блокировки 1-ого типа')
plt.plot(lamda, p_b2,'b-',label='Вер. блокировки 2-ого типа')
plt.legend(loc='best')
plt.show()

avg_n1 = [avg_n1(C, ri, r2) for ri in ro]
avg_n2 = [avg_n2(C,ri,r2) for ri in ro]
plt.figure(figsize=(10, 7), dpi=80)
plt.ylabel('Сред. число обслуживаемых запросов')
plt.xlabel('Интенсивность поступления запросов')
plt.title('График зависимости среднего числа от интенсивности поступления запросов')
plt.plot(lamda, avg_n1,'r-',label='Сред. число N1')
plt.plot(lamda, avg_n2,'b-',label='Сред. число N2')
plt.legend(loc='best')
plt.show()