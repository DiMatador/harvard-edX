#=====================Plates=================================
#===Main Function====
def main():
	valid_plate = is_valid(input("Plate: ").upper())

	if valid_plate == True:
		print("valid")
	else:
		print("invalid")


#====Logical Function Valid====
def is_valid(plate):
	# valid if * start with 2 letters
	# valid if * max of 6 characters(letters or numbers)
	digits = ['1','2','3','4','5','6','7','8','9']
	impostors = ['.',',',' ','?']
	valid_plate = plate

	for d in valid_plate:
        if (d[0] == 1 or d[0:2] in digits):
            return False
		# check the right amount of characters was entered
        elif(len(d) >= 2 and len(d) <= 6):
			return True
	    else:
			False

#===call main===
main()
