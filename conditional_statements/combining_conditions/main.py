# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct=discounted or lowStock
print(movingProduct)
promotion = not(movingProduct) 
print(promotion)
print("Is the item eligible for promotion ?",promotion)
