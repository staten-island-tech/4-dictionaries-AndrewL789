#ratings r outta 10
yang=[
{
    'name':'Xiyang Statue',
    'price':129.99,
    'ratings':8,
    'desc':'A glorious fully aluminum statue of Xiyang',
    'count':0
},
{

    'name':'Xiyang Door Knob',
    'price':5.99,
    'ratings':10,
    'desc':'A brass door knob hand carved into the shape of Xiyangs head',
    'count':0
},
{
    'name':'Xiyang TV Remote',
    'price':4.99,
    'ratings':4,
    'desc':'A tv remote in the shape of Xiyangs head (batteries not included)',
    'count':0
},
{
    'name':'Xiyang Soap Holder',
    'price':11.99,
    'ratings':10,
    'desc':'A plastic carve out of Xiyang with a compartment to store bars of soap',
    'count':0
},
{
    'name':'Xiyang calf shaped moniter',
    'price':3299.99,
    'ratings':10,
    'desc':"A high end monitor for professional buiness pruposes, just in the shape of a 2000% magnification of Xiyang's left calf",
    'count':0 

}

]

print('In the Xiyang store we have:')
for index, xi in enumerate(yang):
    print(index, ":", xi['name'])

""" ti = int(input("what item would you like to buy? Please input the index number :"))

print(f" you have bought a {yang[ti]['name']} for {yang[ti]['price']}!!! ")
 """


# second half, make a cart

cart = [] 
total = []
done = False

while done == False:
    ti = (input('please input the index num of what you wanna add to your cart :')) 
    item = yang[int(ti)]['name']
    cart.append(item)
    price = yang[int(ti)]['price']
    total.append(price) 
    yang[int(ti)]['count'] += 1 
    contin = input("ya wanna add more? (y/n) :")
    if contin == 'n':
        done = True
        for xi in yang:
            if xi['count'] > 0:
                print(f"you have bought {xi['name']} x{xi['count']}")      
        print(f"your total is ${sum(total)}")
            
    elif contin == 'y':
        done = False
    
    