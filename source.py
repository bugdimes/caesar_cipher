# caesar cipher
import time

key = int(input("Enter the key: "))
plain = input("Enter the plain text: ")


def plain_to_cipher(plain, key):
    lenth = len(plain)
    new = ''
    for i in range(lenth):
        number = 0
        number = ord(plain[i])
        number = number + key
        new = new + chr(number)
    return new


ciph = plain_to_cipher(plain, key)
print("your cipher text is: ", ciph)

time.sleep(2)
print("decryption is under process with " + " " + "cipher text: " + ciph + " and key")

time.sleep(2)


def cipher_to_plain(ciph, key):
    lenth = len(ciph)
    plain = ''
    for i in range(lenth):
        number = 0
        number = ord(ciph[i])
        number = number - key
        plain = plain + chr(number)
    return plain


pln = cipher_to_plain(ciph, key)
print('original text is: ', pln)


