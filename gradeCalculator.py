def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    
try:
    
    hrs = float(input("Enter score:"))
       
    if hrs >= 0.9 and hrs <= 1.0:
        print("A")
    elif hrs >= 0.8 and hrs < 0.9:
        print("B")
    elif hrs >= 0.7 and hrs < 0.8:
        print("C")
    elif hrs >= 0.6 and hrs < 0.7:
        print("D")
    elif hrs < 0.6:
        print("F")
    else:
        print("Bad score")
            
except:
    print("Please enter a number")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()