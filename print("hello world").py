import time
count = 0
completed = False
numsgood = False
print ("welcome to my calculator!\n.\n.\n.")
while numsgood ==  False:
    try:
        num_1 = float(input("whats your first number?\n"))
    except ValueError:
        print("\nplease put a valid number!\n")
    else: 
        numsgood = True
numsgood = False
while numsgood ==  False:
    try:
        num_2 = float(input("\nok, whats your second number?\n"))
    except ValueError:
        print("\nplease put a valid number!\n")
    else: 
        numsgood = True

while completed == False:
    operation = input("\ngreat! what operation do you want me to complete?\n options: +, -, *, /, //, ^, root\n")
    match operation:
        case "+":
            print ("calculating!")
            while count <= 3:
                    time.sleep(1)
                    print(".\n" )
                    count += 1
            try:
                print("\n\noperation complete! answer:\n", num_1 + num_2)    
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True
        case "-":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1
            try:
                print("\n\noperation complete! answer:\n", num_1 - num_2)    
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True
        case "*":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1
            try:
                print("\n\noperation complete! answer:\n", round(num_1 * num_2,10))   
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!") 
            completed = True
        case "/":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1
            try: 
                print("\n\noperation complete! answer:\n", round(num_1 / num_2,10))   
            except ZeroDivisionError:
                print("dont try to divide by 0... please")
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True
        case "//":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1           
            try: 
                print("\n\noperation complete! answer:\n", round(num_1 // num_2,10),"\nremainder:\n", num_1 % num_2)     
            except ZeroDivisionError:
                print("dont try to divide by 0... please")
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True    
        case "^":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1
            try: 
                print("\n\noperation complete! answer:\n", round(num_1 ** num_2, 10))    
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True   
        case "root":
            print ("calculating!")
            while count <= 3:
                time.sleep(1)
                print(".\n" )
                count += 1
            try:
                print("\n\noperation complete! answer:\n", round(num_2 ** (1/num_1), 10))  
            except ZeroDivisionError:
                print(f"cant take the {num_1}th root of {num_2}!")
            
            except OverflowError:
                print("woah woah woah! that number is either to large or has to many decimal points!")
            completed = True 
        case _:
            print("please put a valid operation!\n.\n.\n.")