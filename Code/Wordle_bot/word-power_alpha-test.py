from collections import defaultdict
import string

def count_letter_positions(words):
    # Initialize a dictionary to hold counts of letters at each position
    position_counts = defaultdict(lambda: defaultdict(int))
    
    # Iterate over each word and its position index
    for word in words:
        for index, letter in enumerate(word.lower()):
            if letter in string.ascii_lowercase:
                position_counts[index][letter] += 1

    # Convert defaultdict to a regular dict for easier handling/display
    position_counts = dict(position_counts)
    
    return position_counts

# Example usage
words = ["Hello", "world", "Python", "is", "great"]
position_counts = count_letter_positions(words)

for position, counts in position_counts.items():
    print(f"Position {position}:")
    for letter, count in sorted(counts.items()):
        print(f"  {letter}: {count}")