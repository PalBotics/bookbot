#import os
#print(f"Current working directory: {os.getcwd()}")
title = "books/frankenstein.txt"

# read the contents of the book
def read_book():
    with open(title) as f:
        file_contents = f.read()
        #print(file_contents)
        #words = len(file_contents.split())
        #print(f"The text has {words} words.")
        
    return (file_contents)

def count_words(text):
    #text_length = len(text)
    #print(f"text length is {text_length}")
    words = len(text.split())
    print(f"The text has {words} words.")
    return(words)
    

def count_chars(text):
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    chars = {}
    for letter in text:
        letter = letter.lower()
        if letter in alphabet:
            # If letter is already in dictionary
            if letter in chars:
                chars[letter] += 1

            # If letter isn't in dictionary yet
            else:
                chars[letter] = 1
    return (chars)

def print_report(title, words, chars):
    print(f"--- Begin report of {title} ---")
    print(f"{words} words found in the document\n")
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")
    print("--- End report ---")

    return


def main():
    print("Reading the book")
    file_contents = read_book()
    # print(file_contents)
    words = count_words(file_contents)
    chars = (count_chars(file_contents))
    print_report(title, words, chars)

    

if __name__ == "__main__":
    main()
