# --------------- EX 1 ---------------
# Escreva um algoritmo recursivo para cada uma das alternativas
'''
a)
S(1) = 10
S(n) = S(n – 1) + 10,  para n >= 2
'''


def a_alt(n):
    if n == 1:
        S = 10
    else:
        S = a_alt(n - 1) + 10
    return S


'''
b)
A(1) = 2
A(n) = A(n – 1)-1 ,  para n  2

'''


def b_alt(n):
    if n == 1:
        A = 2
    else:
        A = b_alt(n - 1) - 1
    return A


'''
c)	
B(1) = 1
B(n) = B(n – 1) + n2,  para n  2

'''


def c_alt(n):
    if n == 1:
        B = 1
    else:
        B = c_alt(n - 1) + (n * n)
    return B


'''
d)	
P(1) = 1
P(n) = n^2 * P(n – 1) + n - 1,  para n  2
'''


def d_alt(n):
    if n == 1:
        P = 1
    else:
        P = (n * n) * d_alt(n - 1) + (n - 1)
    return P


'''
e)	
D(1) = 3
D(2) = 5
D(n) = (n – 1)*D(n – 1) + (n – 2)*D(n – 2), para n > 2

'''


def e_alt(n):
    if n == 1:
        D = 3
    elif n == 2:
        D = 5
    else:
        D = (n - 1) * e_alt(n - 1) + (n - 2) * e_alt(n - 2)
    return D


'''
f)	
W(1) = 2
W(2) = 5
W(n) = W(n – 1)*W(n – 2), para n > 2
'''


def f_alt(n):
    if n == 1:
        W = 2
    elif n == 2:
        W = 5
    else:
        W = f_alt(n - 1) * f_alt(n - 2)
    return W


'''
g)	
T(1) = 1
T(2) = 2
T(3) = 3
T(n) = T(n – 1) + 2*T(n – 2) + 3*T(n – 3),   para n > 3

'''


def g_alt(n):
    if n == 1:
        T = 1
    elif n == 2:
        T = 2
    elif n == 3:
        T = 3
    else:
        T = g_alt(n - 1) + 2 * g_alt(n - 2) + 3 * g_alt(n - 3)
    return T


# --------------- EX 3 ---------------
'''

3.	Uma coleção T de números é definida recursivamente por:
2 pertence a T
Se X pertence a T, então 	X+3 pertence a T 	e 	2*X pertence a T 

Quais dos seguintes números pertencem a T? 6 , 7 , 19 , 12.
Faça um programa recursivo para demonstrar. (0,5)
'''

# Dos números dados, os seguintes pertencem ao programa: 7 e 19.


# Em que n se refere ao número de termos e m se refere ao n-ésimo termo.
def colecao_T(n):
    if n == 1:  # 2 é o único número sabemos que pertence a T. Então ele é tido como passo base
        m = 2
    else:
        m = colecao_T(n - 1) + 3  # "passo 1"
        print(str(m) + ' (pertence a partir do passo 1)')
        m = colecao_T(n - 1) * 2  # "passo 2"
        print(str(m) + ' (pertence a partir do passo 2)\n')
    return m
