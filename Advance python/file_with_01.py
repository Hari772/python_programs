with open("poem.txt","r") as fp:
    
    if 'Twinkle' in fp.read():
        print("Yes Twinkle is present\n")
    else:
        print("twinkle is not present\n")
        