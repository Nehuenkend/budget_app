# creamos la clase "Category"


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # definimos "deposit" para ingresar un presupuesto

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # definimos "withdraw" para retirar dinero, comprobamos antes que halla fondos

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # definimos "get_balance" que devuelve el presupuesto actual

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    # definimos "transfer" para mover el dinero entre dos categorias distintas

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # definimos "check_funds" que devuelve un booleano (f o v) dependiendo si hay fondos suficientes para cubrir la cantidad ingresada

    def check_funds(self, amount):
        return amount <= self.get_balance()

    # armamos una representacion para la categoria

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:<23}"
            amount = f"{item['amount']:.2f}"
            items += f"{description}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# definimos una funcion que devuelve los porcentajes gastados por categoria


def create_spend_chart(categories):
    total_spent = 0
    category_spending = []

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        total_spent += spent
        category_spending.append((category.name, spent))

    percentages = [
        (name, int(spent / total_spent * 100 // 10) * 10)
        for name, spent in category_spending
    ]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for _, percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")


# EJEMPLO DE USO:

food = Category("Alimentación")
clothing = Category("Ropa")
entertainment = Category("Ocio")

food.deposit(1000, "Depósito inicial")
food.withdraw(150.75, "Compra supermercado")
clothing.deposit(500)
clothing.withdraw(200, "Zapatos")
entertainment.deposit(300)
entertainment.withdraw(120, "Cine")

food.transfer(50, entertainment)

print(food)
print()
print(create_spend_chart([food, clothing, entertainment]))
