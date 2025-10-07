#ratings r outta 5 
yang=[
{
    'name':'Xiyang Statue',
    'price':'129.99',
    'ratings':'8',
    'desc':'A glorious fully aluminum statue of Xiyang'
},
{

    'name':'Xiyang Door Knob',
    'price':'5.99',
    'ratings':'10',
    'desc':'A brass door knob hand carved into the shape of Xiyangs head'
},
{
    'name':'Xiyang TV Remote',
    'price':'4.99',
    'ratings':'4',
    'desc':'A tv remote in the shape of Xiyangs head (batteries not included)'
},
{
    'name':'Xiyang Soap Holder',
    'price':'11.99',
    'ratings':'10',
    'desc':'A plastic carve out of Xiyang with a compartment to store bars of soap'
},

]


for xi in yang:
    xi['price'] = float(xi['price']) 
    xi['ratings'] = float(xi['ratings'])

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
    if ti == :
        done = True
        print(f"You have bought {cart}")
        print(f" your total amounts to {float(sum.total)}") 