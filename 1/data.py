x = 5
y = 8
z = 3

S = z / 5.0 + 0.5
M = 2 * x + y + z + 15
G = 2 * x + 4 * y - z + 10

print('S = ', S)
print('M = ', M)
print('Средне значение интенсиввности сообщ: ', G)


print('-------------------------------------------------------')
print('|                                                      ')
print('|                    Задание 1. Шина                   ')
print('|                                                      ')

B = 10
V = 2.3 * (10 ** 5)
n_p = 2
L_p = 14
L_n = 1600
L_c = 320

#1
t_cp = S / V
print(t_cp * (10 ** 6))
#2
t_pt = n_p * (L_p / (B * (10 ** 6)))
print(t_pt * (10 ** 6))
#3
t = t_pt + t_cp
print(t * (10 ** 6))
#4
t_N = L_n / (B * (10 ** 6))
print(t_N * (10 ** 6))
#5
t_C = L_c /  (B * (10 ** 6))
print(t_C * (10 ** 6))
#6
t_cp_sum = t_N + t_C
print(t_cp_sum * (10 ** 6))
#7
v_cp = t_N / t_cp_sum
print(v_cp)
#8
gamma = M * G
print(gamma)
#9
R = gamma * t_cp_sum
print(R)
#10
alpha = t / t_cp_sum
print(alpha)
#11
t_N_by_t_cp = R * (1 + v_cp ** 2) * ( (1 + alpha * (1 + 2 * 2.7)) / (2 * (1 - R * (1 + alpha * (1 + 2 * 2.7))))) + 1 + alpha / 2.0
print(t_N_by_t_cp)
#12
t_nn = t_N_by_t_cp * t_cp_sum
print(t_nn * (10 ** 6))
#13
C = 1 / (1 + 6.44 * alpha)
print(C)
#14
g_max = C / t_cp_sum
print(g_max)
#15
t_n_min = (1 + alpha / 2.0) * t_cp_sum
print(t_n_min * (10 ** 6))

print('-------------------------------------------------------')
print('|                                                      ')
print('|                    Задание 2. Кольоцо                ')
print('|                                                      ')

L_C = 1600
h = 22
d = 48
b = 2

#1
toe = S / (M * V)
print(toe * (10 ** 6))
#2
t_cp = L_C / (B * (10 ** 6))
print(t_cp * (10 ** 6))
#3
print(gamma)
#4
R = gamma * t_cp
print(R)
#5
L_k = M * (b + B * (10 ** 6) * toe)
print(L_k)
#6
N = int(L_k / (h + d))
print(N)
#7
g = L_k / N 
print(g)
#8
C = d / g
print(C)
#9
t_n_by_toe = 1 / (C - R)
print(t_n_by_toe)
#10
t_n = t_n_by_toe * t_cp
print(t_n * (10 ** 6))
#11
t_n_min = t_cp / C
print(t_n_min * (10 ** 6))














