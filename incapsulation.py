def outer():
    x = "outer variable"
    
    def inner():
        print(x)  # доступ до змінної зовнішньої функції
        
    inner()

outer()  # Виведе: outer variable
