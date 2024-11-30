from kanren import create_fact, run, fact, var, Relation, facts

# Створення відносин для батька, матері і дітей
parent = Relation()
mother = Relation()
father = Relation()
sibling = Relation()

# Додавання фактів для батьків та дітей
fact(father, "John", "Alice")
fact(mother, "Mary", "Alice")
fact(father, "John", "Bob")
fact(mother, "Mary", "Bob")
fact(father, "Peter", "Charlie")
fact(mother, "Lily", "Charlie")

# Визначення батьків дітей
fact(parent, "John", "Alice")
fact(parent, "Mary", "Alice")
fact(parent, "John", "Bob")
fact(parent, "Mary", "Bob")
fact(parent, "Peter", "Charlie")
fact(parent, "Lily", "Charlie")

# Додавання фактів для братів та сестер (якщо два людини мають спільних батьків, то вони є братами чи сестрами)
def siblings(x, y):
    return sibling(x, y) | sibling(y, x) | (parent(x, z) & parent(y, z))

# Створення змінних для запитів
x = var()
y = var()
z = var()

# Запит: хто є братом або сестрою Bob?
print("Brothers/Sisters of Bob:", run(0, x, sibling(x, "Bob")))

# Запит: хто є батьками Alice?
print("Parents of Alice:", run(0, x, parent(x, "Alice")))

# Запит: хто є батьками Charlie?
print("Parents of Charlie:", run(0, x, parent(x, "Charlie")))

# Запит: хто є дитиною John?
print("Children of John:", run(0, x, parent("John", x)))

# Запит: чи є у John брат або сестра?
print("Does John have siblings?", run(0, x, sibling("John", x)))

# Запит на визначення родичів у двох поколіннях
def grandparent(x, y):
    return parent(x, z) & parent(z, y)

# Запит: хто є прабабусею/прадідусем Bob?
print("Grandparents of Bob:", run(0, x, grandparent(x, "Bob")))

# Запит: хто є найближчим родичем Charlie?
# Якщо найближчий родич не є батьком або матір'ю, то знайдемо братів/сестер
def closest_relative(x, y):
    return parent(x, y) | sibling(x, y)

print("Closest relatives of Charlie:", run(0, x, closest_relative(x, "Charlie")))

# Запит на визначення родинних зв'язків з обмеженнями
def is_uncle(x, y):
    return sibling(x, z) & parent(z, y)

# Запит: чи є John дядьком для Bob?
print("Is John an uncle to Bob?", run(0, x, is_uncle(x, "Bob")))

# Запит на складніший зв'язок
def cousin(x, y):
    return is_uncle(x, y) | is_uncle(y, x)

# Запит: чи є Alice кузиною для Charlie?
print("Is Alice cousin to Charlie?", run(0, x, cousin("Alice", "Charlie")))

# Тест на зворотний зв'язок
print("Is Bob a parent of Alice?", run(0, x, parent("Bob", "Alice")))
