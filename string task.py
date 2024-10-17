name=" JOhn  ."
print(name.strip())
print(name.lower().strip().replace("."," "))



sentence_one= "The Dog Breed is German Shepherd" 
print(sentence_one[8:23])
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

sentence_three="The lazy dog; ran so fast; it hit the wall"
print(len(sentence_three))

r='["E","W","C"]'
r=r.replace('[','').replace(']','').replace('"','').replace(',','')
print(r)

first_name=(" Joh.n")
last_name=("Do,e")
first_name=first_name.replace('.','').strip()
last_name=last_name.replace(',','')

full_name=first_name+" "+last_name
print(full_name)