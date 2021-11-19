import data_mkwii
txt = ""
n1 = 0
n2 = 0
check = True
while check:
    u = input("choose your region (P = PAL, U = NTSC-U, J = NTSC-J, K = NTSC-K) :")
    if u.lower() == "p":
        cc200 = data_mkwii.data["PAL"]["200cc"]
        cc350 = data_mkwii.data["PAL"]["350cc"]
        check = False
    elif u.lower() == "u":
        cc200 = data_mkwii.data["NTSC-U"]["200cc"]
        cc350 = data_mkwii.data["NTSC-U"]["350cc"]
        check = False
    elif u.lower() == "j":
        cc200 = data_mkwii.data["NTSC-J"]["200cc"]
        cc350 = data_mkwii.data["NTSC-J"]["350cc"]
        check = False
    elif u.lower() == "k":
        cc200 = data_mkwii.data["NTSC-K"]["200cc"]
        cc350 = data_mkwii.data["NTSC-K"]["350cc"]
        check = False
    else:
        print("invalid version try again")
c = int(input("choose your cc: "))
coef = c/350
l1 = cc200.split("\n")
l2 = cc350.split("\n")
while len(l2) > n2:
    while len(l1)>n1:
        if l2[n2].split()[0] == l1[n1].split()[0]:
            t1 = int(l1[n1].split()[1], base=16)
            t2 = int(l2[n2].split()[1], base=16)
            x = (t1*((t2/t1)**coef if t2 != 0 else 0))
            
            value = hex(round(x))[2:10]
            if len(value)<8 : 
                s = ""
                for i in range(8-len(value)):
                    s += "0"
                value = s + value
            txt += l2[n2].split()[0] +" "+ value +"\n"
            break
        n1 += 1
    n2 += 1

for i in txt.split("\n"):
    print(i)
input("enter to close")