#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
RSA
Autor:
    Ron Rivest, Adi Shamir, e Leonard Adleman 
Colaborador:
    Juan Lopes <me@juanlopes.net>
Tipo:
    crypto
Descri��o: 
    Implementa��o simples do algoritmo RSA.
    
    Este algoritmo se baseia na dificuldade computacional da fatora��o de
    n�meros inteiros.
    
    A id�ia que a chave p�blica e privada sejam baseadas na multiplica��o
    de dois n�meros primos (geralmente grandes) e que a rela��o entre elas
    exija o conhecimento dos fatores dessa multiplica��o.
Complexidade:
    O(n)
Dificuldade:
    medio
Refer�ncias:
    http://en.wikipedia.org/wiki/RSA_(algorithm)
"""

def gcd(a,b):
    if b==0: return (1, 0)
    q = a/b
    x,y = gcd(b, a-q*b)
    return (y, x-q*y)
    
def inverse(a, b):
    x,y = gcd(a,b)
    return (x if x > 0 else x+b)
   
def rsa(n, e, M):
    return map(lambda m: pow(m, e, n), M)
   
p,q = 41, 47              #primos             
n,phi = p*q, (p-1)*(q-1)  #m�dulo and totiente
e,d = 7, inverse(7,phi)   #expoentes p�blico e privado

plain = (1,2,3,4,5,6,7,42)
encrypted = rsa(n, e, plain)
plain_again = rsa(n, d, encrypted)

print 'Chave p�blica:', (n,e)
print 'Chave privada:', (n,d)
print '---'
print 'Mensagem original:', plain
print 'Mensagem encriptada:', encrypted
print 'Mensagem decriptada:', plain_again