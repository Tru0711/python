target_word = "python"  # Replace with the word you want to count
word_count = 0

with open(r'SampleFile.txt', 'r') as file:
    data = file.read()
    words = data.split()

    for word in words:
        if word.lower() == target_word.lower():
            word_count += 1

print(f"The word '{target_word}' appears {word_count} times.")