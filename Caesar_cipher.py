def encryption():
    print("This is encryption:...")
    plain=input("Enter the plain text: ")
    c=""
    f=" "
    x=int(input("Enter the no of shifts: "))
    pt=plain.upper()
    for i in pt:
        if i.isupper():
            c=c+chr((ord(i)+x-65)%26+65)
        elif f==" ":
            c=c+f
        '''elif i.lower():
            c=c+chr((ord(i)+x-97)%26+97)'''
    print("caesar cipher encryption text is :.... ",c)
def decryption():
    print("This is decryption:...")
    cipher_text=input("Enter the cipher  text: ")
    d=""
    a=" "
    y=int(input("Enter the no of shifts: "))
    ct=cipher_text.upper()
    for j in cipher_text:
        if j.isupper():
            d=d+chr((ord(j)-y-65)%26+65)
        elif a==" ":
            d=d+a
        '''elif i.lower():
            d=d+chr((ord(i)-y-97)%26+97)'''
        
    print("caesar cipher decryption  text is :.... ",d)
encryption()
decryption()