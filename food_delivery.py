number_of_chicken_meals = int(input())
number_of_fish_meals = int(input())
number_of_vegan_meals = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery_price = 2.50

chicken_menu_price = number_of_chicken_meals * chicken_menu
fish_menu_price = number_of_fish_meals * fish_menu
vegan_menu_price = number_of_vegan_meals * vegan_menu

total_menu_price = chicken_menu_price + fish_menu_price + vegan_menu_price

dessert_price = total_menu_price * 0.2

final_bill = total_menu_price + dessert_price + delivery_price
print(final_bill)
