from cola import Queue  
mcu_characters = [
    {"real_name": "Tony Stark", "superhero_name": "Iron Man", "gender": "M"},
    {"real_name": "Steve Rogers", "superhero_name": "Captain America", "gender": "M"},
    {"real_name": "Natasha Romanoff", "superhero_name": "Black Widow", "gender": "F"},
    {"real_name": "Bruce Banner", "superhero_name": "Hulk", "gender": "M"},
    {"real_name": "Thor Odinson", "superhero_name": "Thor", "gender": "M"},
    {"real_name": "Clint Barton", "superhero_name": "Hawkeye", "gender": "M"},
    {"real_name": "Carol Danvers", "superhero_name": "Captain Marvel", "gender": "F"},
    {"real_name": "Peter Parker", "superhero_name": "Spider-Man", "gender": "M"},
    {"real_name": "T'Challa", "superhero_name": "Black Panther", "gender": "M"},
    {"real_name": "Wanda Maximoff", "superhero_name": "Scarlet Witch", "gender": "F"},
    {"real_name": "Stephen Strange", "superhero_name": "Doctor Strange", "gender": "M"},
    {"real_name": "Scott Lang", "superhero_name": "Ant-Man", "gender": "M"},
    {"real_name": "Hope van Dyne", "superhero_name": "The Wasp", "gender": "F"},
    {"real_name": "Sam Wilson", "superhero_name": "Falcon", "gender": "M"},
    {"real_name": "Bucky Barnes", "superhero_name": "Winter Soldier", "gender": "M"},
    {"real_name": "Shuri", "superhero_name": "Shuri", "gender": "F"},
    {"real_name": "Peter Quill", "superhero_name": "Star-Lord", "gender": "M"},
    {"real_name": "Gamora", "superhero_name": "Gamora", "gender": "F"},
    {"real_name": "Nebula", "superhero_name": "Nebula", "gender": "F"},
    {"real_name": "Drax", "superhero_name": "Drax the Destroyer", "gender": "M"},
    {"real_name": "Rocket", "superhero_name": "Rocket Raccoon", "gender": "M"},
    {"real_name": "Groot", "superhero_name": "Groot", "gender": "M"}
]

cola_char= Queue()
fem_char=Queue()
masc_char= Queue()
s_char= Queue()
carol_danvers= False


for i in range(len(mcu_characters)):
    cola_char.arrive(mcu_characters[i])
     
for i in range(cola_char.size()):
    current_character= cola_char.on_front()
    
    if current_character["superhero_name"] == "Captain Marvel":
        print(f'El nombre del personaje de Capitana Marvel es: {current_character["real_name"]}')
    
    if current_character["gender"]=="F":
        fem_char.arrive(current_character["superhero_name"])
    else:
        masc_char.arrive(current_character["real_name"])
    
    if current_character["real_name"]=="Scott Lang":
        print(f'El nombre del superheroe de Scott Lang es: {current_character["superhero_name"]}')
        
    if current_character["real_name"].startswith("S") or current_character["superhero_name"].startswith("S"):
        s_char.arrive(current_character)
    
    if current_character["real_name"]== "Carol Danvers":
        carol_danvers= True
        carol_char=current_character
        
    
    cola_char.move_to_end()

print("---Los nombres de los superheroes femeninos son:")

for i in range(fem_char.size()):
    print(fem_char.on_front())
    fem_char.move_to_end()
    
print("---Los nombres de los personajes masculinos son:")

for i in range(masc_char.size()):
    print(masc_char.on_front())
    masc_char.move_to_end()


print("---Los personajes o superheroes que empiezan por S son:")

for i in range(s_char.size()):
    print(s_char.on_front())
    s_char.move_to_end()

if carol_danvers:
    print(f"""El personaje Carol Danvers se encuentra en la cola y sus datos son: 
          -Nombre real: {carol_char["real_name"]}, 
          -Nombre de superheroe: {carol_char["superhero_name"]}, 
          -Genero: {carol_char["gender"]}""")
else:
    print("El personaje Carol Danvers no se encuentra en la cola")