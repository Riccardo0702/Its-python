class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Il nome del ristorante è: {self.restaurant_name}")
        print(f"La cucina del ristorante è: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")
    
restaurant = Restaurant("Da Gianni", "Napoletana")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()