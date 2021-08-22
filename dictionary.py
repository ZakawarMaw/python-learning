person = {
    'name' : 'Zakawar',
    'age'  : 20
};

#add new data in Person Dictionary
person['hair_color']="black";


#Using (In) Keyword 
if 'job' in person :
    print('Work');

#Person Key Convert To List
person_keys=list(person.keys());
print(person_keys);   


#Person value Convert To List
person_values=list(person.values());
print(person_values);    



