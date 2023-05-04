def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        word_index = (index - 1) % len(words)
        return (num_unique_words, words[word_index])
