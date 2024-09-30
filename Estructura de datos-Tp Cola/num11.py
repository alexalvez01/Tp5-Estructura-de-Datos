from cola import Queue


star_wars_characters = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Princess Leia Organa", "planet": "Alderaan"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Darth Vader", "planet": "Tatooine"},
    {"name": "Obi-Wan Kenobi", "planet": "Stewjon"},
    {"name": "Yoda", "planet": "Unknown"},
    {"name": "Chewbacca", "planet": "Kashyyyk"},
    {"name": "R2-D2", "planet": "Naboo"},
    {"name": "C-3PO", "planet": "Tatooine"},
    {"name": "Anakin Skywalker", "planet": "Tatooine"},
    {"name": "Padmé Amidala", "planet": "Naboo"},
    {"name": "Jar Jar Binks","planet": "Naboo"},
    {"name": "Qui-Gon Jinn", "planet": "Coruscant"},
    {"name": "Mace Windu", "planet": "Haruun Kal"},
    {"name": "Darth Maul", "planet": "Dathomir"},
    {"name": "Rey", "planet": "Jakku"},
    {"name": "Finn", "planet": "Unknown"},
    {"name": "Poe Dameron", "planet": "Yavin 4"},
    {"name": "Kylo Ren", "planet": "Chandrila"}
]

cola_char= Queue()

for i in range(len(star_wars_characters)):
    cola_char.arrive(star_wars_characters[i])

for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()
    
    
    
for i in range(cola_char.size()):
    if (cola_char.on_front()["planet"] == "Alderaan" or cola_char.on_front()["planet"] == "Endor" or cola_char.on_front()["planet"] == "Tatooine" ):
        print("-Los personajes del planeta Alderaan, Endor y Tatooine son:")
        print(cola_char.on_front())
        
    cola_char.move_to_end()
    
    
for i in range(cola_char.size()):
    if (cola_char.on_front()["name"] == "Luke Skywalker" ):
        print(f'-El planeta natal de Luke Skywalker es {cola_char.on_front()["planet"]}')
    if (cola_char.on_front()["name"] == "Han Solo" ):
        print(f'-El planeta natal de LHan Solo es {cola_char.on_front()["planet"]}')

        
    cola_char.move_to_end()
    
temp_cola=Queue()

new_character = {"name": "Ahsoka Tano", "planet": "Shili"}

found_yoda = False

for i in range(cola_char.size()):
    current_character = cola_char.on_front()  
    
    if current_character["name"] == "Yoda" and not found_yoda:
       
        temp_cola.arrive(new_character)
        found_yoda = True

    
    temp_cola.arrive(current_character)
    
    
    cola_char.move_to_end()


for i in range(cola_char.size()):
    cola_char.attention()
    
for i in range(temp_cola.size()):
    cola_char.arrive(temp_cola.on_front())
    temp_cola.move_to_end()

print("---Agregando un nuevo personaje adelante de Yoda:")
for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()
    

found_Jar_Jar_Binks= False

for i in range(temp_cola.size()):
    temp_cola.attention()

for i in range(cola_char.size()):
    current_character = cola_char.on_front()  
    
    if current_character["name"] == "Jar Jar Binks" and not found_Jar_Jar_Binks:
            found_Jar_Jar_Binks = True
        
    
    if found_Jar_Jar_Binks:
            cola_char.attention()
            found_Jar_Jar_Binks= False

    
    temp_cola.arrive(current_character)
    
    
    cola_char.move_to_end()

for i in range(cola_char.size()):
    cola_char.attention()
    
for i in range(temp_cola.size()):
    cola_char.arrive(temp_cola.on_front())
    temp_cola.move_to_end()
    
print("---Eliminando el personaje ubicado despues de Jar Jar Binks:")
for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()
    