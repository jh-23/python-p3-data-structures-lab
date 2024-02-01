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
    food_list = []
    for food in spicy_foods:
        food_list.append(food['name'])
    return food_list

def get_spiciest_foods(spicy_foods):
    heat_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_list.append(food)
    return heat_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None 

def print_spiciest_foods(spicy_foods):
        for food in spicy_foods:
            heat_level = "🌶" * food['heat_level']
            if food['heat_level'] > 5:
                print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
        return spicy_foods

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)
    
    for food in spicy_foods:
        total_heat_level += food['heat_level']
        average_heat = total_heat_level/num_foods
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
