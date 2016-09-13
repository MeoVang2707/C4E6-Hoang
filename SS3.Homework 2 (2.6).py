#2.6
print('2.6')
sizes = [5,7,300,90,24,50,75]
print('\nHello, My names is Hoang and these are my ship sizes: ')
print(sizes)
size_max=sizes[0]
k=0
for i in range(len(sizes)):
    if size_max<sizes[i]:
        size_max = sizes[i]
        k = i
print('\nNow my biggest sheep has size',size_max,"let's shear it")
#2.3
sizes[k] = 8
print('After shearing, here is my flock: ')
print(sizes)
for i in range(3):
    for y in range(len(sizes)):
        sizes[y] = sizes[y] + 50
    print('\nMonth', i+1,': ')
    print('One month has passed, now here is my flock: ')
    print(sizes)
    if i==2:
        break
    size_max=sizes[0]
    k=0
    for i in range(len(sizes)):
        if size_max<sizes[i]:
            size_max = sizes[i]
            k = i
    print('Now my biggest sheep has size',size_max,"let's shear it")
    sizes[k] = 8
    print('After shearing, here is my flock: ')
    print(sizes)
sum=0
for size in sizes:
    sum = sum + size
print('\nMy flock has size in total:',sum)
print('I would get',sum,'*2$ =', sum*2,'$')

