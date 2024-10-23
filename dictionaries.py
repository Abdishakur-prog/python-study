person={
    'name':'kevin',
    'age' :25,
    'gender':'male',
    'location':["nairobi",518,'thika'],
    'address':{
       "country":"kenya",
       "city":"nairobi",
       "street":"muthaiga"
    }
}
print(type(person))
print(person['name'])
print(person['gender'])
print(person['age'])
print(person['location'][2])
print(person['address']['country'])
print(person['address']['city'])
print(person['address']['street'])

person['age']=30
print(person)

person['location'][0]='garissa'
print(person)

person['occupation']='doctor'
print(person)


#dictionaries methods

print(person.keys())

print(person.values())

print(person.items())

person.pop("occupation")
print(person)






#my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]
#my_ds=my_ds[3][2]["currency"]
#print(my_ds)







