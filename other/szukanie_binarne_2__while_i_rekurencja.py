# binary search po listach posortowanych


def main():

    uniwersytety = [
        "Bercley",
        "California",
        "Cambridge",
        "Chicago",
        "Columbia",
        "Harvard",
        "MIT",
        "Oxford",
        "Pennsylvania",
        "Princeton",
        "Sorbonne",
        "Stanford",
        "Yale",
    ]

    print("\n", uniwersytety)
    szukany = input("\nKtórego szukamy?\n")
    print()

    # zapis 1 : while : 12 linii
    while len(uniwersytety) > 0:
        srodkowy = round(len(uniwersytety) / 2)

        if szukany == uniwersytety[srodkowy]:
            print(f"Znalazłem {szukany}!\n")
            break

        elif szukany < uniwersytety[srodkowy]:
            uniwersytety = uniwersytety[0:srodkowy]

        else:
            uniwersytety = uniwersytety[srodkowy + 1 : len(uniwersytety)]

    # zapis 2 : funkcja z rekurencją : 18 linii
    szukaj(uniwersytety, szukany)


def szukaj(uniwersytety, szukany):

    if len(uniwersytety) == 0:
        return

    srodkowy = round(len(uniwersytety) / 2)

    if szukany == uniwersytety[srodkowy]:
        print(f"Znalazłem {szukany} dzięki szukaj!\n")
        return

    elif szukany < uniwersytety[srodkowy]:
        uniwersytety = uniwersytety[0:srodkowy]

    else:
        uniwersytety = uniwersytety[srodkowy + 1 : len(uniwersytety)]

    szukaj(uniwersytety, szukany)


if __name__ == "__main__":
    main()

# można teraz porównać czas działania algorytmów
