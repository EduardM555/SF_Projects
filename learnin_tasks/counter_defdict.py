from collections import Counter
from collections import defaultdict

c = Counter()

print(c)

c['red'] += 1
print(c)

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter()
for car in cars:
    c[car] += 1
print(c)

c = Counter(cars)
print(c['red'])

print(c.values())

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(counter_moscow + counter_spb)
print(counter_moscow.subtract(counter_spb))
print(counter_moscow)

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(counter_moscow - counter_spb)

print(counter_moscow)
print(*counter_moscow.elements())
print(*counter_moscow.values())
print(*counter_moscow.keys())
print(list(counter_moscow.keys()))
print(list(counter_moscow))

print(counter_moscow.most_common(1))

counter_moscow.clear()
print(counter_moscow)


students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

groups = dict()
q = []

for student, group in students:
    if group not in groups:
        groups[group] = list()
    groups[group].append(student)

print(groups)

groups = defaultdict(list)
# print(groups)

for student, group in students:
    groups[group].append(student)
    
print(groups)

print(groups[1])


