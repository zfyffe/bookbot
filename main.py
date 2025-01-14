
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
        alpha_store = ""
        number_list = []
        letter_max = ""
        del_alpha_dict = alphabet_dict
        
        for key in alphabet_dict:
            number_list.append(alphabet_dict[key])
        number_list.sort(reverse=True)
        print(number_list)

        for key in number_list:
            for key2 in alphabet_dict:
                if key == alphabet_dict[key2]:
                    alpha_store += key2
            print(key)
        
        print(alpha_store)
            




        #organized report
        print(f"--- Begin report of {book_path} ---")
        print(f"{word_count} words found in the document")
        print()
        for key in alpha_store:
            print(f"The '{key}' character was found {alphabet_dict[key]} times")
        print("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()