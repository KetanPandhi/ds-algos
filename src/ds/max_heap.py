class Max_Heap:

    def __init__(self, arr=[]):
        self.__array = arr
        if len(self.__array) > 0:
            self.__heapify()

    def __heapify(self):
        for i in reversed(range(self.__get_parent_index(len(self.__array) - 1) + 1)):
            print("-> " + str(i))
            self.__sink(i)

    def __swap(self, index1, index2):
        temp = self.__array[index1]
        self.__array[index1] = self.__array[index2]
        self.__array[index2] = temp

    def __get_parent_index(self, index):
        return int((index - 1) / 2)

    def __get_child_l_index(self, index):
        return 2 * index + 1

    def __sink(self, index):
        child_index = self.__get_child_l_index(index)
        arr_len = len(self.__array)
        if child_index >= arr_len:
            return
        if child_index < arr_len - 1:
            if self.__array[child_index] < self.__array[child_index + 1]:
                child_index = child_index + 1
        if self.__array[child_index] > self.__array[index]:
            self.__swap(index, child_index)
            return self.__sink(child_index)
        return

    def __swim(self, index):
        if index == 0:
            return
        else:
            parent_index = self.__get_parent_index(index)
            if self.__array[parent_index] < self.__array[index]:
                self.__swap(index, parent_index)
            return self.__swim(parent_index)

    def push(self, val):
        self.__array.append(val)
        self.__swim(len(self.__array) - 1)

    def display(self):
        print(self.__array)

    def pop(self):
        arr_len = len(self.__array)
        if arr_len == 0:
            return None
        if arr_len == 1:
            return self.__array.pop()
        self.__swap(len(self.__array) - 1, 0)
        ret_val = self.__array.pop()
        self.__sink(0)
        return ret_val


heap = Max_Heap()

heap.push(30)
heap.display()
heap.push(2)
heap.display()
heap.push(45)
heap.display()
heap.push(15)
heap.display()
heap.push(25)
heap.display()
heap.push(33)
heap.display()
heap.push(5)
heap.display()
heap.push(19)
heap.display()
heap.push(32)

heap.display()
print(heap.pop())

heap.display()
print(heap.pop())

heap.display()
print(heap.pop())

heap.display()
print(heap.pop())


heap.display()
print(heap.pop())

heap.display()
print(heap.pop())

heap.display()

d = Max_Heap([11, 41, 23, 37, 45, 78, 12, 34, 32, 21, 67, 54])
d.display()
print(d.pop())
print(d.pop())
print(d.pop())
print(d.pop())
print(d.pop())
print(d.pop())

print(d.pop())
print(d.pop())
print(d.pop())
d.display()
