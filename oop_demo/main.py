# Input animal type e.g. Dog, Cat


class CreatePet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def introduce(self):
        print(
            f"My name is {self.name.title()} i am a {self.age} year old {self.pet_type.title()}"
        )


pet1 = CreatePet("doge", 8, "dog")

pet1.introduce()