# Coffee machine simulator

class CoffeeMachine:
    def __init__(self, water_level=1000, beans_quantity=500):
        self.water_level = water_level #ml
        self.beans_quantity = beans_quantity #grams
        
    def make_coffee(self):
        if self.water_level < 250:
            print("Not enough water to make coffee! Please refill!")
            return # the blank return is similar to the break in a while loop
        if self.beans_quantity < 50:
            print("Not enough beans to make coffee! Please refill!")
            return
        
        self.water_level -= 250
        self.beans_quantity -= 50
        print("Made a cup of coffee. Enjoy!")

    def refill_water(self, amount):
        self.water_level += amount
        print(f"Refilled water by {amount} ml.")

    def refill_beans(self, amount):
        self.beans_quantity += amount
        print(f"Refilled beans by {amount} grams.")

    def check_status(self):
        print(f"Water level: {self.water_level} ml.")
        print(f"Coffee beans quantityL {self.beans_quantity} grams.")

machine = CoffeeMachine()

while True:
    print("\n1. Make coffee\n2. Refill water\n3. Refill coffee beans\n4. Check status\n5. Turn off")
    choice = input("Choose an action: ")


    if choice == "5":
        print("Turning off the machine.")
        break
    elif choice == "1":
        machine.make_coffee()
    elif choice == "2":
        amount = int(input("Enter the amount of wate to refill(ml): "))
        machine.refill_water(amount)
    elif choice == "3":
        amount1 = int(input("Enter the amount of beans to refill(grams): "))
        machine.refill_beans(amount1)
    elif choice == "4":
        print(f"total water: {self.}")

