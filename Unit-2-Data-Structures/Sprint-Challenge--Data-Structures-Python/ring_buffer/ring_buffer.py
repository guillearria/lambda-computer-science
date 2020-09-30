class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.item_storage = []
        self.order_storage = []
        self.order = 1
        
    def append(self, item):
        if len(self.item_storage) < self.capacity:
            self.item_storage.append(item)
            self.order_storage.append(self.order)
        else:
            min_order = min(self.order_storage)
            oldest_index = self.order_storage.index(min_order)
            self.item_storage[oldest_index] = item
            self.order_storage[oldest_index] = self.order
        self.order += 1

    def get(self):
        return self.item_storage