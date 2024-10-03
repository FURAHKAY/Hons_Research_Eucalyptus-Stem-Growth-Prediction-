import numpy as np

def make_fail_table(pattern, character_dict):
    M = len(pattern)
    R = len(character_dict)
    dfa = np.zeros([R, M], int)
    dfa[character_dict.get(pattern[0])][0] = 1
    X = 0
    for j in range(1, M):
        for c in range(0, R):
            dfa[c][j] = dfa[c][X]
        dfa[character_dict.get(pattern[j])][j] = j + 1
        X = dfa[character_dict.get(pattern[j])][X]
    return dfa

def KMP_Search(text, pattern, character_dict):
    dfa = make_fail_table(pattern, character_dict)
    N = len(text)
    M = len(pattern)
    j = 0
    i = 0
    matches = []  # List to store indices of all matches found
    while i < N:
        if text[i] not in character_dict:
            i += 1
            continue
        j = dfa[character_dict.get(text[i])][j]
        i += 1
        if j == M:
            matches.append(i - M)
            j = 0  # Reset j to continue searching for next match
    return matches

# Driver code
if __name__ == "__main__":
    text = 'GCATTAGCAGATTACATAGGAGAGAAGGATCCATACAGACAGACGTATATGGATCCAACATGCATAGCATAAGAGTTAAGATAGCAAGCAGGATCCAAGCATCAGCATAGCA'
    pattern = 'GGATCC'
    character_dict = {'G': 0, 'A': 1, 'T': 2, 'C': 3}

    matches = KMP_Search(text, pattern, character_dict)
    print("Matches found at indices:", matches)

    import time
    start_time = time.time()
    matches = KMP_Search(text, pattern, character_dict)
    end_time = time.time()

    print("Matches found at indices:", matches)
    print("Time taken:", end_time - start_time, "seconds")



    print("----------------------------------------------------------------")
def KMP_Search(text, pattern, character_dict):
    matches = []  # List to store indices of all pattern matches
    
    dfa = make_fail_table(pattern, character_dict)
    N = len(text)
    M = len(pattern)
    j = 0
    i = 0
    while i < N:
        if text[i] in character_dict:
            j = dfa[character_dict[text[i]]][j]
            i += 1
            if j == M:
                matches.append(i - M)  # Store the index of the match
                j = 0  # Reset j to continue searching for more matches
        else:
            i += 1

    return matches


# Driver code
text = 'GCATTAGCAGATTACATAGGAGAGAAGGATCCATACAGACAGACGTATATGGATCCAACATGCATAGCATAAGAGTTAAGATAGCAAGCAGGATCCAAGCATCAGCATAGCA'
pattern = 'GGATCC'
character_dict = {'G': 0, 'A': 1, 'T': 2, 'C': 3}
matches = KMP_Search(text, pattern, character_dict)
print(matches)

import time
start_time = time.time()
matches = KMP_Search(text, pattern, character_dict)
end_time = time.time()
print("Matches found at indices:", matches)
print("Time taken:", end_time - start_time, "seconds")
