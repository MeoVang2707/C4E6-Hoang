#2.1-2.4
sizes = [5,7,300,90,24,50,75]
#2.1
print('2.1 Hello, My names is Hoang and these are my ship sizes: ')
print(sizes)
#2.2
size_max=sizes[0]
k=0
for i in range(len(sizes)):
    if size_max<sizes[i]:
        size_max = sizes[i]
        k = i
print('\n2.2 Now my biggest sheep has size',size_max,"let's shear it")
#2.3
sizes[k] = 8
print('\n2.3 After shearing, here is my flock: ')
print(sizes)
#2.4
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print('\n2.4 One month has passed, now here is my flock: ')
print(sizes)
