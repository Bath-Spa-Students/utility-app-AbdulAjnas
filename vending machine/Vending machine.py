items = {
    11: "Cheetoes", 12: "Doritoes", 13: "Lays", 14: "Kurkure", 15: "Oman Chips", 16: "Pringles",
    17: "Bugles", 18: "Lays Max", 19: "Mr Krips", 20: "Takis",
    21: "M&Ms", 22: "Gumballs", 23: "Skittles", 24: "Hello Panda", 25: "Pop rocks", 26: "Sour Candy",
    27: "Bubble Gum", 28: "Lolipop",
    31: "Coca Cola", 32: "7up", 33: "Mountain Dew", 34: "Fanta", 35: "Sprite", 36: "Pepsi",
    41: "Apple", 42: "Orange", 43: "Mango", 44: "Strawberry", 45: "Pomogranate", 46: "Lichi",
    47: "Lemon", 48: "Lemon Mint", 49: "Mixed", 50: "Water",
    51: "Dairy Milk", 52: "Galaxy", 53: "Flakes", 54: "Toblerone", 55: "Twix", 56: "Snickers",
    57: "Break Rizzo", 58: "Hersheys", 59: "Bounty", 60: "Ferero Rocher"
}

prices = {
    11: 4, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4,
    21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 2, 27: 2, 28: 2,
    31: 3, 32: 3, 33: 3, 34: 3, 35: 3, 36: 3,
    41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1,
    51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2
}

while True:
    print("\nMenu:")
    for code, item in items.items():
        print(f"{code} - {item}")

    money = int(input("\nInsert money: "))
    choice = int(input("Choose your order: "))

    if choice not in items:
        print("Error! Please choose the correct order number.")
        continue

    item_price = prices[choice]
    if money == item_price:
        print(f"You chose {items[choice]}. Enjoy your {items[choice]}. Thank you!")
    elif money > item_price:
        change = money - item_price
        print(f"You chose {items[choice]}. Here's your change: {change}. Please take your order. Thank you!")
    else:
        print("Please enter enough money.")

    order_again = input("Do you want to order again? (yes/no): ").lower()
    if order_again != 'yes':
        break