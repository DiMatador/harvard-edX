#==================Taqueria Script=======================

#==main===
def main():
	order = menu_order("Item: ")
	return order


#========================================================
def menu_order(tacos):
	meals = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
	total = 0
	while True:
		#total = 0
		try:
			order = input(tacos).title()
		except (EOFError):
			break
		try:
			#order = input(tacos).title()
			#ordered_item =  meals[order]
			#print(f"${ordered_item:0.2f}")
			if order in meals:
				total = meals[order] + total
				print(f"Total: ${total:0.2f}")
			else:
				pass
		except (NameError):
			pass


		#print(f"Total: ${total:0.2f}")

# call main
main()