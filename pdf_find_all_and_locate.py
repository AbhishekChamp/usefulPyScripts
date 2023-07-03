# PyPDF2==3.0.1

# This script is used for finding the word occurance inside the pdf file. It also keeps track of the index at which the word occurs.

import PyPDF2
import re


def find_word_occurrences(pdf_path, word):
    occurrences = []

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            occurrences.extend([match.start() for match in re.finditer(
                r'\b{}\b'.format(word), text, re.IGNORECASE)])

    return occurrences


# Example usage
pdf_file = 'example.pdf'  # Path to your PDF file
search_word = 'example'  # Word to search for

word_occurrences = find_word_occurrences(pdf_file, search_word)
print(f"Occurrences of '{search_word}': {len(word_occurrences)}")
print("Located at Indexes:", word_occurrences)
