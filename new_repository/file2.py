# ushbu funksiya list korinishidagi ma`lumotlarni dic ko`rinishida 
# ifodalash uchun

def list_to_dict(lst):
    dic = {}
    for key,val in enumerate(lst):
        dic[key] = [val]
    return dic

lst = [1,2,3,4,5,6,7,8,9]
print(list_to_dict(lst))