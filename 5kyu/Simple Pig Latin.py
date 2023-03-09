# DESCRIPTION: Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave
# punctuation marks untouched. 

def pig_it(text):
    return " ".join([x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split()])
