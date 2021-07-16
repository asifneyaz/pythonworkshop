def duplicate_count(text):
    text = text.lower()
    duplicate = []
    for char in text:
        if text.count(char) > 1 and char not in duplicate:
                duplicate.append(char)
    return len(duplicate)


print(duplicate_count("abbcdeaaaaabbb89ccAADD"))