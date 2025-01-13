
def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)

        #number of words
        words = file_contents.split()       
        word_count = 0
        for key in words:
            word_count += 1
        #print(word_count)

        #counts letters and stores resault in dict
        words_lowered = file_contents.lower()
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        alphabet_dict = {}
        for key in alphabet_string:
            letter_count = 0
            for char_key in words_lowered:
                if char_key == key:
                    letter_count += 1
            alphabet_dict[key] = letter_count
        #print(alphabet_dict)

        #creates a string for alphabet order
        alpa_store = {}
        number_store = {}
        number_max = 0

        for key in alphabet_dict:
            if alphabet_dict[key] > number_max:
                number_max = alphabet_dict[key]
        print(number_max)




        #organized report
        print(f"--- Begin report of {book_path} ---")
        print(f"{word_count} words found in the document")
        print()
        for key in alphabet_dict:
            print(f"The '{key}' character was found {alphabet_dict[key]} times")
        print("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()