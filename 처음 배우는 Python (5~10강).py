list_1 = ["a", "B", "C"]
list_2 = list_1
list_3 = list_2
list_1 = ["b", "c", "d"]
list_2.append(3)
print((list_1))

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1[1:3]
list_1 = list_1[2:]
list_3 = list_2[0:] + list_2
print(list_3)

planets = []
f = open('planets.txt','r')
for line in f:
    planets.append(line.strip())
f.close()
print(planets)

f = open('planets.txt','r')
current = 0
earth = 0
for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == 'earth':
        earth = current
print('Earth is planet #%d' %earth)

a=0
for x in range(3):
    while a > 0:
        a += 1
        if a > 5:
            break
    a += 1
print(a)

cards = []
for i in range(4):
    card = Card()
card.value = i
cards.append(card)
print(cards[1].value)