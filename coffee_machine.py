# water_amount = int(input("Write how many ml of water the coffee machine has: "))
# milk_amount = int(input("Write how many ml of milk the coffee machine has: "))
# coffee_amount = int(input("Write how many grams of coffee beans the coffee machine has: "))
# cups_amount = int(input("Write how many cups of coffee you will need: "))
# water_needed = cups_amount * 200
# milk_needed = cups_amount * 50
# coffee_needed = cups_amount * 15
# cups = min(water_amount // 200, milk_amount // 50, coffee_amount // 15)
# if water_needed <= water_amount and milk_needed <= milk_amount and coffee_needed <= coffee_amount:
#     if cups > cups_amount:
#         print(f"Yes, I can make that amount of coffee (and even {cups - cups_amount} more than that)")
#     else:
#         print(f"Yes, I can make that amount of coffee")
# else:
#     print(f"No, I can make only {cups} cups of coffee")
class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    coffee = 120
    cups = 9

    def __init__(self, _water, _milk, _coffee, _cups, _money):
        self.water = _water
        self.milk = _milk
        self.coffee = _coffee
        self.cups = _cups
        self.money = _money

    def coffee_machine_state(self):
        print(f"The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.coffee} of coffee beans\n"
              f"{self.cups} of disposal cups\n"
              f"{self.money} of money")

    def check_resources(self, _water, _milk, _coffee, _cups=1):
        if self.water - _water <= 0:
            print("Sorry, not enough water!")
        elif self.milk - _milk <= 0:
            print("Sorry, not enough milk!")
        elif self.coffee - _coffee <= 0:
            print("Sorry, not enough coffee beans!")
        elif self.cups - _cups <= 0:
            print("Sorry, not enough coffee disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            return True
        return False

    def coffee_machine_buy(self):
        coffee_type = input("What do you want to buy? "
                            "1 - espresso, 2 - latte, "
                            "3 - cappuccino, back - to main menu: ")
        if coffee_type == "back":
            return False
        elif coffee_type == "1" and self.check_resources(250, 0, 16):
            self.water -= 250
            self.coffee -= 16
            self.money += 4
            self.cups -= 1
        elif coffee_type == "2" and self.check_resources(350, 75, 20):
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
            self.cups -= 1
        elif coffee_type == "3" and self.check_resources(200, 100, 12):
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1

        # status = self.check_resources()
        # if status:
        #     self.update_state(self.money, self.water, self.milk, self.coffee, self.cups)
        return True

    def coffee_machine_fill(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))

    def coffee_machine_take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def update_state(self, _money, _water, _milk, _coffee, _cups):
        self.money = _money
        self.water = _water
        self.milk = _milk
        self.coffee = _coffee
        self.cups = _cups

    def menu(self):
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            self.coffee_machine_buy()
        elif action == "fill":
            self.coffee_machine_fill()
        elif action == "take":
            self.coffee_machine_take()
        elif action == "remaining":
            self.coffee_machine_state()
        elif action == "exit":
            return False
        return True


if __name__ == "__main__":
    my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    user_exit = True
    while user_exit:
        user_exit = my_coffee_machine.menu()
