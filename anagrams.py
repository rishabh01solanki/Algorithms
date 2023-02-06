# Two strings are anagrams if they contain the same letters, 
# not necessarily in the same order(case does not matter)

def anagram(s1,s2):
    
    # converting the strings to lowercase and removing any spaces
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # comparing the sorted strings
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False

