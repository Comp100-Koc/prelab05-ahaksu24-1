def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    
    def check(s):  
        t = 0
        for i in range(len(s)):
            
            if (i != len(s)-1) and (s[i] == s[i+1]):
                t+=1
                
        if t == 0:
            return True
        else:
            return False


    while check(s) is False:
        new = ""
        i=0
        while i < len(s):
            if (i!= len(s)-1) and (s[i]==s[i+1]):
                i+=2
            else:
                new += s[i]
                i+=1
        s=new
    return s
