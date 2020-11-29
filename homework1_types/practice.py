# def idiotic_str(input_str):
#     idiotic_str =  ""
#     for i, c in enumerate(input_str):
#         idiotic_str += c if not i % 2 else c.upper()
#     return idiotic_str

# idiotic_str("Chto Proishodit?") 

# def filter_unique_int(input_list) :
#     unique_list = list(set(input_list))
#     return unique_list

# def avg_score(score_list):
    
#     avg_score1 = score_list.split('|')
#     avg_score = f"{avg_score1[0]}|{str(sum(str(avg_score1[1]).split(', ')) / len(str(avg_score1[1]).split(', ')))}"
#     return avg_score

# print(avg_score("Mike|83, 90, 34, 54",))

def DNA_pair(chain):
    map =  {'A' : 'T',
            'T' : 'A',
            'C' : 'G',
            'G' : 'C'}
    pair = [map[i] for i in chain]
    return ''.join(pair)
result = DNA_pair("ATTGC")
print(result)