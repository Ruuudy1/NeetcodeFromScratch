class KthLargest:

    # heapify the list of numbers and kth largest 
    # add and pop in Log(n) time and O(1) to lookup min with a min heap
    # we are only adding elements not removing so heap is fast
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k #minheap with k largest integers
        heapq.heapify(self.minHeap) #make the variable a heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #pop the smallest value
        return self.minHeap[0] #the min value is in the 0th index