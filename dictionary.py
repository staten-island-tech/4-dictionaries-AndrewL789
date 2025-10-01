#ratings r outta 5 
yang= [
{
    df
    'name':'Xiyang Statue',
    'price':'129.99',
    'ratings':'8',
    'desc':'A glorious fully aluminum statue of Xiyang'

    },
{

    'name':'Xiyang door knob',
    'price':'5.99',
    'ratings':'10',
    'desc':'A brass door knob hand carved into the shape of Xiyangs head'
    },
{
    'name':'Xiyang tv remote',
    'price':'4.99',
    'ratings':'4',
    'desc':'A tv remote in the shape of Xiyangs head (batteries not included)'
    },
{
    'name':'Xiyang tapistry'
    'price':'34.99',
    'ratings':'9',
    'desc':'High quality silk tapistry of Xiyang posing dramatically'
    },
{
    'name':'Xiyang soap holder',
    'price':'11.99',
    'ratings':'10',
    'desc':'A plastic carve out of Xiyang with a compartment to store bars of soap'
},
    ]


for xi in yang:
    xi['price'] = float(xi['price'])
    xi['ratings'] = int(xi['ratings'])


print(yang['name'])