grocery_inventory={
    "Milk":("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}
price_eggs=grocery_inventory["Eggs"][1]
grocery_inventory.get("Eggs")
if price_eggs>5:
    grocery_inventory["Eggs"]= (
        grocery_inventory["Eggs"][0],
        price_eggs - 1,
        grocery_inventory["Eggs"][2]
    )
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes":("Produce",  1.20,  30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

stock=grocery_inventory["Milk"][2]
if stock<10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"]=(
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        stock+20,
    )
else:
    print("Milk has sufficient stock.")
price_apples=grocery_inventory["Apples"][1]
if price_apples>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)

    
    