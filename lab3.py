import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fct

#Raw data
C = 100
l1 = 30
l2 = 60
theta1 = 2
theta2 = 4
a1 = theta1 * l1 / C
a2 = theta2 * l2 / C

#Main function
def p_zero(C, a1, a2):
  return sum([fct(n1 + n2) * (a1 ** n1 / fct(n1)) * (a2 ** n2 / fct(n2)) for n2 in range(C + 1) for n1 in range(C + 1) if(n1 + n2 <= C)]) ** -1

def p_n(C, a1, a2):
    p_0 = p_zero(C, a1, a2)
    return [[(a1 ** n1 / fct(n1)) * (a2 ** n2 / fct(n2)) * fct(n1 + n2) * p_0 for n2 in range(C + 1) if(n1 + n2 <= C)] for n1 in range(C + 1)]

def average_n(l1, l2, theta1, theta2):
    n1 = l1 * (theta1 / (theta1 * l1 + theta2 * l2))
    n2 = l2 * (theta2 / (theta1 * l1 + theta2 * l2))
    return [n1, n2]

def average_t(l1, l2, theta1, theta2):
    a_n = average_n(l1, l2, theta1, theta2)
    return [a_n[0] / l1, a_n[1] / l2]

#Analysis data 
print('Распределение верояностей:')
prob_n = p_n(C, a1, a2)
for n1 in range(C+1):
    for n2 in range(C+1):
        if (n1+n2 <= C):
            print(prob_n[n1][n2])

print('Среднее число в системе запросов на передачу данных [N1,N2]:')
avg_n = average_n(l1, l2, theta1, theta2)
print(avg_n)

print('Среднее время в системе запросов на передачу данных [T1,T2]:')
avg_t = average_t(l1, l2, theta1, theta2)
print(avg_t)

#Graph's dependencies
l = np.arange(0.5, 30, 0.5)
avg_t1 = [average_t(l1, li, theta1, theta2)[0] for li in l]
avg_t2 = [average_t(l1, li, theta1, theta2)[1] for li in l]
plt.figure(figsize=(10, 7), dpi=80)
plt.ylabel('Сред. время обслуживания запроса')
plt.xlabel('Интенсивность поступления запросов')
plt.title('График зависимости среднего времени от интенсивности поступления запросов')
plt.plot(l, avg_t1,'r-',label='Сред. время T1')
plt.plot(l, avg_t2,'b-',label='Сред. время T2')
plt.legend(loc='best')
plt.show()

avg_n1 = [average_n(l1, li, theta1, theta2)[0] for li in l]
avg_n2 = [average_n(l1, li, theta1, theta2)[1] for li in l]
plt.figure(figsize=(10, 7), dpi=80)
plt.ylabel('Сред. число обслуживаемых запросов')
plt.xlabel('Интенсивность поступления запросов')
plt.title('График зависимости среднего числа от интенсивности поступления запросов')
plt.plot(l, avg_n1,'r-',label='Сред. число N1')
plt.plot(l, avg_n2,'b-',label='Сред. число N2')
plt.legend(loc='best')
plt.show()