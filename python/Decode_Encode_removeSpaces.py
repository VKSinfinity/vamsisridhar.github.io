while True:
    z = input("\ninsert x to encode\decode or insert y to remove spaces:")
    a = ord(z)
    if a==ord("x"):
        x = input("Enter message to encode: ")
        
        print ("Decoded string (in ASCII):")
        print ("\n"), 
        for ch in x:
            #print ord(ch)
            #print 255-ord(ch)
            print ((chr(65535-int(ord(ch)))),end="")
        print ("\n\n"),    
        
    if a==ord("y"):
        c = input("enter text to remove space: ")
        print (c.replace(" ",""),end=""),

