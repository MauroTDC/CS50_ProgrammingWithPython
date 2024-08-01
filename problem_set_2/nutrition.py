def main():
    fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grape": 90,
    "honeydew": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
    item = input("Item: ")
    print(get_calories(item, fruits))


def get_calories(fruit: str, fruits: dict):
    fruit = fruit.lower().strip()
    if fruit in fruits:
        return f"Calories: {fruits[fruit]}"
    else:
        return None


if __name__ == "__main__":
    main()