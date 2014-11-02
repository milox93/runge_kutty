import math
import numpy as np
import matplotlib.pyplot as plot
from progressbar import ProgressBar

pbar = ProgressBar()

Gamma = 1.0


def funkcja(x, y):
    F = np.array([[0, 1], [-1, -Gamma]])
    return np.dot(F, y)


def metoda_Eulera(x, y, krok, N):
    wynik = np.zeros(N)
    for i in range(N):
        wynik[i] = y[i] + krok * funkcja(x, y)[i]
    return wynik


def metoda_RK4(x, y, krok, N):
    wynik = np.zeros(N)
    for i in range(N):
        k1 = krok * funkcja(x, y)[i]
        k2 = krok * funkcja(x + krok / 2.0, y + (krok / 2.0) * k1)[i]
        k3 = krok * funkcja(x + krok / 2.0, y + (krok / 2.0) * k2)[i]
        k4 = krok * funkcja(x + krok / 2.0, y + krok * k3)[i]

        wynik[i] = y[i] + 1 / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    return wynik


# def pisanie_do_pliku(x, y, plik):
#	#wpisywac mozna tylko typ str, wiec zamieniam f str()
#	wpis =str(x) + " " + str(y) + "\n"
#	plik.write(wpis)

#otwieranie pliku:
#plik = open('wynik1.dat', 'w')

#liczba rownan
N = 2

#dane poczatkowe
x0 = 0.0
y0 = [0.0, 1.0]
Gamma = 0.0

#granica wyznaczenia + krok
x_k = 30.
krok = 0.001

liczba_krokow = int((x_k - x0) / krok)

#zmienne do obliczen
Y = np.zeros((liczba_krokow, N))
E = np.zeros(liczba_krokow)
error = np.zeros(liczba_krokow)
X = np.zeros(liczba_krokow)
x = x0
y = np.zeros(N)
y = y0

#czy dobrze przypisane zmienne startowe
print "Zmienne poczatkowe to ", y
#l krokow
print "Liczba krokow to ", liczba_krokow

print "Wspolczynnik hamowania to ", Gamma

for i in pbar(range(liczba_krokow)):
    #y = metoda_Eulera(x, y, krok,N)
    y = metoda_RK4(x, y, krok, N)
    X[i] = x
    Y[i, :] = y

    E[i] = (Y[i, 1] ** 2) + (Y[i, 0]) ** 2  # - math.sin(x)**2- math.cos(x)**2)/(math.sin(x)**2 + math.cos(x)**2)
    error[i] = (math.sin(x) - Y[i, 0])
    x += krok

plot.plot(X, Y[:, 0])
plot.savefig("y_x.png")

plot.clf()
plot.plot(Y[:, 0], Y[:, 1])
plot.savefig("y1_y2.png")

plot.clf()
plot.plot(X, E)
plot.savefig("energia.png")

plot.clf()
plot.plot(X, error)
plot.savefig("error.png")
