

def solution(x):
    # Your code here
    code={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n"}
    decode_str=""
    key_list= list(code.keys())
    value_list= list(code.values())
    for chr in x:
        if chr in key_list:
            decode_str += code[chr]
        elif chr in value_list:
            decode_str += key_list[value_list.index(chr)]
        else:
            decode_str += chr
       
    return(decode_str)

