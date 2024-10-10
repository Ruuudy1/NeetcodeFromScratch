class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26 #make empty arrays to store matches
        for i in range(len(s1)):  
            s1Count[ord(s1[i]) - ord("a")] += 1  #get the ascii val of the char and sub a to map correctly
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0  # check the number of matches 

        l = 0
        for r in range(len(s1), len(s2)):  #sliding window
            if matches == 26:  #if matches is 26 every char in the sliding window is matching with the other string
                return True #this means that out of the 26 lowercase chars, they all have the same num of matching characters 

            index = ord(s2[r]) - ord("a") #ADDS A CHAR TO THE RIGHT OF OUR WINDOW
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: 
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")  #ADDS A CHAR TO THE LEFT OF OUR WINDOW
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1           #slide the sliding window
        return matches == 26
