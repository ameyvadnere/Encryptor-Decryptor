msg = str(input("Enter a message:"))
key = int(input("Enter the key:"))

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*(){}[]:";\'<>,.?/'
    
decpt = ''
for i in range(0, len(msg)):
          char = msg[i]
          pos = alpha.find(char)
          pos = (pos - key)%len(alpha)
          decpt = decpt + alpha[pos]

print ("The decrypted message is:", decpt)


