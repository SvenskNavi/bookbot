def main():
    print('--- Begin report of books/frankenstein.txt ---')

    text = get_text()
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_char_list = char_dict_to_sorted_list(char_dict)

    print(f'{word_count} words found in the document')

    for char in sorted_char_list:
        if char['character'].isalpha():
            print(f"The '{char['character']}' character was found {char['count']} times")

    print('--- End report ---')


def get_text():
    with open('books/frankenstein.txt') as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    character_counts = {}

    for character in text.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts


def char_dict_to_sorted_list(char_dict):
    new_list = []

    for character, count in char_dict.items():
        new_list.append({'character': character, 'count': count})

    new_list.sort(reverse=True, key=sort_on)

    return new_list


def sort_on(d):
    return d['count']


main()
