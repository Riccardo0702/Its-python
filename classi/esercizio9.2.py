class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, address):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.address = address
        
    def describe_restaurant(self):
        print(f"Il nome del ristorante è: {self.restaurant_name}")
        print(f"La cucina del ristorante è: {self.cuisine_type}")
        print(f"L'indirizzo del ristorante è: {self.address}")
    


restaurant = Restaurant("Da Gianni", "Napoletana", "Via Riccardo Placidi 724")

restaurant.describe_restaurant()
   