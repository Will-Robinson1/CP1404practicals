number_of_items = int(input( "Number of items: "))
total = 0
for i in range(0, number_of_items, 1):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    total = 0.9*total
print(f"Total price for {number_of_items:} items is ${total:.2f}")