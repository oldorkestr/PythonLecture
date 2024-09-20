def person_info(name, age):
    print(f"Name: {name}, Age: {age}")

person_info("Alice", 30)  # позиційні аргументи
person_info(age=25, name="Bob")  # іменовані аргументи
