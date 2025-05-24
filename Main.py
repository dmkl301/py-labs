def orders():
    order_list = ["Піцца", "Салат", "Бургер", "Паста"]
    order_list.append("Суп")
    order_list.remove(order_list[1])
    return order_list[1:3]
print(f"Список замовлень - {orders()}")

def categories():
    dishes_categories = ("Напої", "Супи", "Основні страви", "Десерти")
    return dishes_categories[2]
print(f"Другий індекс категорій - {categories()}")

def ingredients():
    ingredients_list = {"помідор", "огірок", "сир", "шинка", "салат"}
    ingredients_list.add("базилік")
    recipe = {"помідор", "огірок", "олія", "часник"}
    recipe.intersection(ingredients_list)
    recipe.difference(ingredients_list)
    return recipe
print(f"Інградієнти - {ingredients()}")

def dishes_price():
    menu = {"Піцца": 120, "Салат": 80, "Бургер": 100, "Паста": 110}
    menu["Суп"] = 90
    menu["Бургер"] = 105
    menu.pop("Салат")
    order = ["Піцца", " Бургер", "Суп"]
    order_bill = sum(menu.get(order_sum, 0) for order_sum in order)
    return order_bill
print(f"Рахунок замовлення - {dishes_price()}")