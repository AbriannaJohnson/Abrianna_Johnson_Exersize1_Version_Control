# Abrianna Johnson
# 10/19/25

# The function prompts the user to enter a paragraph,
# then separates the sentences from the paragraph using a pattern and
# adds up the total of sentences in the paragraph and displays the results.

import re

def get_paragraph():
    # Prompt the user to enter their paragraph
    s = input('Enter your paragraph: ')
    # Return the user's input
    return s

def analyze_paragraph():
    # Get the paragraph input from the previous function
    sentence = get_paragraph()
    # Create a pattern that can identify each sentence in the paragraph
    # including sentences that start with numbers.
    pat = r'[A-Z, 1-9].*?[.!?](?= [A-Z, 1-9]|$)'
    sentences = re.findall(pat, sentence, flags=re.DOTALL | re.MULTILINE)
    # Create a for loop that identifies the sentences and adds 1 to the count of sentences
    for i, sentence in enumerate(sentences):
        # Display each sentence in number order
        print(f'Sentence {i + 1}: {sentence}')
    # Display the total number of sentences in the paragraph
    print(f'\nTotal number of sentences: {len(sentences)}')



if __name__ == "__main__":
    # Call the analyze_paragraph function to start the loop
    analyze_paragraph()