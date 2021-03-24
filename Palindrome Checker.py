s = input("Δώσε μία λέξη: ")

if len(s) == 1:
    print("Μήκος = 1")
    
elif s == s[::-1]:
    adict = {s : len(s)}
    alist = []
    for i in s:
        alist.append(i)
    print(adict)
    print(alist)
else:
    print("Δεν είναι παλίνδρομο")
        
    
