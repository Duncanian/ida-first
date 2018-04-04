
def longest(word_list):
    word_list = word_list.split()
    w_long = ''
    sizes = 0

    for word in word_list:
        if len(word) > sizes:
            w_long = word
            sizes = len(word)
    return w_long


yes = longest('This is Andela')

print yes
