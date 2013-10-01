import sys, random

word_total = 5

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {}
    words = corpus.split()

    index = 0
    while True:
        if chains.has_key((words[index], words[index + 1])):
            chains[(words[index], words[index + 1])].append(words[index + 2])
        else:
            chains[(words[index], words[index + 1])] = [words[index + 2]]

        index += 1
        if index > len(words) - 3:
            break  
    return chains

def add_word(chains):
    pass

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_text = ""
    key_list = chains.keys()
    tuples = key_list[random.randint(0, len(key_list) - 1)]
    
    first_word = tuples[0]
    second_word = tuples[1]
    third_word = chains[tuples][random.randint(0, len(chains[tuples]) - 1)]
    random_text += first_word[0].upper() + first_word[1:] + " " + second_word + " " + third_word
    
    for x in range(word_total - 3):
        first_word = second_word
        second_word = third_word
        tuples = (first_word, second_word)
        third_word = chains[tuples][random.randint(0, len(chains[tuples]) - 1)]
        random_text += " " + third_word
    
    return random_text


def main():
    script, filename = sys.argv
    f = open(filename)
    text = f.read()
    print make_text(make_chains(text.lower()))
    f.close()
    # Change this to read input_text from a file
    # input_text = "Some text"

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

# if __name__ == "__main__":
#     main()

main()