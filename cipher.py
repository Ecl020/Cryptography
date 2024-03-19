################################################################################################################
# Vigenere Cipher
# Erik Claros Turcios
# This is a tool that can encrypt and decrypt messages using the Vigenere and Ceaser ciphers
# 03/18/2024
# Refernce : https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf

# We can start encrypting a message using the algorithm below
#  x = (x + k mod length) % 26

# Where x is the position of the letter in the alphabet and k is the key
class ShiftCipher:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    # Encrypt the message using the key
    def s_encrypt(key, message):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        ciphertext = ''
        # Iterate through each character in the message
        for char in message:
            # If the character is in the alphabet, shift it by the key
            if char in alphabet:
                temp = alphabet.index(char)
                # Adjusted to support both upper and lower case letters
                ciphertext += alphabet[(temp + key) % 52]  # Adjusted to support both upper and lower case letters
            else:
                # If the character is not in the alphabet, leave it unchanged
                ciphertext += char  # If the character is not in the alphabet, leave it unchanged
        return ciphertext
    
    # Decrypt the message using the key
    def s_decrypt(message):
        # List to display all the possible decrypted messages
        decrypted_list = []
        # Iterate through all possible keys
        for shift in range(26):
            decrypted_message = ''
            # Iterate through each character in the message
            for char in message:
                # If the character is in the alphabet, shift it by the key
                if char.isupper():
                    decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
                # Adjusted to support both upper and lower case letters
                elif char.islower():
                    decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
                # If the character is not in the alphabet, leave it unchanged
                else:
                    decrypted_char = char
                    # Add the decrypted character to the decrypted message
                decrypted_message += decrypted_char
                # Add the decrypted message to the list of possible decrypted messages
            decrypted_list.append(decrypted_message)
        return decrypted_list


class VigenereCipher:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    # Encrypt the message using the key
    def v_encrypt(key, message):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        ciphertext = ''
        # Iterate through each character in the message
        for i in range(len(message)):
            # If the character is in the alphabet, shift it by the key
            temp = alphabet.index(message[i])
            # Adjusted to support both upper and lower case letters
            x = alphabet.index(key[i % len(key)])
            #  x = (x + k mod length) % 26
            ciphertext += alphabet[(temp + x) % 26]
        return ciphertext


    def v_decrypt(key, message):
        plaintext = ""
        key_length = len(key)
        # Convert the key to uppercase
        key_as_int = [ord(k) for k in key.upper()]
        i = 0
        # Iterate through each character in the message
        for char in message:
            if char.isalpha():
                # If the character is in the alphabet, shift it by the key. Adjusted to support both upper and lower case letters
                shift = key_as_int[i % key_length] - 65 if char.isupper() else key_as_int[i % key_length] - 97
                # Adjusted to support both upper and lower case letters and to decrypt the message
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97)
                # Add the decrypted character to the decrypted message
                plaintext += decrypted_char
                i += 1
            else:
                plaintext += char
        return plaintext
    

    # Analyze the frequency of the letters in the message
    def frequent_analysis(message):
        frequency = {}
        for letter in message:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        return frequency

    # Find the most common letter in the message
    def most_common_letter(frequency):
        return max(frequency, key=frequency.get)

    # Find the possible words that could be decrypted from the message
    def possible_words(frequency, message):
        possible_words = []
        for i in range(26):
            possible_words.append(VigenereCipher.v_decrypt(message, VigenereCipher.alphabet[i]))
        return possible_words
    


class main:
    def main():
        print("Would you like to work with a ceaser cipher or a vigenere cipher? (ceaser/vigenere)")
        choice = input()
        print("Would you like to encrypt or decrypt? (encrypt/decrypt)")
        action = input()
        if (choice == "ceaser"):
            print("Enter a key: to encrypt or decrypt")
            key = int(input())
            print("Enter a message: to encrypt or decrypt")
            message = input()
        else:
            key = input("Enter a key: to encrypt or decrypt. ")
            message = input("Enter a message: to encrypt or decrypt(All Caps for Decrypt):")
        # key = "candy"
        # message = "Hello World"


        print("----------------------Vigenere Cipher Tool----------------------" + "\n")
        print("Message:" + message)
        print("Key:")
        print (key)
        print("\n")
        if(choice == "ceaser"):
            print("----------------------Shift Cipher----------------------" + "\n")
            if(action == "encrypt"):
                print("Encrypted Message:")
                print (ShiftCipher.s_encrypt(key, message))
            else:
                print("Decrypted Message:")
                print (ShiftCipher.s_decrypt(message))
                print("\n")
                



        if(choice == "vigenere"):
            print("----------------------Vigenere Cipher----------------------" + "\n")
            if(action == "encrypt"):
                print("Encrypted Message:")
                print (VigenereCipher.v_encrypt(key, message))

            else:
                print("Decrypted Message:")
                print (VigenereCipher.v_decrypt(key, message))
                print("\n")

        else:
            # print("Most Common Letters:"+ "\n")
            # print(VigenereCipher.frequent_analysis(message))
            # print("Most Common Letter:") 
            # print(VigenereCipher.most_common_letter(VigenereCipher.frequent_analysis(message)) )
            # print("Rotation :"+ "\n") 
            # print (VigenereCipher.possible_words(VigenereCipher.frequent_analysis(message), message) )
            # print("\n")
            print("Error: Invalid Input. Please try again.")

# Call the main function
main.main()