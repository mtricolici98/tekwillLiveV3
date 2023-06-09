"""
Scrieți un program_exemplu care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""

propozitie = input("Introduceți o propoziție: ")

if propozitie.endswith("?"):
    print("Aceasta este o întrebare.")
else:
    print("Aceasta nu este o întrebare.")

# Alte variante
# if propozitie[-1] == '?':
#     print("Aceasta este o întrebare.")
# else:
#     print("Aceasta nu este o întrebare.")
#
# if '?' in propozitie[-1]:
#     print("Aceasta este o întrebare.")
# else:
#     print("Aceasta nu este o întrebare.")
