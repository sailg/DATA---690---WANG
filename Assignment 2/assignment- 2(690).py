def integers():
    ele=[]
    for i in range(10):
        try:
            Ele=int(input("ENTER NUMBER"))
            ele.append(Ele)
        except ValueError:
            return ("INTEGERS ONLY")
    a=max(ele)
    b=min(ele)
    c=a-b
    d=sum(ele)/len(ele)
    Total=0
    for i in range(len(ele)):
          Total=pow((ele[i]-c),2)+Total
    e = Total/len(ele)
    f=pow(e,.5)
    print("NUMBERS ARE",ele)
    print("BIGGEST NUMBER =",a)
    print("SMALLEST NUMBER =",b)
    print("Range =",c)
    print("Mean =",d)
    print("varience = ",e)
    print("Standard Deviation = ",f)
    
    