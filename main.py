def count_words(s):
    words = s.split()
    return len(words)

def letter_count(text):
    counts = {}
    for t in text.lower():
        if t.isalpha():
            if t in counts:
                counts[t] += 1
            else:
                counts[t] = 1
    dict_list = []
    for key in counts:
        dict_list.append({"name": key, "num": counts[key]})

    def sorter(dict):
        return dict["num"]
    dict_list.sort(reverse=True, key=sorter)
    # print(dict_list)
    return dict_list

def create_report(path):
    with open(path) as f:
        file_contents =f.read()
    print("-- Begin report for " + path + " --")
    print(count_words(file_contents), " words found in the document")
    letters = letter_count(file_contents)
    for dict in letters:
        print("The '{}' character was found {} times".format(dict["name"], dict["num"]))

def main():
    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     # print(file_contents)
    #     print("Word count is: ")
    #     print(count_words(file_contents))
    #     print("letter count is: ")
    #     print(letter_count(file_contents))

    create_report("books/frankenstein.txt")

if __name__ == "__main__":
    main()
