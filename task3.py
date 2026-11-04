# Клас двовимірного вектора
class Вектор2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Звичайне представлення
    def __str__(self):
        return f"Вектор ({self.x}; {self.y})"

    # Представлення для програміста
    def __repr__(self):
        return f"Вектор2D({self.x}, {self.y})"

    # Додавання векторів
    def __add__(self, other):
        return Вектор2D(self.x + other.x,
                        self.y + other.y)

    # Віднімання векторів
    def __sub__(self, other):
        return Вектор2D(self.x - other.x,
                        self.y - other.y)

    # Порівняння векторів
    def __eq__(self, other):
        if not isinstance(other, Вектор2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Довжина вектора
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# Створення векторів
вектор1 = Вектор2D(3, 4)
вектор2 = Вектор2D(1, 2)

print("МАГІЧНІ МЕТОДИ PYTHON\n")

# Представлення
print("Перший вектор:", вектор1)
print("Другий вектор:", вектор2)
print("repr:", repr(вектор1))

# Арифметичні операції
print("\nАРИФМЕТИЧНІ ОПЕРАЦІЇ")

print("Додавання:", вектор1 + вектор2)
print("Віднімання:", вектор1 - вектор2)

# Порівняння
print("\nПОРІВНЯННЯ")

print("Вектори рівні:", вектор1 == вектор2)
print("Перевірка однакових:",
      вектор1 == Вектор2D(3, 4))

# Обчислення довжини
print("\nДОВЖИНА ВЕКТОРА")

print("Довжина першого:", abs(вектор1))
print("Довжина другого:", round(abs(вектор2), 2))
