def word_count(s):
    # initate dictionary
    words = {}
    ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    special = ['\r', '\n', '\t']

    # remove special characters
    s=s.replace(special[0], " ")
    s=s.replace(special[1], " ")
    s=s.replace(special[2], " ")
    
    # remove punctuation
    s = "".join([char for char in s if char not in ignored])

    # check if empty
    if s:
        # split string into words
        word_list = s.split(" ")
        # lowercase all words & remove spaces
        word_list = [word.lower() for word in word_list if word]

        # iterate and add to dictionary
        for i in word_list:
            if i in words:
                words[i] += 1
            else: 
                words[i] = 1

        return words
    else: return words 



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))