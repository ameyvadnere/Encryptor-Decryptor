#The Shady Cipher:

charstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*(){}[]:";\'<>,.?/'

n = int(input("Enter the number of files you want to convert:"))
key = int(input("Enter the key:"))

def fileconversion(fileencpt):
    file1 = open(input("Enter the file to be encrypted:"), "r")
    open(fileencpt,"w").close() 
    file2 = open(fileencpt, "a+")

    for line in file1:
        line2 = ''
        for char in line:
            pos = charstring.find(char)
            pos = (pos+key)%len(charstring)
            line2 = line2 + charstring[pos]
        line3 = line2[:len(line2)-1]
        file2.write(line3+"\n")

    file1.close()
    file2.close()

for i in range(n):
    fileencpt = input("Enter the name of the final encrypted file no. {0}:" .format(i+1))
    fileconversion(fileencpt)
