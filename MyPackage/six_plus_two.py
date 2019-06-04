def uc_6_2(first_name,last_name):
    if (len(last_name)>=6):
        sixplus2 = last_name[0:6] + first_name[0] + first_name[-1]
    else:
        sixplus2 = last_name + first_name[0:(6-len(last_name)+1)] + first_name[-1]
    return(sixplus2.lower())