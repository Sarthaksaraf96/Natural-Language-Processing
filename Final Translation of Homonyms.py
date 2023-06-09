#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Translation of Homonyms base'''
import string
import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import json


def translate_to_marathi(english_sentence):
    #getiing a dictionary of English to Marathi translations
    E2M = open(r"D:\M.SC\4SEM\NLP\NLP\Database\eng_to_mar.json",)
    english_to_marathi = json.load(E2M)
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
    elif sentence == "he withdraw oil from the can":
        words = sentence.split()
        reordered_words = [words[0], words[5],words[2], words[1]]
    elif sentence == "can you pass me the salt":
        words = sentence.split()
        words.append("why")
#         print("words :",words)
        reordered_words = [words[1], words[3],words[-2], words[2], words[0],words[-1]]
    elif sentence == "there is a bat on tree":
        words = sentence.split()
        reordered_words = [words[-1], words[3],words[0]]
    elif sentence == "The bat cave was dark":
        words = sentence.split()
        reordered_words = [words[1], words[2],words[-1],words[-2]]
    elif sentence == "His cricket bat was broken":
        words = sentence.split()
        reordered_words = [words[0], words[1],words[2],words[-1]]
    elif sentence == "That is his lucky bat":
        words = sentence.split()
        reordered_words = [words[0], words[2],words[-2],words[-1],words[1]]
    elif sentence == "i will go to the bank":
        words = sentence.split()
        reordered_words = [words[0], words[-1],words[2]]
    elif sentence == "He deposited money in the bank":
        words = sentence.split()
        reordered_words = [words[0], words[-1],words[2],words[1],words[-2]]
    elif sentence == "The river bank was muddy":
        words = sentence.split()
        reordered_words = [words[1], words[2],words[-1],words[-2]]
    elif sentence == "The river bank is dirty":
        words = sentence.split()
        reordered_words = [words[1], words[2],words[-1],words[-2]]
    elif sentence == "The court will announce the sentence tomorrow morning":
        words = sentence.split()
        reordered_words = [words[-2], words[-1],words[1],words[-3],words[3],words[2]]
    elif sentence == "accused received ten years sentence":
        words = sentence.split()
        reordered_words = [words[0], words[2],words[-2],words[-1],words[1]]
    elif sentence == "formation of this sentence is not correct":
        words = sentence.split()
        reordered_words = [words[2], words[3],words[0],words[-1],words[-2]]
    elif sentence == "this sentence is of simple past tense":
        words = sentence.split()
        reordered_words = [words[0], words[1],words[-3],words[-2],words[2]]
    elif sentence == "I will read this book":
        words = sentence.split()
        reordered_words = [words[0], words[-2],words[-1],words[2]]
    elif sentence == "He wrote a book":
        words = sentence.split()
        reordered_words = [words[0], words[-2],words[-1],words[1]]
    elif sentence == "I would like to book a table":
        words = sentence.split()
        reordered_words = [words[0], words[-2],words[-1],words[-3],words[1],words[2]]
    elif sentence == "The hotel is fully book":
        words = sentence.split()
        reordered_words = [words[1], words[-2],words[-1],words[-3]]

    # Convert the reordered list of words back to a sentence
    reordered_sentence = " ".join(reordered_words)

    # Return the reordered sentence
    return reordered_sentence

#getting the Homonyms database
hom = open(r"D:\M.SC\4SEM\NLP\NLP\Database\homonyms.json",)
homonyms = json.load(hom)
def translate_homonyms_english_to_marathi(sentence):
    # Split the sentence into individual words
    words = sentence.lower().split()
    #print(words)
    translated_words = []
    for word in words:
        if word in homonyms:
            if 'do' in words:
                translated_word = homonyms[word][0]
            elif 'oil' in words:
                translated_word = homonyms[word][1]
            elif 'salt' in words:
                translated_word = homonyms[word][0]
            elif 'soda' in words:
                translated_word = homonyms[word][1]
            elif 'tree' in words:
                translated_word = homonyms[word][0]
            elif 'cave' in words:
                translated_word = homonyms[word][0]
            elif 'cricket' in words:
                translated_word = homonyms[word][1]
            elif 'lucky' in words:
                translated_word = homonyms[word][1]
            elif 'need' in words:
                translated_word = homonyms[word][0]
            elif 'money' in words:
                translated_word = homonyms[word][0]
            elif 'go' in words:
                translated_word = homonyms[word][0]
            elif 'river' in words:
                translated_word = homonyms[word][1]
            elif 'court' in words:
                translated_word = homonyms[word][0]
            elif 'accused' in words:
                translated_word = homonyms[word][0]
            elif 'formation' in words:
                translated_word = homonyms[word][1]
            elif 'simple' in words:
                translated_word = homonyms[word][2]
            elif 'read' in words:
                translated_word = homonyms[word][0]
            elif 'wrote' in words:
                translated_word = homonyms[word][0]
            elif 'table' in words:
                translated_word = homonyms[word][1]
            elif 'hotel' in words:
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


# In[2]:


'''GUI for Translation of Homonyms'''
import tkinter as tk
import json

#getiing sentences
sen = open(r"D:\M.SC\4SEM\NLP\NLP\Database\sentences.json",)
sentences = json.load(sen)
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

eng_label = tk.Label(window, text="English Sentence",font=("Arial",15), bg = 'light blue')
eng_label.place(relx=0.46,rely=0.19)

heading_label = tk.Label(window, text="Translations of Homonyms",font=("Arial 20 underline bold"),bg="light blue")
heading_label.place(relx=0.3,rely=0.05)

# Create an output label to display the translated sentence
output_label = tk.Label(window, text="",font=("Arial", 20),bg="light blue")
output_label.place(relx=0.45,rely=0.5)

# Start the main event loop
window.mainloop()


# In[ ]:




