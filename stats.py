def num_of_words(book_string):
    words = book_string.split()
    count = len(words)
    print(f"Found {count} total words")
    
def letters_of_book(book_string):
    text = book_string.lower()
    characters = {}
    for char in list(text):
        if char in characters:
            characters[char] += 1
        else:
            characters[f"{char}"] = 1
    return characters
    
def dict_sorted(dictionary):
    records = []
    for char, count in dictionary.items():
        records.append({"char": char, "num":count})
        
    def sort_key(rec):
        return rec["num"]
    records.sort(reverse=True, key=sort_key)
    return records



