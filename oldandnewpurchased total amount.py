a=int(input("enter the no of fresh loaves purchased :"));
b=int(input("enter the no of old loaves purchased :"));
if(a<=0):
    print("enter the positive integer greater than 0");
else:
    f=a*185
    o=(b*185)*60/100
    print("regular price: Rs.185.00");
    print("amount of new loaves:", float(f));
    print("amount of old loaves:", float(o));
    print("total amount:", f+o);
