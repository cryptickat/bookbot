def num_words(string):
    return len(string)


def same_characters(string):
    text = string.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sorted_list(dictionary):
    result = []
    for key, value in dictionary.items():
      result.append({"char": key, "num": value})
    
    result.sort(reverse=True, key=sort_on)

    for item in result:
        print(f"{item['char']}: {item['num']}")
    