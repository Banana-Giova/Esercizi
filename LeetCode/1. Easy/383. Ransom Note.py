class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_list = list(ransomNote)
        magazine_list = list(magazine)
        
        for i in note_list:
            if i in magazine_list:
                if note_list.count(i) > magazine_list.count(i):
                    return False
            else:
                return False

        return True