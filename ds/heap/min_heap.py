"""
                    0
            1               3
        15      7       8       9
    22

heap = [0, 1, 3, 15, 7, 8, 9, 22]
Index:  0, 1, 2, 3 , 4, 5, 6 , 7
"""
import sys


class MinHeap:

    def __init__(self):
        self.heap = []

    def heapify_down(self, root_index=0):
        left = 2*root_index + 1
        right = 2*root_index + 2
        min_index = root_index
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if min_index != root_index:
            self.heap[min_index], self.heap[root_index] = self.heap[root_index], self.heap[min_index]
            self.heapify_down(min_index)

    def heapify_up(self, index):
        if index == 0:
            return
        parent = (index - 1) / 2
        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
        self.heapify_up(parent)

    def display(self):
        print(self.heap)

    def heappush(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def heappop(self):
        top = self.heap[0]
        self.heap[0] = sys.maxsize
        self.heapify_down()
        return top


if __name__ == '__main__':
    heap = MinHeap()
    heap.heappush(15)
    heap.heappush(3)
    heap.heappush(1)
    heap.heappush(0)
    heap.heappush(7)
    heap.heappush(8)
    heap.heappush(9)
    heap.heappush(22)
    heap.heappush(4)
    heap.heappush(-1)
    heap.display()
    assert heap.heappop() == -1
    assert heap.heappop() == 0
    assert heap.heappop() == 1
    assert heap.heappop() == 3
    assert heap.heappop() == 4
    assert heap.heappop() == 7
    assert heap.heappop() == 8
    assert heap.heappop() == 9
