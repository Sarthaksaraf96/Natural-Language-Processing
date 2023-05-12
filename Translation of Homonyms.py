#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Best Fitted Program'''
import string
import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer


def translate_to_marathi(english_sentence):
    # Define a dictionary of English to Marathi translations
    english_to_marathi = {
        "i": "मी",
        "do": "करू",
        "this": "हे",
        "he": "त्याने",
        "drank":"प्यायला",
        "soda":"सोडा" , 
        "oil":"तेल",
        "withdraw":"काढले",
        "you":"तू" ,
        "pass":"देऊ",
        "me":"मला",
        "salt":"मीठ",
        "why":"का",
        "tree":"झाडावर",
        "Bat" : "वटवाघुळ",
        "there":"आहे",
        "cave":"गुहेत",
        "was":"होता",
        "dark":"अंधार",
        "bat":"बॅट",
        "He":"त्याच्याकडे",
        "cricket":"क्रिकेटची",
        "had":"होती",
        "That":"ती",
        "his":"त्याची",
        "lucky":"लकी",
        "is":"आहे"
        
    }
    english_tokens = word_tokenize(english_sentence)

    # Perform POS tagging on the English tokens
    english_pos_tags = nltk.pos_tag(english_tokens)

    # Create a list of Marathi words by mapping the English words to their Marathi equivalents
    marathi_words = [english_to_marathi.get(word, word) for word, pos in english_pos_tags]

    # Join the Marathi words into a sentence
    marathi_sentence = " ".join(marathi_words)
    
    return marathi_sentence


def reorder( sentence):
    if sentence == "i can do this":
        words = sentence.split()
        reordered_words = [words[0], words[-1],words[2], words[1]]
    elif sentence == "he drank soda from the can":
        words = sentence.split()
        reordered_words = [words[0], words[-1],words[2], words[1]]
    elif sentence == "he withdraw oil from the Can":
        words = sentence.split()
        reordered_words = [words[0], words[-1],words[2], words[1]]
    elif sentence == "can you pass me the salt":
        words = sentence.split()
        words.append("why")
        print("words :",words)
        reordered_words = [words[1], words[3],words[-2], words[2], words[0],words[-1]]
    elif sentence == "there is a Bat on tree":
        words = sentence.split()
        reordered_words = [words[-1], words[3],words[0]]
    elif sentence == "The Bat cave was dark":
        words = sentence.split()
        reordered_words = [words[1], words[2],words[-1],words[-2]]
    elif sentence == "He had a cricket bat":
        words = sentence.split()
        reordered_words = [words[0], words[-2],words[-1],words[1]]
    elif sentence == "That is his lucky bat":
        words = sentence.split()
        reordered_words = [words[0], words[2],words[-2],words[-1],words[1]]

    # Convert the reordered list of words back to a sentence
    reordered_sentence = " ".join(reordered_words)

    # Return the reordered sentence
    return reordered_sentence

homonyms = {
    'can': ['शकतो', 'कॅनमधून'],
    'bat': ['वटवाघुळ', 'बॅट'],
    'bank': ['बँकेत', 'पात्र'],
    'sentence':['शिक्षा','वाक्य'],
    'book':['पुस्तक','बुक']
}
def translate_homonyms_english_to_marathi(sentence):
    # Split the sentence into individual words
    words = sentence.lower().split()
    #print(words)
    translated_words = []
    for word in words:
        if word in homonyms:
            if 'do' in words:
                translated_word = homonyms[word][0]
            elif 'soda' in words:
                translated_word = homonyms[word][1]
        else:
            translated_word = word

        translated_words.append(translated_word)

    # Join the translated words to form the final sentence
    translated_sentence = ' '.join(translated_words)

    return translated_sentence

def final(english_sentence):
    reorder_sentence = reorder(english_sentence)
    homnym = translate_homonyms_english_to_marathi(reorder_sentence)
    marathi_sentence = translate_to_marathi(homnym)
    return marathi_sentence


# In[3]:


'''Best Fitted GUI'''
import tkinter as tk
from PIL import Image, ImageTk

