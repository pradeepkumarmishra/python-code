#%%
avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
avengers.pop(1)
avengers.insert(0, 'Captain America')
#print(avengers)

scores = [92, 85, 76, 58, 89, 91, 73, 84]
aCount = bCount = cCount = dCount = eCount = 0
for i in scores:
    if i > 90 and i <= 100:
        aCount += 1
    elif i > 80 and i <= 89:
        bCount += 1
    elif i > 70 and i <= 79:
        cCount += 1
    elif i > 60 and i <= 69:
        dCount += 1
    else:
        eCount += 1

# print(f"""
# Grade Summary:
# - A: {aCount} students
# - B: {bCount} students
# - C: {cCount} students
# - D: {dCount} students
# - F: {eCount} students
# """)

# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering
items_to_order = []
for i in range(len(product_names)):
        if stock_levels[i] < minimum_stock:
            items_to_order.append(product_names[i])
#helloMsg = "hello" if 1 < 2 else "bye"
print("Items to Reorder:")
for i in items_to_order:
    print(f"- {i}")


#%%
