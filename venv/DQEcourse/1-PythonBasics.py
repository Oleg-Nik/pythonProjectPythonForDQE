#
import random

# define length of the list
dieLaenge = 100
# define the Depth of probability
WahrscheinlichkeitTiefe = 1000
# create list with sequence 1, 2, ..., length in it
dieListe = list(range(0, dieLaenge))
# create auxiliary list for ordering in cycle
dieReihenfolge = list(range(0, dieLaenge))
# create/define dummy list for sorted list
sortierteListe = list(range(0, dieLaenge))
# form list with random number
for i in dieReihenfolge:
    dieListe[i] = random.randrange(0, WahrscheinlichkeitTiefe)
# an output for random list
print("------->: unsorted random List:")
print(dieListe)
print("------->sorted random List:")
#sorting the List
Tiefstwert = 0
Maximalwert = WahrscheinlichkeitTiefe
j = 0
while j < dieLaenge:
    Tiefstwert = min(dieListe)
    sortierteListe[j] = Tiefstwert
    dieListe.remove(Tiefstwert)
    j = j + 1

# sum of even
geradzahlige = 0
# sum of odd
ungerade = 0

# calculation of sums for even and odd numbers
k = 0
while k < dieLaenge:
    if sortierteListe[k] % 2 == 0:
        geradzahlige = geradzahlige + sortierteListe[k]
    if sortierteListe[k] % 2 == 1:
        ungerade = ungerade + sortierteListe[k]
    k = k + 1

print(sortierteListe)

print("The sum of even numbers:")
print(geradzahlige)
print("The sum of odd numbers:")
print(ungerade)