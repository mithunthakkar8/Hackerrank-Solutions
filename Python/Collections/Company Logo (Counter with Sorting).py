# Import the Counter class from the collections module
# Counter is used to count occurrences of each element in an iterable
from collections import Counter  

# Entry point of the script
if __name__ == '__main__':
    # Accept input from the user
    # Input is expected to be a single string
    s = input()
    
    # Count the frequency of each character in the input string
    # The result is stored as a dictionary-like object where keys are characters and values are their counts
    letter_counter = Counter(s)
    
    # Sort the character-frequency pairs:
    # - Primary: By frequency in descending order (negative sign ensures descending sort for counts)
    # - Secondary: By character in ascending lexicographical order (default for strings)
    sorted_items = sorted(letter_counter.items(), key=lambda item: (-item[1], item[0]))

    # Print the top 3 most frequent characters along with their counts
    # Each line of output contains the character and its frequency, separated by a space
    for item in sorted_items[:3]:
        print(item[0], item[1])
