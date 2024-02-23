spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names=[]
    count = 0
    while count < len(spicy_foods): 
        food_names.append(spicy_foods[count]["name"])
        count += 1
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_food_list = []
    count = 0
    while count < len(spicy_foods):
        if spicy_foods[count]["heat_level"] > 5:
            spiciest_food_list.append(spicy_foods[count])
        count += 1
    return spiciest_food_list

def print_spicy_foods(spicy_foods):
    count = 0
    while count <len(spicy_foods):
        print(
            spicy_foods[count]["name"] 
            + " ("
            + spicy_foods[count]["cuisine"]
            + ") | Heat Level: " 
            + "🌶" * spicy_foods[count]["heat_level"]
        )
        count += 1

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    count = 0 
    while count < len(spicy_foods):
        if spicy_foods[count]["cuisine"] == cuisine:
            selected_food = spicy_foods[count]
        count += 1
    return selected_food  

def print_spiciest_foods(spicy_foods):
    count = 0 
    while count < len(spicy_foods):
        if spicy_foods[count]["heat_level"] > 5:
            print(
                spicy_foods[count]["name"]
                + " ("
                + spicy_foods[count]["cuisine"]
                + ") | Heat Level: "
                + "🌶" * spicy_foods[count]["heat_level"]
            )
        count += 1

def get_average_heat_level(spicy_foods):
    count = 0 
    total_heat = 0
    average_heat = 0
    while count < len(spicy_foods):
        total_heat += spicy_foods[count]["heat_level"]
        count += 1
    average_heat = total_heat / len(spicy_foods)
    print(int(average_heat))
    return int(average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
