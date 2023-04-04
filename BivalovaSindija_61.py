diena = ['pirmdiena', 'otrdiena', 'trešdiena', 'ceturtdiena', 'piektdiena', 'sestdiena', 'svētdiena']
temperatura = [0] * 7 # definējam masīvu ar 7 elementiem

for numurs in range(7): # ievadām masīva elementus
    temperatura[numurs] = int(input('Ievadiet ' + diena[numurs] + 's gaisa temperatūru: '))

dienu_skaits = 0
for numurs in range(7):
    if temperatura[numurs] > 25:
        dienu_skaits = dienu_skaits + 1 # dienu saskaitīšana
print('Nedēļas karstāko dienu skaits bija', dienu_skaits)