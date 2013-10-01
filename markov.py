import sys, random

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
def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_text = ""
    
    return random_text


def main():
    script, filename = sys.argv
    f = open(filename)
    text = f.read()
    print make_text(make_chains(text))
    f.close()
    # Change this to read input_text from a file
    # input_text = "Some text"

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

# if __name__ == "__main__":
#     main()

main()