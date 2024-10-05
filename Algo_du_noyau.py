#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:39:31 2024

@author: olivier
"""

def liste_puits(DAG: dict):
    # Retourne une liste de tous les sommets du DAG qui n'ont pas
    # de successeurs (puits)
    return [s for s in DAG if not DAG.get(s)]

def liste_predecesseurs(DAG: dict, s):
    # Retourne une liste de tous les prédécesseurs du sommet s dans
    # le DAG
    return [pred for pred in DAG if s in DAG.get(pred)]

def supprime_sommet(DAG: dict, s):
    # Supprime le sommet s du DAG
    DAG.pop(s)
    
    # Pour chaque prédécesseur de s, retire s de sa liste de
    # successeurs
    for pred in liste_predecesseurs(DAG, s):
        DAG.get(pred).remove(s)

def noyau(DAG: dict):
    # Calcule le noyau du DAG
    # Cette fonction prend en entrée un DAG représenté sous forme 
    # de liste d'adjacence et calcule son noyau.

    # Noyau du DAG
    N = []
    
    # Tant que le DAG n'est pas vide
    while DAG:
        # Trouve tous les puits dans le DAG actuel
        puits = liste_puits(DAG)
        
        for p in puits:
            # Ajoute chaque puits au noyau
            N.append(p)
           
            # Trouve les prédécesseurs du puits
            predecesseurs = liste_predecesseurs(DAG, p)
            
            # Supprime le puits du DAG
            supprime_sommet(DAG, p)
            
            # Supprime tous les prédécesseurs du puits du DAG
            for pred in predecesseurs:
                supprime_sommet(DAG, pred)
    # Retourne le noyau calculé
    return N

# Cas d'un jeu de soustraction avec position initiale N=20
def succ_soustraction(n, max_retire):
    return [n - i for i in range(1, max_retire + 1) if n - i >= 0]

N = 20
max_retire = 3

sous = {n: succ_soustraction(n, max_retire) for n in range(N + 1)}

print(f"Noyau du graphe d'un jeu de soustraction pour {N=}")
print(noyau(sous))

# Cas d'un jeu de nim à 3 piles avec position initiale (3,3,3)
def succ_nim(a,b,c):
    li=[(i,b,c) for i in range(a)] + [(a,i,c) for i in range(b)] + [(a,b,i) for i in range(c)]
    li=[tuple(sorted(i)) for i in li]
    return list(set(li)) 

N=3
nim={(a,b,c):succ_nim(a,b,c) for c in range(N+1) for b in range(c+1) for a in range(b+1)}

print(f"Noyau du graphe d'un jeu de Nim à {N} piles avec position initiale  ({N},{N}, {N})")
print(noyau(nim))