inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylyphone', 'dagger', 'bedroll', 'bread loaf']
    }
inventory['poket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50
for key, value in inventory.items():
    print('{0} : {1}'.format(key,value)) 
 
