# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}
def morse_generator(text):
    morse = ""
    for char in text:
        if char in morse_code:
            morse += ' '+ morse_code[char]
    return morse
def decode_morse(morse):
    splited_morse = morse.split(' ')
    decoded_morse = ''
    for text in splited_morse:

        for (key, values) in morse_code.items():
           if text == values:
               decoded_morse += " "+ key

    return decoded_morse

def main():
    while True:
        print("1. encode text. ")
        print("2. decode morse code. ")
        print("3. exit. ")
        print("*"*100)
        choice = input("Enter your choice: ")
        if choice == "1":
            text = input("Enter morse code: ")
            morse = morse_generator(text)
            print(morse)
        elif choice == "2":
            text = input("Enter morse code: ")
            decoded_morse = decode_morse(text)
            print(decoded_morse)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
