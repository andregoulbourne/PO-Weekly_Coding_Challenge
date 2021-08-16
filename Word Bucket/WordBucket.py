def bucketize(string, count):
    result = []
    temp = ""
    addedString = ""
    list_of_words = string.split()
    for i in range(len(list_of_words)+2):
        if i == len(list_of_words)+1:
             if 0 <= i < len(list_of_words):
                addedString += list_of_words[i] + " "
             result.append(cut_last_character(temp))

        if len(addedString)-1 > count:
            result.append(cut_last_character(temp))
            if 0 <= i - 1 < len(list_of_words):
                addedString = list_of_words[i-1]+" "
            temp = ""
        if i < len(list_of_words):
            addedString += list_of_words[i] + " "
        if 0 <= i-1 < len(list_of_words):
            temp += list_of_words[i-1]+" "
    return result


def cut_last_character(string):
    result = ""
    for l in range(len(string) - 1):
        result += string[l]
    return result