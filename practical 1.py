to_start = input (f"starting with: ")
to_end = input(f"ending with: ")
string = input(f"input string : ")
acceptanace = False
if string[0] == to_start or to_start == "any":
    print("pass cond. 1")
    if string[-1] == to_end or to_end == "any":
        print("pass cond. 2")
        acceptanace = True
    else:
        print("cond. 2 fail")
else:
    print("cond. 2 fail")

if acceptanace == True:
    print("string accepted")
else :
    print ("string not accepted")