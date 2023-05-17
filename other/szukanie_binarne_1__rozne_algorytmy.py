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

    # 0 - metoda index
    miejsce = uniwersytety.index(szukany) + 1
    print(f"#0 Jest na {miejsce} miejscu.")

    # 1 - szukanie po kolei (algorytm liniowy):
    miejsce = 1
    for _ in uniwersytety:
        if _ == szukany:
            print(f"#1 Jest na {miejsce} miejscu.")
            break
        miejsce += 1

    # 2 - szukanie przy pomocy dzielenia na połowy (algorytm binarny).
    # Szukamy wyrazu najbliżej środka stawki. Sprawdzamy go.

    srodkowy = 0  # inicjuję dowolną cyfrą, na potrzeby rozruchu pętli

    while len(uniwersytety) > 0:
        srodkowy = srodek_listy(uniwersytety, srodkowy)

        # - jeśli szukany == środkowy, ogłoś sukces
        if szukany == uniwersytety[srodkowy]:
            print(f"#2 Znalazłem {szukany}!")
            break

        # - jeśli szukany < środkowy, skróć listę do pierwszej połowy
        elif szukany < uniwersytety[srodkowy]:
            print(f"#2 {szukany} jest w pierwszej części listy:")
            uniwersytety = uniwersytety[0:srodkowy]
            print(uniwersytety)

        # - jeśli szukany > środkowy, skróć listę do drugiej połowy
        else:
            print(f"#2 {szukany} jest w drugiej części listy:")
            uniwersytety = uniwersytety[srodkowy + 1 : len(uniwersytety)]
            print(uniwersytety)

    print()


def srodek_listy(uniwersytety, srodkowy):
    # Zmierz długość listy. Podziel na pół. Zaokrąglij do int.
    # Round zaokrągla do liczb parzystych, unikając kumulowania się błędów zaokrągleń.
    srodkowy = round(len(uniwersytety) / 2)
    print(f"\n#2 Środek jest w {uniwersytety[srodkowy]}")
    return srodkowy


if __name__ == "__main__":
    main()

# możesz teraz usunąć nadmiarowe printy, zlikwidować funkcję i porównać czas działania algorytmów
