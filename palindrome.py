
clean = lambda word: word.lower().strip().replace(' ', '').replace(',', '')

reverse = lambda string: "".join([c for c in clean(string)[::-1]])

is_palindrome = lambda word: True if reverse(word) == clean(word) else False



if __name__ == "__main__":
    print(is_palindrome('pudim'))
    print(is_palindrome('tattarrattat'))
    print(is_palindrome('never odd or even'))
    print(is_palindrome('Sir, I demand, I am a maid named Iris'))
