
#alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    #     'q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        pos=alphabet.index(char)
        new=(pos+shift_key)%26
        cipher_text+=alphabet[new]
    print("Encrypted text: ",cipher_text)
def decryption(plain_text,shift_key):
    text=""
    for char in plain_text:
        pos=alphabet.index(char)
        new=(pos-shift_key)%26
        text+=alphabet[new]
    print(f"Encrypted text: {cipher_text}")


operation=input("Encrypt or Decrypt:\n")

if operation=="Encrypt":
    text=input("Enter the message:\n")
    shift=int(input("Enter the shift key:\n"))
    encryption(plain_text=text,shift_key=shift)
elif operation=="Decrypt":
    text=input("Enter the message:\n")
    shift=int(input("Enter the shift key:\n"))
    decryption(plain_text=text,shift_key=shift)
