class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

firstHuman = Human("이창희", 8);
print(f"firstHuman.name = {firstHuman.name}, age = {firstHuman.age}")

secondHuman = Human("김시헌", 9)
print(f"secondHuman.name = {secondHuman.name}, age = {secondHuman.age}")