prices = {
    "banana" : 4,
    'appele' : 2,
    'orange' : 1.5,
    'pear' : 3
    }
stock = {
    "banana" : 6,
    'appele' : 0,
    'orange' : 32,
    'pear' : 15
    }
print('In my store:')
print()
def print_info(fruit):
    print(fruit)
    print('price :',prices[fruit])
    print('stock :',stock[fruit])
total = 0
for key in prices:
    print_info(key)
    print()
    total = total + stock[key]*prices[key]
print('If we sold out all of them, we can earn toatlly is:',total) 
