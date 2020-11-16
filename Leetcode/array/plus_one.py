class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l_string = map(str,digits)
        new_str = str(int("".join(l_string))+1)
        string_l = map(int,new_str)
        return(list(string_l))
        
