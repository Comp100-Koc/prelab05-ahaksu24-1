def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest = ""

    for i in range(len(s)):
        for j in range((i+2),len(s)):
            sub = s[i:j]

            if sub == sub[::-1]:
                if len(sub)>= len(longest):
                    longest = sub
    return longest
    
                

