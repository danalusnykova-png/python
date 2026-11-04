products = [
    (1, "Mouse", 2, 350),
    (2, "Keyboard", 1, 900),
    (3, "USB Drive", 3, 200)
]

def unpack_product(product):
    product_id, name, quantity, price = product
    return product_id, name, quantity, price

def total_cost(items):
    total = 0
    for product in items:
        product_id, name, quantity, price = unpack_product(product)
        total += quantity * price
    return total

print("Список товарів:")
for product in products:
    print(unpack_product(product))

print("Загальна вартість:", total_cost(products), "грн")

try:
    products[0][1] = "Monitor"
except TypeError:
    print("Помилка: кортеж не можна змінювати")

student = ("Lusnykova", [8, 10])
print("Початковий кортеж:", student)

student[1].append(12)
print("Після зміни вкладеного списку:", student)
