#ratings r outta 10
yang=[
{
    'name':'Xiyang Statue',
    'price':129.99,
    'ratings':8,
    'desc':'A glorious fully aluminum scale statue of Xiyang.',
    'count':0
},
{

    'name':'Xiyang Door Knob',
    'price':5.99,
    'ratings':10,
    'desc':'A brass door knob hand carved into the shape of Xiyangs head.',
    'count':0
},
{
    'name':'Xiyang TV Remote',
    'price':4.99,
    'ratings':4,
    'desc':'A tv remote in the shape of Xiyangs head (batteries not included).',
    'count':0
},
{
    'name':'Xiyang Soap Holder',
    'price':11.99,
    'ratings':10,
    'desc':'A plastic carve out of Xiyang with a compartment to store bars of soap.',
    'count':0
},
{
    'name':'Xiyang calf shaped moniter',
    'price':3299.99,
    'ratings':10,
    'desc':"A high end monitor for professional buiness pruposes, just in the shape of a 2000% magnification of Xiyang's left calf.",
    'count':0 
},
{
    'name':"The Yang Cam",
    'price':149.99,
    'ratings':100,
    'desc':"You've already seen the magestic Xiyang Statue, but now we have the Xiyang Statue ++, IT is now equipped with a 4k ultra hd ring doorbell camera, perfect for home defense.",
    'count': 0 

},
{
    'name':"Xiyang Sock set",
    'price': 12.99,
    'ratings': 6,
    'desc':"A colorful assortment of 18 different pairs of ankle socks embroided with Xiyang's face.",
    'count': 0 
},
{
    'name':'Inflatable Xiyang',
    'price': 39.99,
    'ratings' : 7,
    'desc' : "A 40 ft tall inflatable Xiyang that flails with the wind.",
    'count': 0 
},
{
    'name':'The Xiyang booster pack',
    'price':3.99,
    'ratings':2,
    'desc':"A 10 pack of Xiyang cards",
    'count':0
},
{
    'name': 'Xiyang booze',
    'price' :599.99,
    'ratings' : 8,
    'desc' : 'Xiyang booze is top grade wine, fermented for atleast 13 mil'
}
]

print('In the Xiyang store we have:')
for index, xi in enumerate(yang):
    print(index, ":", xi['name'])
# second half, make a cart

cart = [] 
total = 0
done = False
while done == False:
    ti = input('Name what you want to buy :')
    for xi in yang:
        if ti.lower() == xi['name'].lower():
            print('confirmed')
            amt = int(input("amt? :"))
            price = xi['price'] * amt
            total += price
            xi['count'] += amt 
    contin = input("ya wanna add more? (y/n) :")
    if contin == 'n':
        done = True
        for xi in yang:
            if xi['count'] > 0:
                cart.append(f" {xi['name']} x{xi['count']}")  
        print(f"you have bought {cart}")
        print(f"your total is ${round(total)}")
    elif contin == 'y':
        done = False
