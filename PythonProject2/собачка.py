class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} каже {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "гав")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "няв")

dog = Dog("пельмешек")
cat = Cat("шаурма")
dog.speak()
cat.speak()