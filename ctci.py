

def isunique(s):
    '''
    Is Unique:
    Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
    O(n)
    '''
    '''
    Indeed, CPython's sets are implemented as something like dictionaries with dummy values (the keys being the members of the set)
    So basically a set uses a hashtable as its underlying data structure. 
    This explains the O(1) membership checking, since looking up an item in a hashtable is an O(1) operation, on average.
    '''
    counts=set()
    for i in s:
        if i in counts: return False
        counts.add(i)


def isunique2(s):
    '''
        Implement an algorithm to determine if a string has all unique characters.
        What if you cannot use additional data structures?
        if you can't use additional data structures, sort the string in place
        then iterate over it checking if adjacent characters are the same
        if no two adjacent characters are the same then all characters are unique
        O(n log n)
    '''
    s = sorted([c for c in s]) # n + n log n
    for i in range(len(s)-1): # O(n)
        if s[i] == s[i+1]:
            return False
    return True

def check_permutation(s1,s2):
    # Given two strings,write a method to decide if one is a permutation of the other.
    '''
    The strings must be the same length
    The strings must have the same characters
    More precisely each character must occur the same number of times in both strings
    '''
    if len(s1)!=len(s2): return False
    # Use dictionaries to count the number of occurrences of every character in each string
    counts_s1={}
    counts_s2={}
    for c in s1:
        if c in counts_s1:
            counts_s1[c] += 1
        else:
            counts_s1[c]  = 1
    for c in s2:
        if c in counts_s2:
            counts_s2[c] += 1
        else:
            counts_s2[c]  = 1
            
    return counts_s1 == counts_s2