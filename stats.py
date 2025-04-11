import sys

def get_word_count(contents):
    return len(contents.split())



def get_character_counts(contents):
    characters = {}
    for char in contents:
        if char.isalpha():
            if char.lower() in characters:
                characters[char.lower()] += 1
            else:
                characters[char.lower()] = 1

    return characters


def sort_on(dict):
    return dict["count"]


def make_report(contents):

    my_characters = get_character_counts(contents)
    my_character_list = []


    for character in my_characters:
        my_character_list.append({"character": character, "count": my_characters[character]})
    
    my_character_list.sort(reverse=True, key=sort_on)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(contents)} total words")
    print("--------- Character Count -------")
    for dict in my_character_list:
        print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")