sentences = {
    "can": [
        "i can do this",
        "he drank soda from the can",
        "he withdraw oil from the can",
        "can you pass me the salt"
    ],
    "bat": [
        "there is a Bat on tree",
        "The Bat cave was dark",
        "He had a cricket bat",
        "That is his lucky bat"
    ],
    "bank": [
        "I need to go to the bank",
        "He deposited his money in the bank",
        "The river bank was muddy",
        "The bank robbers were caught",
        "She works at the bank"
    ],
    "sentence": [
        "The court will announce the sentence tomorrow morning",
        "I received a lengthy prison sentence for my crime",
        "The grammatical error in that sentence is quite glaring",
        "The children were told to write a sentence about their favorite animal"
    ],
    "book": [
        "I want to read a book.",
        "He wrote a book about his travels.",
        "The bookshelf was full of books.",
        "She booked a flight to Paris.",
        "The hotel was fully booked."
    ]
}

def display_can_sentences():
    sentences_text.delete("1.0", tk.END)
    sentences_text.insert(tk.END,"            <<< Sentences for can >>>"+"\n")
    for sentence in sentences["can"]:
        sentences_text.insert(tk.END, sentence + "\n")

def display_bat_sentences():
    sentences_text.delete("1.0", tk.END)
    sentences_text.insert(tk.END,"            <<< Sentences for bat >>>"+"\n")
    for sentence in sentences["bat"]:
        sentences_text.insert(tk.END, sentence + "\n")

def display_bank_sentences():
    sentences_text.delete("1.0", tk.END)
    sentences_text.insert(tk.END,"            <<< Sentences for bank >>>"+"\n")
    for sentence in sentences["bank"]:
        sentences_text.insert(tk.END, sentence + "\n")

def display_sentence_sentences():
    sentences_text.delete("1.0", tk.END)
    sentences_text.insert(tk.END,"            <<< Sentences for sentence >>>"+"\n")
    for sentence in sentences["sentence"]:
        sentences_text.insert(tk.END, sentence + "\n")

def display_book_sentences():
    sentences_text.delete("1.0", tk.END)
    sentences_text.insert(tk.END,"            <<< Sentences for book >>>"+"\n")
    for sentence in sentences["book"]:
        sentences_text.insert(tk.END, sentence + "\n")

def translate_sentence():
    english_sentence = input_field.get()
    output_label.config(text="Marathi sentence: " + final(english_sentence))

def on_sentence_click(event):
    selected_sentence = sentences_text.get("current linestart", "current lineend")
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, selected_sentence)

# Create the main window
window = tk.Tk()
window.title("English to Marathi Translator")
# photo = tk.PhotoImage(file = r"C:\Users\sarth\Downloads\colorful-Blur-Wallpapers.jpg")
window.minsize(1150, 500)
window.configure(bg='light blue')

# Create buttons for each word
can_button = tk.Button(window, text="can", command=display_can_sentences)
can_button.place(relx=0.1,rely=0.1)

bat_button = tk.Button(window, text="bat", command=display_bat_sentences)
bat_button.place(relx=0.1,rely=0.2)

bank_button = tk.Button(window, text="bank", command=display_bank_sentences)
bank_button.place(relx=0.1,rely=0.3)

sentence_button = tk.Button(window, text="sentence", command=display_sentence_sentences)
sentence_button.place(relx=0.1,rely=0.4)

book_button = tk.Button(window, text="book", command=display_book_sentences)
book_button.place(relx=0.1,rely=0.5)

# Create a text area to display the sentences
sentences_text = tk.Text(window, height=10,width=50)
sentences_text.place(relx=0.1,rely=0.6)
sentences_text.bind("<Button-1>", on_sentence_click)  # Bind the click event to the sentences_text

input_field = tk.Entry(window,width=50)
input_field.place(relx=0.6,rely=0.2)

# Create a button to trigger the translation
translate_button = tk.Button(window, text="Translate", command=translate_sentence)
translate_button.place(relx=0.6,rely=0.3)

# Create an output label to display the translated sentence
output_label = tk.Label(window, text="",font=("Arial", 20),bg="light blue")
output_label.place(relx=0.45,rely=0.5)

# Start the main event loop
window.mainloop()


# In[ ]:




