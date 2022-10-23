'''
CISC-121 2022W
  
This program proccesses a group of books to find which of the other
books is most similar to it in terms of similarity in their
signature words. 

Name: Matthew Sun
Student Number: 20273229
Email: matt.suncy@gmail.com

I confirm that this assignment solution is my own work and conforms to 
Queen's standards of Academic Integrity
'''

import glob
from tkinter.filedialog import askdirectory
import tkinter as tk
from tkinter import font
import ntpath


def letters_only(word):
    '''
    This function takes in a string and removes any non-letter character and 
    then returns it.

    Parameters: word - a string of characters

    Returns: clean_word - a string of only letters
    '''

    clean_word = ''
    for x in word:
        if x.isalpha():
            clean_word += x

    return clean_word


def find_signatures(text_files, stop_words):
    '''
    This function reads .txt files from a directory and counts the number of 
    times non-stop-words appear.

    Parameters: text_files - an iterable of file directories
    stop_words - a set of words for which the function will not count if it 
    is encountered

    Returns: book_signatures - a dictionary, keys are the book titles, the 
    value is a list of tuples of the 25 most common words in the text, the 
    first element of each tuple is the word and the second is the frequency
    '''

    book_signatures = {}

    for book in text_files:
        infile = open(book, 'r', encoding="UTF-8")
        # Now the program will do all the reading and count the words

        word_count = {}

        for line in infile:
            line_words = line.split()
            for word in line_words:
                word = letters_only(word.lower())
                if word not in stop_words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        words_frequencies = []

        for w, c in iter(word_count.items()):
            words_frequencies.append((w, c))

        words_frequencies.sort(key=lambda x: x[1], reverse=True)
        # I used ntpath.basename to access the file name instead of the whole directory
        book_title = (ntpath.basename(book))[0:-4]
        # Takes book title as key and then takes a list of the first 25 elements as the value
        book_signatures[book_title] = words_frequencies[0:25]

    return book_signatures


def text_similarities(book_signatures):
    '''
    This function takes in a dictionary of book titles and their signature 
    words and finds which of the other books it is most similar to based on
    the Jacard similarity measure.

    Parameters: book_signatures - a dictionary, keys are titles, values are
    lists of tuples containing words and their frequencies

    Returns: most_similar_dict - a dictionary, where each text is the key and
    the values are the text that it is most similar to.
    '''

    list_of_keys = list(book_signatures.keys())
    list_of_sets = []
    for key in list_of_keys:
        # Each group of signature words is added into a set
        set_of_words = set()
        for tuple in book_signatures[key]:
            set_of_words.add(tuple[0])

        list_of_sets.append(set_of_words)

    # Where n is the number of sets in list_of_sets we should compare n choose 2 times
    # In this case we have 25 texts so we compare 24+23+22+...+1 = 300 times
    # This loop structure makes n choose 2 unique tuples with 2 titles and their Jaccard similarity score
    measures_list = []
    for i in range(len(list_of_sets)):

        for j in range(i + 1, len(list_of_sets)):

            jaccard_similarity = (len(list_of_sets[i].intersection(
                list_of_sets[j]))) / (len(list_of_sets[i].union(list_of_sets[j])))
            measures_list.append(
                (list_of_keys[i], list_of_keys[j], jaccard_similarity))

    # This sorts all tuples by Jaccard similarity in descending order
    measures_list.sort(key=lambda x: x[2], reverse=True)
    # Now we can add to pairs of texts to a dictionary where the key is the name of every text and the value is the most similar text
    most_similar_dict = {}
    for x in measures_list:
        # If both a and b are not in the dict that means a is most similar to b and vice versa.
        # Let's say later on we see c is most similar to b, b is already most similar to a so we just have c: b
        if x[0] not in most_similar_dict or x[1] not in most_similar_dict:

            if x[0] not in most_similar_dict:
                most_similar_dict[x[0]] = x[1]
            if x[1] not in most_similar_dict:
                most_similar_dict[x[1]] = x[0]

    return most_similar_dict


stop_words_file = open("StopWords.txt", 'r', encoding='UTF-8')
stop_words = set()
for line in stop_words_file:
    word = letters_only(line)
    stop_words.add(word)

books_data_directory = askdirectory(
    initialdir="Macintosh HD/users/matt.suncy/Documents/CISC 121/A3/Books")
text_files = glob.glob(books_data_directory + "/" + "*.txt")

books_signatures = find_signatures(text_files, stop_words)

similar_texts = text_similarities(books_signatures)

window = tk.Tk()
window.title('What Do You Recommend?')
window.geometry("600x800")
# pady = 20 gives some vertical separation between this row and the next
col_0_head = tk.Label(window, text=" Book Title: ", pady=20, font=('None', 16))
col_0_head.grid(row=0, column=0)

col_1_head = tk.Label(
    window, text=" It's Most Similar to: ", font=('None', 16))
col_1_head.grid(row=0, column=1)

book_titles = list(similar_texts.keys())
rows = 25
columns = 2
for i in range(rows):
    n = i + 1
    for j in range(columns):
        # Column 0 shows the book title
        if j == 0:
            x = tk.Label(window, text=str(book_titles[i]))
            x.grid(row=n, column=j)
        # Column 1 shows the most similar book
        elif j == 1:
            x = tk.Label(window, text=str(similar_texts[book_titles[i]]))
            x.grid(row=n, column=j)

window.mainloop()
