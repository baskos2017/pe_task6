class MyReversed:

    
    def __init__(self, list_):
        self.list = list_
        self.index = len(list_) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        boo = self.list[self.index]
        self.index -= 1

        return boo
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in MyReversed(mylist):
    print(i)