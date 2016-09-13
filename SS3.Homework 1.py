#1
colors=['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
#1.1
print('1.1 My color list:',colors)
#1.2
print('1.2 Color_list at index :',colors[3])
#1.3
i = int(input('1.3 Enter a number from 0-5: '))
print('Your color:',colors[i])
#1.4
print('1.4 Row: ', colors)
print('Column:')
for color in colors:
    print(color)
#1.5
x = input("1.5 What is your favorite color? ")
for i in range(len(colors)):
    if colors[i]==x:
        print('Your color is at index',i,'in my list')
        k = True
        break
    else:
        k = False
if not k:
    print('Sorry, I could not find your color')
