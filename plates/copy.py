#=====================Plates=================================
#===Main Function====
def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("valid")
    else:
        print("invalid")


#====Logical Function Valid====
def is_valid(s):
# valid if * start with 2 letters
# valid if * max of 6 characters(letters or numbers)
    digits = ['1','2','3','4','5','6','7','8','9']
    impostors = ['.',',',' ','?','!','/']
          
    # validate first two letter != numbers
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False

    for ch in s:
        if ch.isdigit():
            fd = s.index(ch)
            if s[fd:].isdigit()and ch != '0':
                return True
            else:
                return False
        
    # check for puntuations   
    for banana in s:
        if(banana in impostors):
            return False
        
    # check for any digits in the middle of the plate name    
    
            
    # Validate length of string
    if (len(s) >= 2 and len(s) <= 6):
        return True
   

#===call main===
main()
ye
