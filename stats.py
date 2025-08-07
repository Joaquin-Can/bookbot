def count_words(string):
    new_list = string.split()
    return len(new_list)

def each_character_count(book_string):
    book_string = book_string.lower()
    new_dic = {}
    for character in book_string:
        if character in new_dic:
            new_dic[character] += 1
        else: new_dic[character] = 1
    return new_dic

def sort_on(items):
    return items["count"]

def get_list_dics(dic):
    new_list = []
    for key, value in dic.items():
        new_list.append({"char": key, "count": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
