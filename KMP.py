# Dilton's Python Program for KMP Algorithm, AOA Practical Examination
# Roll No: 8865
# SE Comps-A (Practical Batch: A)

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    
    lps = [0]*M
    j = 0 # index of pattern 

    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print ("Found pattern at index: ",str(i-j)," Position: ",(int(i-j)+1))
            j = lps[j-1]
        #mismatch
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    i = 0 
    lps[0] = 0 
    j = 1
    # loop calculates lps[j] for j = 1 to M-1
    while j < M:
        if pat[j]== pat[i]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1
    print(lps)

txt = input(">> KMP Program - Author: Dilton D'souza\nEnter text: ")
pat = input("Enter pattern: ")
KMPSearch(pat, txt)
