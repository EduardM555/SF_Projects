from collections import deque

def brackets(line):
    dq = deque()
    for bracket in line:
        if bracket == '(':
            dq.append(bracket)
        elif bracket == ')':
            if len(dq) == 0:
                return False
            dq.pop()
    if len(dq) == 0:
        return True
    return False
    


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False

center = [['Milk', 'Bread'], ['Meat']]
cent = list()
for ls in center:
    for prod in ls:
        cent.append(prod)

print(cent)

center_list = [elem for bill in center for elem in bill]
south_list = [elem for bill in center for elem in bill]
north_list = [elem for bill in center for elem in bill]
print(center_list)


