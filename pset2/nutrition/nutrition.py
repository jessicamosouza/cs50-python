fruits_cal_dict = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 80,
        "Orange": 50,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }


def main():
    fruit = input('Item: ').title()
    check_calorie(fruits_cal_dict, fruit)


def check_calorie(fruits_cal_dict, fruit):
    if fruit in fruits_cal_dict:
        print('Calories:', fruits_cal_dict[fruit])


main()
