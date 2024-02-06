'''"Assign 10:  Word Frequency

Write a function which counts frequency of each word in an input string (returns the dictitionary)

(Deadline: Feb 7)

"'''
def freq_count(sentence:str)->int:
    freq = {char: sentence.count(char) for char in set(sentence)}
    return freq

'''"Assign11 :
Invert Dictionary

Write a function which returns a reversed dictionary in which the key and values are swapped.

{""Ram"":12} => {12:""Ram""}
(Deadline: Feb 7)"'''

def reverse_dict(dic:dict)->dict:
    return {val : key for key , val in dic.items()} # but herer loss of data takes place

def reverse_dict_without_dataloss(dic:dict)->dict:
    rev_dic = {}
     #{val:[key for key,value in dic.items() if val == value] for val in dic.values()}
    for key , value in dic.items():
        if value in rev_dic:
            rev_dic[value].append(key)
        else:
            rev_dic[value] = [key]
    return rev_dic

if __name__ == "__main__":

    sentence = "ayush is a good boy"
    freq_count_dict = freq_count(sentence=sentence)
    print(freq_count_dict)

    reverse = reverse_dict(freq_count_dict)
    print(reverse)
    reverse_without_data_loss = reverse_dict_without_dataloss(freq_count_dict)
    print(reverse_without_data_loss)