
def longest(word_list):
    word_list = word_list.split()
    long_w = ''
    sizes = 0

    for word in word_list:
        if len(word) > sizes:
            long_w = word
            sizes = len(word)
    return long_w


yes = longest('This is Andela')

print yes
