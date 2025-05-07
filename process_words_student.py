import pygame
import random

word_map = {}

# this is for display you can ignore it
pygame.init()

# Setup Pygame window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tag Cloud")

# this reads the file in to an list of words split by word
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
    return words


# this removes special characters(e.g. !, ', ., etc)
# from each word
def remove_special_characters(words):
    for index, word in enumerate(words):
        for spec in ["!", ..., ...]: # add whatever characters you want  to get rid of
             words[...] = word.replace(..., "") # replace with empty character
    return words


# this makes every word lower case
def to_lower_case(words):
    for index, word in enumerate(words):
        words[...] = ...
    return words

# this removes words that have no significance to our 
# determining the meaning of the passage -- (e.g. "of", "is", etc)
def remove_insignificant_words(words):
    temp_words = []
    for word in ...:
        if not ... in ["of", "is"]: # add whatever words you want to get rid of
            temp_words.append(...)
    return ...

# this takes the word list counts the occurances of each word 
# the final structure is a dictionary in which the word is the key and 
# the number of occurances is the value
# {
#   "word1": 10,
#   "word2": 5
# }
def put_in_map(words):
    for word in words:
        if ... in ...: # word exists in map - add 1
            word_map[...] = word_map[...] + 1
        else: # word does not exist so set it to 1
            word_map[...] = 1 

# this removes words from the map that have less then 
# the num_chars parameter
def remove_low_occurance_words(num_chars):
    for key in list(word_map.keys()):
        if word_map[...] < ...:
            del word_map[...]


# this displays each word at a random place, with a random color
# and a font size that bigger is the word happens more often
def display_words():
    screen.fill((255, 255, 255))  # White background

    for word, count in word_map.items():
        # Random position - In pygame the top-left corner is 0, 0
        x = random.randint(..., ...)
        y = random.randint(..., ...)

        # Random color
        color = (
            random.randint(..., ...),
            random.randint(..., ...),
            random.randint(..., ...)
        )

        # Text size tied to count (you can adjust the scale)
        # come up with function that sets font_size based number of occurances
        font_size = ...   # cap at 72 pt  
        font = pygame.font.SysFont(None, font_size)

        # Render the text
        text_surface = font.render(word, True, color)
        screen.blit(text_surface, (x, y))

    pygame.display.flip()

# this is the main method that drives the application
def process_words():
    file_path = "speech.txt"
    # process the words from the speech
    words = read_file(file_path)
    # print(words)
    # words = remove_special_characters(words)
    # words = to_lower_case(words)
    # words = remove_insignificant_words(words)

    # # count the number of occurances and put in map
    # put_in_map(words)
    # remove_low_occurance_words(10)
    
    # print(word_map)

    # display_words()

    # # keeps window open until you close it
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    # pygame.quit()
    
process_words()
