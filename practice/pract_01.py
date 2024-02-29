class Pets:
    def __init__(self):
        self.pets_list = []

    def add_pet(self, *pet_name):
        for pet in pet_name:
            self.pets_list.append(pet)

    def remove_pet(self, *pet_name):
        for pet in pet_name:
            try:
                self.pets_list.remove(pet)
                print(f"Pet {pet} removed")
            except:
                print(f"Pet {pet} not found")

    def list_pets(self):
        for i, pet in enumerate(self.pets_list):
            print(i+1, pet)


my_pets = Pets()
my_pets.add_pet("Dog", "Cat", "Camel", "Cow")
print(my_pets.pets_list)
my_pets.remove_pet("Camel")
my_pets.list_pets()
