from numpy import array

def saisir():
    n = 0
    while not (1 <= n <= 100):
        n = int(input("Nombre de codes (1-100) : "))
    return n

def remplir(T, n):
    T[0] = int(input("T[0] = "))
    for i in range(1, n):
        ok = False
        while not ok:
            T[i] = int(input(f"T[{i}] = "))
            ok = (T[i] >= T[i - 1])
            if not ok:
                print("⚠️ Saisir une valeur ≥ à la précédente")

def recherche_d(T, n, v):
    a = 0
    b = n - 1
    trouve = False
    while (a <= b) and (not trouve):
        m = (a + b) // 2
        if T[m] == v:
            trouve = True
        elif T[m] > v:
            b = m - 1
        else:
            a = m + 1
    return trouve

# Programme principal
n = saisir()
T = array([int()] * n)
remplir(T, n)
v = int(input("Code à chercher : "))
trouve = recherche_d(T, n, v)
if trouve:
    print(f"Le code {v} existe dans le catalogue.")
else:
    print(f"Le code {v} n'existe pas dans le catalogue.")