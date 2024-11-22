class TimeMap:
    # constructor initializes the hashmap
    # a key can have multiple values so to find the right value we pass it both the key and the timestamp
    # if the timestamp is not found we return the one with the closest time LESS than our timestamp
    # example: get(key,3) if key exist but no 3: return 2 if 2 exists. 
    # if key does not exist make an empty arr []

    # all the timestamps passed in our ALWAYS in increasing order, meaning we do not need to sort 
    # So to get a key and val the:
    # Time: O(log(n)) Space: O(m*n) 
    # where m: number of total keys, n: is the unique total timestamps
    def __init__(self):
        self.store = {} #key = string, value = list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []  #set the key into an empty list if it does not exist in our hashmap
        self.store[key].append([value,timestamp]) # now (knowing we have an empty list) append the pair of values passed in
        

    def get(self, key: str, timestamp: int) -> str:
        res = "" #if the key does not exist we will return an empty string
        self.value = self.store.get(key,[]) #if get finds a match with the key it will return that match, otherwise it will return an empty list

        #BINARY SEARCH TIME
        l,r = 0,len(self.value)-1

        while l <= r:
            m = (l+r)//2
            if self.value[m][1] <= timestamp:
                res = self.value[m][0] #since index m is a valid value smaller than our current val, we will set that to oue result for now
                l=m + 1
            else:
                r = m - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)