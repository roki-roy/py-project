#..Define yhe manue the restaurant

manu = {
    'pizza' : 500,
    'pasta' : 100,
    'salad' : 50,
    'coffee' : 150,
}
# Greet

print('Welcome to PYTHONE Restaurant')
print("pizza: 500\npasta: 100\nsalad: 50\ncoffee: 150")

order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in manu:
    order_total += manu[item_1] # 0+ ...
    print(f"your item{item_1} has been added to your order")
else:
    print(f"Order item is not avaialable yet")

another_order = input("do you went another item?(YES/NO)")
if another_order == "YES":
    item_2 = input("enter the name of second manu:")
    if item_2 in manu:
        order_total += manu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"order item{item_2}is not available!")

print(f"the total amount of items to pay is:{order_total}")