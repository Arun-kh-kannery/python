def encryption(text,shift_key):
    ans=""
    for i in text:
        if(ord('a')<= ord(i) <=ord('z')):
            ans+=chr(ord('a')+(ord(i)-ord('a')+shift_key)%26)
        elif(ord('A') <= ord(i) <=ord('Z')):
            ans+=chr(ord('A')+(ord(i)-ord('A')+shift_key)%26)
        else:
            ans+=i
    print(f"Here is the text after encryption : {ans}")
def decryption(text,shift_key):
    ans=""
    for i in text:
        if (ord('a') <= ord(i) <= ord('z')):
            ans += chr(ord('a') + (ord(i) - ord('a') - shift_key) % 26)
        elif (ord('A') <= ord(i) <= ord('Z')):
            ans += chr(ord('A') + (ord(i) - ord('A') - shift_key) % 26)
        else:
            ans += i
        # just testing it
    print(f"Here is the text after decryption: {ans}")
while(True):
    text=input("Enter your message:\n ")
    shift_key=int(input("Enter Shift_Key:\n"))
    operation = input("Type 'encrypt' for encryption,Type 'decrypt' for decryption :\n")
    if(operation == 'encrypt'):
        encryption(text,shift_key)
    elif(operation=="decrypt"):
        decryption(text,shift_key)
    play_again=input("Type 'yes' to continue,Type 'no' to exit:\n")
    if(play_again=="no"):
        print('Have a nice day ')
        exit()

