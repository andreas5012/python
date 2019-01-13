xn=int(input("Geben sie die zu berechnende Zahl an: "))
a = int(input("Wie viele Berechnungen?"))
for i in range(a):
    if xn%2==0:
        xn=xn/2
        print("xgerade = ",xn)
    elif xn%2==1:
        xn=3*xn+1
        print("xungerade = ",xn)
