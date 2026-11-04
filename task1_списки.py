numbers = [10, 20, 30, 40, 50, 60]

print("Початковий список:", numbers)

print("Елемент за індексом 1:", numbers[1])
print("Останній елемент:", numbers[-1])

print("Зріз 1:", numbers[1:5])
print("Зріз 2:", numbers[::2])
print("Зріз 3:", numbers[::-1])

numbers.append(70)
print("Після додавання:", numbers)

numbers.pop(0)
print("Після видалення:", numbers)
