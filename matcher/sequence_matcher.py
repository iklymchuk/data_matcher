# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import SequenceMatcher

#Function for retriving definition
def retrive_definition(first_word, second_world):
    return SequenceMatcher(None, first_word, second_world).ratio()

#Input from user
first_word_user = input("Enter first word: ")
second_word_user = input("Enter second word: ")

#Retrive the definition using function and print the result
print(retrive_definition(first_word_user, second_word_user))