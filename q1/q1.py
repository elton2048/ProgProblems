import sys
from collections import OrderedDict
for line in sys.stdin:
    pass
    #print(line, end="")
line = line.replace('\n', '')
x = line.split(';')
y = {}
x.sort(reverse=True)
for i in x:
    i = i.split('-')
    # print(i)
    y[i[0]] = i[1]
    
Orderedy = OrderedDict(sorted(y.items(), reverse=True))
correct = False

# print(Orderedy)
if "BEGIN" in Orderedy:
    nextNode = Orderedy["BEGIN"]
    for j in Orderedy:
        if(j == Orderedy.get(nextNode)):
            #print(j)
            Orderedy[nextNode] = "NULL"
            nextNode = j
            #print(nextNode)
            # print(Orderedy)
            if(Orderedy.get(nextNode) == "END"):
                correct = True
                break

if(correct):
    print("GOOD")
else:
    print("BAD")
