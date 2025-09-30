# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Print de dictionary-waarde gekoppeld aan onderstaande variabele

# Niveau 1
fruit = "banaan"
print( fruitmand[fruit] )


# Niveau 2
nieuw_fruit  = "mango"
nieuw_aantal = 1

fruitmand[nieuw_fruit] = nieuw_aantal
#rint(fruitmand)

# Niveau 3
fruit = "banaan"
#nieuw_aantal = 8
#fruitmand["banaan"] = nieuw_aantal
#print(fruitmand)

# Niveau 4
fruit = "kers"
#nieuw_aantal = 43
#fruitmand["kers"] = fruitmand["kers"] - nieuw_aantal # Waarde van element verhogen
#print(fruitmand)

# Niveau 5
terugleggen_fruit = "kers"
fruitmand.pop("kers")
print(fruitmand)
