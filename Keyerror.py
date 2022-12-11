
ages={"kasi":40,"lakshmi":38,"harshu":10}

age= ages.get('kasi')

print(age)

age1= ages.get('kasi1')

print(age1)

default= ages.get('kasi1',0)

print(default)

person='kasi1'
try:
    print(f'{person}, {ages[person]} age')
except KeyError:
    print(f'{person} age is unkonwn')

list =[1,3,2,4]

