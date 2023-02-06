# a palindrome is word that reads the same backwards eg, wow

def palindrome(s1):
    
    if s1.lower() == s1[::-1].lower():
        return True
    else:
        return False