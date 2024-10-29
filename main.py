import random


# Use this piece of code to filter the list
def filter_file(filename:str, lenth):
    ''' 
    filename:str
    -----
            will be the name of the file containing the words which is to be filtered
    '''
# Filtering the old/original file by removing any words with less then two elements in it
    with open(filename, "r") as f:
        just_reading = f.readlines()
        filtered = [item.rstrip('\n') for item in just_reading if len(item)>lenth]
        # main_fil = [item.strip("'") for item in filtered]
        filename1 = filename.replace('.txt',"_")
        # newlist = [x for x in range(10) if x < 5]
    # Writing the filtered data to a new file to be used
    with open(f"{filename1}filtered_words.txt", "w") as openedforwriting:
        openedforwriting.write(str(filtered))
        print(f"Wrote the filtered data into {filename1}filtered_words.txt")



def generate(num_words:int, file_name:str = "filtered_words.txt"):
    '''
        Usage
    -----
    This function takes **num_words** i.e number of words to be used to generate pass phrase or [the words in pass phrase ]\n
    **file_name** -- name of the file which shall be used for passphrase generation\n
    Returns two variables, **pass_phrase** -- Contains the pass_phrase itself, \n
    **easyrem** -- contains the words used to generate the pass_phrase so that it will be easier to remeber/understand
    suggested to use 4 or more for security reasons. 
    by - github.com/MU51HAK33M
    '''
    # reading from the filtered list of dictionary txt file
    with open(file_name, "r") as words_file:
        words:list = words_file.read().split() # reading the file returns a single str, usung split to split it into multiple items, so that we can perform random.choice
    if __name__ == "__main__":
        print("this")
    # to be able to add the phrases to it down the line
    easyrem:str = ""
    pass_phrase:str = "" 
    for i in range(0,num_words):
        oneword = random.choice(words)
        easyrem += "".join(oneword).strip(",") # without the strip, it will return --"'word',"
        oneword_stipped = oneword.strip(",'") # without the strip, it will return --"'word',"
        pass_phrase += "".join(oneword_stipped) # concatinating the passphrase
    return [pass_phrase , easyrem]


def another(num_words:int, file_name:str = "filtered_words.txt"):
    with open(file_name, "r") as words_file:
        words:list = words_file.read().split() # reading the file returns a single str, usung split to split it into multiple items, so that we can perform random.choice
        
    pass_phrase = random.choices(words, k=num_words)
    return str(pass_phrase).strip("',")
if __name__ == "__main__":
    # print(another(5))
    print(generate(5))
    # filter_file("short.txt", 3)