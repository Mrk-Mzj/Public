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

    # sprawdzanie czy odpowiedź jest na liście uniwersytetów
    while True:
        szukany = input("\nKtórego szukamy?\n")

        if szukany in uniwersytety:
            break
    print()

    # szukanie z licznikiem położenia

    # środkowy - to położenie szukanego elementu względem aktualnej, krótszej sublisty
    # pozycja - to położenie względem oryginalnej, długiej listy
    srodkowy = round(len(uniwersytety) / 2)
    pozycja = round(len(uniwersytety) / 2)

    while len(uniwersytety) > 0:

        if szukany == uniwersytety[srodkowy]:

            print(f"Znalazłem {szukany} na pozycji {pozycja}!\n")
            break

        elif szukany < uniwersytety[srodkowy]:

            # skracamy listę
            uniwersytety = uniwersytety[:srodkowy]

            # updejtujemy liczniki
            srodkowy = round(len(uniwersytety) / 2)
            pozycja = pozycja - (len(uniwersytety) - srodkowy)

        else:
            # skracamy listę
            uniwersytety = uniwersytety[srodkowy + 1 :]

            # updejtujemy liczniki
            srodkowy = round(len(uniwersytety) / 2)
            pozycja = pozycja + srodkowy + 1


if __name__ == "__main__":
    main()
