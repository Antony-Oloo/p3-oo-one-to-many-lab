class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet instance to the all list
        Pet.all.append(self)
        
        # If the owner is provided, add the pet to the owner's pets
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list to store pets
    
    def pets(self):
        """Returns a list of the owner's pets"""
        return self._pets
    
    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets"""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        
        pet.owner = self  # Set this pet's owner to the current owner
        self._pets.append(pet)
    
    def get_sorted_pets(self):
        """Returns the owner's pets sorted by their name"""
        return sorted(self._pets, key=lambda pet: pet.name)

