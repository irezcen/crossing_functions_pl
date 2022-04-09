import matplotlib.pyplot as plt
import math


def menu():
    wyboropcji = input()
    if wyboropcji == 'funkcja':
        menufunkcji()
    elif wyboropcji == 'koniec':
        koniec()
    else:
        print('nieznana opcja ', wyboropcji, ', spróbuj jeszcze raz')
        interfejs()


def interfejs():
    print('Wyświetlanie przebiegu funkkcji --> \"funkcja\"')
    print('zamknij program --> \"koniec\"')
    menu()


def tylkoliczby(a):
    try:
        numer = float(a)
        return numer
    except ValueError:
        print('podaj numer!')
        menufunkcji()


def menufunkcji():

    a = tylkoliczby(input('podaj parametr a funkcji pierwszej: '))
    b = tylkoliczby(input('podaj parametr b funkcji pierwszej: '))
    c = tylkoliczby(input('podaj paramter c funkcji pierwszej: '))
    aj = tylkoliczby(input('podaj parametr a funkcji drugiej: '))
    bj = tylkoliczby(input('podaj parametr b funkcji drugiej: '))
    cj = tylkoliczby(input('podaj parametr c funkcji drugiej: '))
    kropki(obliczaniezer(a, b, c, aj, bj, cj), a, b, c)
    wyswdwochfunkcji(a, b, c, aj, bj, cj)
    zatwierdz()


def zatwierdz():
    print('wróć do menu głównego --> \"menu\"')
    print('zamknij program --> \"koniec\"')
    wyboropcji = input()
    if wyboropcji == 'menu':
        interfejs()
    elif wyboropcji == 'koniec':
        koniec()
    else:
        print('nieznana opcja ', wyboropcji, ', spróbuj jeszcze raz')
        zatwierdz()


def wyswdwochfunkcji(a, b, c, aj, bj, cj):
    z = []
    y = []
    poz = []
    for x in range(-100000, 100000):
        z.append(x/10000)
    for x in range(0, 200000):
        y.append(a*z[x]**2 + b * z[x] + c)
        poz.append(aj * z[x] ** 2 + bj * z[x] + cj)
    plt.plot(z, y, 'r--', z, poz, 'bs')
    plt.show()


def koniec():
    if 1 == 1:
        print('')
        exit(1)


def obliczaniezer(a, b, c, aj, bj, cj):
    zera = []
    parama = a - aj
    paramb = b - bj
    paramc = c - cj
    if paramb**2 - 4 * parama * paramc == 0:
        if parama == 0 and paramb == 0 and paramc == 0:
            print('funkcje mają nieskończenie wiele miejsc wspólnych')
            for i in range(0, 3):   # kod na nieskończenie wiele miejsc
                zera.append(0)      # kod na nieskończenie wiele miejsc
            return zera             # kod na nieskończenie wiele miejsc
        elif paramc != 0:
            print('funkcje się nie przecinają')
            for i in range(0, 4):   # kod na brak miejsc wspólnych
                zera.append(0)      # kod na brak miejsc wspólnych
            return zera             # kod na brak miejsc wspólnych
        else:
            print('funkcje przecinają się jeden raz')
            zera.append(paramb/2 * parama)
            rozmiarosi(zera, a, b, c)
        return zera
    elif paramb**2 - 4 * parama * paramc > 0:
        if parama == 0:
            if paramb == 0 and paramc == 0:
                print('funkcje mają nieskończenie wiele miejsc wspólnych')
                for i in range(0, 3):   # kod na nieskończenie wiele miejsc
                    zera.append(0)      # kod na nieskończenie wiele miejsc
                return zera             # kod na nieskończenie wiele miejsc
            elif paramb == 0:
                print('funkcje się nie przecinają')
                for i in range(0, 4):   # kod na brak miejsc wspólnych
                    zera.append(0)      # kod na brak miejsc wspólnych
                return zera             # kod na brak miejsc wspólnych
            print('funkcje przecinają się jeden raz')
            zera.append(paramc/paramb)
            rozmiarosi(zera, a, b, c)
            return zera
        xjeden = (-paramb + math.sqrt(paramb**2 - 4 * parama * paramc))/(2 * parama)
        xdwa = (-paramb - math.sqrt(paramb**2 - 4 * parama * paramc))/(2 * parama)
        if xjeden < xdwa:
            zera.append(xjeden)
            zera.append(xdwa)
        else:
            zera.append(xdwa)
            zera.append(xjeden)
        print(xjeden)
        print(xdwa)
        rozmiarosi(zera, a, b, c)
        print('funkcje przecinają się dwa razy')
        return zera
    else:
        print('funkcje się nie przecinają')
        return


def kropki(x, a, b, c):
    yj = []
    if len(x) == 2:
        xj = x
        yj.append(a * x[0] ** 2 + b * x[0] + c)
        yj.append(a * x[-1] ** 2 + b * x[-1] + c)
        plt.scatter(xj, yj, s=20**2,)
        return
    elif len(x) == 1:
        yj.append(a * x[0] ** 2 + b * x[0] + c)
        plt.scatter(x, yj, s=20**2)
        return
    elif len(x) == 3:
        return
    elif len(x) == 4:
        return


def start():
    print('Witaj, w czym mogę pomóc?')
    while 1 == 1:
        interfejs()


def rozmiarosi(zera, a, b, c):
    plt.axis([(zera[0] - 3), (zera[-1] + 3), (a * zera[0] ** 2 + b * zera[0] + c - 3),
              (a * zera[-1] ** 2 + b * zera[-1] + c + 3)])


start()
