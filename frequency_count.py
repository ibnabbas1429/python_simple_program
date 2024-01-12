def frequecy_count():
    word = input("Enter a string: ")
    word_list = word.split()
    dic = {}
    for word in word_list:
        if word not in dic.keys():
            dic[word] = 0
        dic[word] = dic[word] + 1
    print(dic)

frequecy_count()