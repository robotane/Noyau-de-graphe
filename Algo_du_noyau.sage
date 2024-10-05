#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:39:31 2024

@author: olivier
"""

from sage.all import *

def noyau(DAG: Graph):
    # Calcule le noyau du DAG
    # Cette fonction prend en entrée un DAG représenté sous forme 
    # de liste d'adjacence et calcule son noyau.

    # Noyau du DAG
    N = []
    
    # Tant que le DAG n'est pas vide
    while DAG:
        # Trouve tous les puits dans le DAG actuel
        puits = DAG.sinks()
        
        for p in puits:
            # DiGraph(DAG).show()

            # Ajoute chaque puits au noyau
            N.append(p)
           
            # Trouve les prédécesseurs du puits
            predecesseurs = DAG.neighbors(p)
            # print(predecesseurs)

            # Supprime le puits du DAG
            DAG.delete_vertex(p)
            
            # Supprime tous les prédécesseurs du puits du DAG
            DAG.delete_vertices(predecesseurs)
    # Retourne le noyau calculé
    return N

# Cas d'un jeu de soustraction avec position initiale N=20
def succ_soustraction(n, max_retire):
    return [n - i for i in range(1, max_retire + 1) if n - i >= 0]

N = 20
max_retire = 3

sous = {n: succ_soustraction(n, max_retire) for n in range(N + 1)}

DiGraph(sous).show()
print(f"Noyau du graphe d'un jeu de soustraction pour {N=}")
print(noyau(sous))

# Cas d'un jeu de nim à 3 piles avec position initiale (3,3,3)
def succ_nim(a,b,c):
    li=[(i,b,c) for i in range(a)] + [(a,i,c) for i in range(b)] + [(a,b,i) for i in range(c)]
    li=[tuple(sorted(i)) for i in li]
    return list(set(li)) 

N=3
nim={(a,b,c):succ_nim(a,b,c) for c in range(N+1) for b in range(c+1) for a in range(b+1)}

Poset(nim).show()
print(f"Noyau du graphe d'un jeu de Nim à {N} piles avec position initiale  ({N},{N}, {N})")
print(noyau(nim))
