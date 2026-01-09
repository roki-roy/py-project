# Import we need from the user...

# total flat vara
# total food order cost fee
# Electricity units spand
# charge par units
# parsone leving in room/flat

'OUTPOU'

# Total amount leving pay is

flat_vara = int(input("total flat vara = "))
total_food_cost = int(input("food costing par month = "))
electricity_spand = int(input("spanding electricity = "))
charge_par_units = int(input("pay unit amount = "))
leving_parsone = int(input("total parsone leving the room = "))

electricity_bill = electricity_spand*charge_par_units

'output'

total_leving_cost = (flat_vara+total_food_cost+electricity_bill) // leving_parsone

print("par parsone total cost = ", total_leving_cost)