import random , time
def main():
    target = input("Enter a wor you want to print")
    print_word(target)

def print_word(target):
    result = ""
    
    word_list = "abcdefghijklmnopqrstuvwxyz "
    for letters in target:
        while True:
            selected_word = random.choice(word_list)
            
            
            print(result+selected_word)
            time.sleep(0.09)
            if selected_word == letters:
                result += selected_word
                break
main()     
            
    

        
