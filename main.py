
orders = ["Піцца", "Салат", "Бургер", "Паста"]
print("Початкові замовлення:", orders)

orders.append("Суп")
print("Після додавання супу:", orders)

del orders[1]
print("Після видалення з індексом 1:", orders)

print("Зріз елементів з 1 по 3:", orders[1:4])


categories = ("Напої", "Супи", "Основні страви", "Десерти")
print("\nКатегорії страв:", categories)
print("Категорія з індексом 2:", categories[2])


available_ingredients = {"помідор", "огірок", "сир", "шинка", "салат"}
print("\nНаявні інгредієнти:", available_ingredients)

available_ingredients.add("базилік")
print("Після додавання базиліку:", available_ingredients)

required_ingredients = {"помідор", "огірок", "олія", "часник"}
common = available_ingredients & required_ingredients
missing = required_ingredients - available_ingredients

print("Спільні інгредієнти:", common)
print("Відсутні інгредієнти:", missing)


menu = {"Піцца": 120, "Салат": 80, "Бургер": 100, "Паста": 110}
print("\nМеню:", menu)

menu["Суп"] = 90
print("Після додавання Супу:", menu)

menu["Бургер"] = 105
print("Після зміни ціни Бургера:", menu)

del menu["Салат"]
print("Після видалення Салату:", menu)

order_list = ["Піцца", "Бургер", "Суп"]
total_price = sum(menu[item] for item in order_list)
print("Загальна вартість замовлення (Піцца, Бургер, Суп):", total_price)
