#
import random

# define length of the list
dieLaenge = 1000
# create list with 1, 2, ..., length in it
dieListe = list(range(0, dieLaenge))
# create auxiliary list for cycle
dieReihenfolge = list(range(0, dieLaenge))
# create/define dummy for sorted list
sortierteListe = list(range(0, dieLaenge))
# form list with random number
for i in dieReihenfolge:
    dieListe[i] = random.randrange(0, 1000)
# an output for random list
print("------->: unsorted random List:")
print(dieListe)
print("------->sorted random List:")
Tiefstwert = 0
Maximalwert = 1000
j = 0
while j < dieLaenge:
    Tiefstwert = min(dieListe)
    # Maximalwert = max(dieListe)
    sortierteListe[j] = Tiefstwert
    dieListe.remove(Tiefstwert)
    j = j + 1

print(sortierteListe)

# even
geradzahlige = 0
# odd
ungerade = 0

k = 0
while k < dieLaenge:
    if sortierteListe[k] % 2 == 0:
        geradzahlige = geradzahlige + sortierteListe[k]
    if sortierteListe[k] % 2 == 1:
        ungerade = ungerade + sortierteListe[k]
    k = k + 1

print(geradzahlige)
print(ungerade)