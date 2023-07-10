# implement a script to read out of a dictionary the calorie values for fruits

# main function
def main():
	nutrition = input("Item: ").capitalize()

	if calories_in_fruits(nutrition):
		print()
	else:
		return False

# logical function
def calories_in_fruits(c):
    fruits = {
        'name':'Apple', 'calories': 130, 'name':'Avacado','calories': 50,
        'name':'Banana', 'calories': 110, 'name':'Cantaloupe','calories': 50,
        'name':'Grapfruit','calories': 60, 'name':'Grapes', 'calories': 90,
        'name':'Honeydew', 'calories': 50, 'name':'Kiwifruit', 'calories': 90,
        'name':'Lemon', 'calories': 15, 'name':'Nectarine', 'calories': 60,
        'name':'Orange', 'calories': 80, 'name':'Peach', 'calories': 60,
        'name':'Pear', 'calories': 100, 'name':'Pineapple', 'calories': 50,
        'name':'Plum', 'calories': 70, 'name':'Sweet', 'calories': 100,
        'name':'Tangerine', 'calories': 50, 'name':'Watermelon', 'calories': 80
}
    for f in fruits:
        c = fruits.get('calories')
        print(c)
# call main
main()
