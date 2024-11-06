class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1= person("Ana",30)
person2= person("Luis", 25)

person1.greet()
person2.greet()