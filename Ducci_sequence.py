'''
takes a starting list of integers and a number ‘n’ as input, and returns the nth element of the Ducci sequence
'''
def ducci_sequence(test_list,n):
    temp_list=[]
    for i in range(0,len(test_list)):
        if i == 3:
            temp_list.append(abs(test_list[0]-test_list[3]))
        else:
            j = abs(test_list[i]-test_list[i+1])
            temp_list.append(j)

    if n == 0:
        return temp_list
    else:
        final_list = ducci_sequence(temp_list,n-1)
    return final_list

ducci_element=ducci_sequence([7, 60, 861, 3070] , 3)
print(ducci_element)