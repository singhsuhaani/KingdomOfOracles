# Kingdom of Oracles Nested Dictionaries - Suhaani Singh
# Defines nested dictionaries for characters, their inventories,
# and locations, and then prints each property/descp in a
# clear and organized format


characters = {                                                                       # defines dict for char roles + properties
    'commoner': {                                                                    # role type 1 
        'age': 22,                                                                   # character’s age
        'quirk': 'can read minds'                                                    # special ability
    },
    'knight': {                                                                      # role type 2
        'age': 26, 
        'quirk': 'can run fast'
    },
    'royalty': {                                                                     # role type 3 
        'age': 24, 
        'quirk': 'can win over people/please the crowd'
    }
}

inventory = {                                                                        # defines dict for char's inv + descp 
    'commoner': {
        'axe': {
            'description': "sturdy for woodcutting",                                 # item description
            'damage': 5                                                              # damage it causes out of 20
        },
        'wagon': {
            'description': 'a small wooden wagon',
            'capacity': 40                                                           # capacity out of 100
        },
        'cattle': {
            'description': 'a pair of oxen for transport',
            'health': 80                                                             # health/endurance out of 100
        },
        'coin pouch': {
            'description': 'leather pouch with coins',
            'value': 50                                                              # monetary value in present economy
        }
    },
    'knight': {
        'horse': {
            'description': 'a strong horse; used in war',                            # description
            'speed': 7                                                               # speed out of 10 
        },
        'sword': {
            'description': 'a long steel sword with gold accents',
            'damage': 17                                                             # damage out of 20
        },
        'armour': {
            'description': 'shining plate armour',
            'defense': 20                                                            # defense out of 20
        }
    },
    'royalty': {
        'crown': {
            'description': 'jeweled gold crown', 
            'value': 1000000                                                         # monetery value in present economy
        },
        'books': {
            'description': 'wisdom and advice passed on from generations',  
            'knowledge': 8                                                           # knowledge out of 10
        },
        'gloves': {
            'description': 'brown, thick leather gloves',
            'defense': 5                                                             # defense out of 20 
        }
    }
}

locations = {                                                                        # defines dict for location + qualities 
    'mountain': {
        'description': 'steep, forest hills with hidden caves',                      # descp 
        'advantage': 'high ground for visibility',                                   # environmental benefit
        'disadvantage': 'harsh weather conditions'                                   # environmental drawback
    },
    'desert': {
        'description': 'sand wonderland under a blazing sun',
        'advantage': 'vast open spaces',
        'disadvantage': 'scarcity of water'
    },
    'island': {
        'description': 'lush palm trees surrounded by a glistening sea',  
        'advantage': 'surrounded by water for defense',
        'disadvantage': 'limited resources'
    }
}

for name, details in characters.items():                                             # loops for each character role
    print(f"\n{name.title()} age is {details['age']}")                               # prints char role + age
    print(f"{name.title()} quirk is {details['quirk']}")                             # print cahr role + quirk

for location, details in locations.items():                                          # loops for each location
    print(f"\n{location.title()} is {details['description']}")                       # prints desc of each location
    print(f"{location.title()} advantage is {details['advantage']}")                 # prints advantage
    print(f"{location.title()} disadvantage is {details['disadvantage']}")           # prints disadvantage

for char, items in inventory.items():                                                # loops each char role 
    print(f"\n{char.title()}'s inventory:")                                          # header for char's inventory list
    for item, details in items.items():                                              # loops each item in char's inventory
        print(f"* {item.title()}")                                                   # item name with asterisk
        for details, value in details.items():                                       # loops stat of each item of each char
            print(f"    {details.title()}: {value}")                                 # prints descp and value with indentation

