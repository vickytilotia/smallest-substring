# This is a python program for smallest substrig
# with maximum distinct characters

from collections import defaultdict

# function "findSubString" will return the desired string.

def FindSubString(given_str):
    str_distinct=set([x for x in given_str]) #total distinct char in given_string
    distinct_char=len(str_distinct)          #length of total distinct char


    count=0
    start=0
    start_index=-1
    min_len =999999999

#     here we used python defaultdict,
#     The functionality of both dictionaries and defualtdict
#     are almost same except for the fact that defualtdict never raises a KeyError

    curr_count = defaultdict(lambda:0)  #lambda:0 so that default value of each key equals to zero

    for i in range(len(given_str)):
        curr_count[given_str[i]] +=1



        if curr_count[given_str[i]]==1:
            count +=1 # count increment on each new distinct character

#       below code will try to minimize substring
        if count == distinct_char:
            while curr_count[given_str[start]]>1:
                if curr_count[given_str[start]]>1:
                    curr_count[given_str[start]]-=1
                start+=1

#           updating substring size
            len_substring =i -start +1
            if min_len>len_substring:
                min_len= len_substring
                start_index = start

    what_we_want = given_str[start_index:start_index + min_len]
    return len(what_we_want)




if __name__=='__main__':

    print(FindSubString(input()))
