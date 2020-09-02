def solution(s):

    to_right=salutes=0

    for person in s:

        if (person=="<" and right >0):
            salutes += 2*to_right
        if (person==">"):
            to_right+=1
    return salutes
