
def output_table(table, str1, str2):
    print("\n   ", end = " ")
    for i in str2:
        print(i, end = " ")

    for i in range(len(table)):
        if i:
            print("\n" + str1[i-1], end = " ")
        else:
            print("\n ", end = " ")
        for j in range(len(table[i])):
            print(table[i][j], end = " ")
    print("\n")


def levenshtein(str1, str2):
    len_i = len(str1) + 1
    len_j = len(str2) + 1
    table = [[i + j for j in range(len_j)] for i in range(len_i)]
    
    for i in range(1, len_i):
        for j in range(1, len_j):
            forfeit = 0 if (str1[i - 1] == str2[j - 1]) else 1
            table[i][j] = min(table[i - 1][j] + 1,
                              table[i][j - 1] + 1,
                              table[i - 1][j - 1] + forfeit)
          
    output_table(table, str1, str2)
    return(table[-1][-1])


def damerau_levenshtein(str1, str2):
    len_i = len(str1) + 1
    len_j = len(str2) + 1
    table = [[i + j for j in range(len_j)] for i in range(len_i)]
    
    for i in range(1, len_i):
        for j in range(1, len_j):
            forfeit = 0 if (str1[i - 1] == str2[j - 1]) else 1
            table[i][j] = min(table[i - 1][j] + 1,
                              table[i][j - 1] + 1,
                              table[i - 1][j - 1] + forfeit)
            if (i > 1 and j > 1) and str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
                table[i][j] = min(table[i][j], table[i-2][j-2] + 1)
     
    output_table(table, str1, str2)
    return(table[-1][-1])


def get_strings_and_run(function, output = False):
    print(function)
    str1 = input("Input str1: ")
    str2 = input("Input str2: ")
    distance = function(str1, str2)
    print("Distance == ", distance)
           
            
if __name__ == "__main__": 
    get_strings_and_run(levenshtein)
    get_strings_and_run(damerau_levenshtein)
    