class ds:
    def list():
        nums = [1, 2, 3, 4, 5]
        print(nums[::-1])   # reverse
        nums.append(6)
        nums.remove(3)
        print([x**2 for x in nums if x % 2 == 0])
    def Tuples():
        point = (3, 4)
        x, y = point
        print(x, y)
        from collections import namedtuple
        Student = namedtuple("Student", "name age")
        s = Student("Alice", 20)
        print(s.name, s.age)
    def set():
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}
        print(a | b)   # union
        print(a & b)   # intersection
        print(a - b)   # difference
    def dic():
        freq = {}
        s = "banana"
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        print(freq)

        squares = {x: x**2 for x in range(6)}
        print(squares)
ds.set()
























ds.list()