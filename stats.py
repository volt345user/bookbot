def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_char(file_contents):
    lc_file_contents = file_contents.lower()
    letter_dict = dict()
    list_out = list()
    for x in range(0,len(lc_file_contents)): 
        
        if lc_file_contents[x] in letter_dict.keys():
            letter_dict[lc_file_contents[x]] += 1
        else:
            letter_dict[lc_file_contents[x]] = 1
    x=0
    for key in letter_dict.keys():
        list_out.append({"char": key,"num": letter_dict[key]})
        x += 1

    return list_out

def sort_on(dict_in):
    return dict_in["num"]