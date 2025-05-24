dishes = ["Піцца", "Салат", "Бургер", "Паста", "Суп"]

ingredients = {
    "Піцца": {"помідор", "сир", "шинка", "тісто", "соус"},
    "Салат": {"огірок", "помідор", "салат", "олія", "часник"},
    "Бургер": {"булочка", "котлета", "сир", "салат", "соус"},
    "Паста": {"паста", "соус", "сир", "шинка"},
    "Суп": {"вода", "картопля", "морква", "цибуля", "м'ясо"}
}
dishes_price = {"Піцца": 120, "Салат": 80, "Бургер": 100, "Паста": 110, "Суп": 90}

order_list = ["Піцца", "Бургер"]

def make_order(order):
    order_list.append(order)

def main():
    customer_choice = input(f"Активні замовлення: {order_list}\n1 - Додати нове замовлення.\n2 - Відкрити список інградієнтів.\n")
    if customer_choice == "1":
        print(f"Список страв - {dishes_price}")
        number = input()
        print(dishes[int(number)-1] + " Додано до замовлення")
        make_order(dishes[int(number)-1])
        print(f"Активні замовлення - {order_list}")
    elif customer_choice == "2":
        print(f"Список страв - {dishes}")
        number = input()
        print(ingredients[dishes[int(number) - 1]])
main()