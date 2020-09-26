class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.order = 1
        
    def append(self, item):
        # adds element to buffer
        # if capacity is not full
            # append to end of list
        # else if full
            # remove oldest value
            # replace with new value
        if len(x) < self.capacity:
            self.storage[item] = self.order
        else:
            oldest_item = min(self.storage, key=self.storage.get)
            self.storage[item] = self.storage[oldest_item].pop
            self.storage[item] = self.order
        self.order += 1
        
    def get(self):
        # return the list
        pass