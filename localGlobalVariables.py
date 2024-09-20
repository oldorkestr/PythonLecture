x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)  # Виведе: 20
