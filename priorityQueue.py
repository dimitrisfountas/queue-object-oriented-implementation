from _heapq import heappush, heappop, heapreplace


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.count = 0

    def push(self, item, priority):
        self.item = item
        self.priority = priority
        heappush(self.pq, (priority, item))
        self.count += 1

    def pop(self):
        self.tup = heappop(self.pq)
        self.count -= 1
        return (self.tup[1])

    def isEmpty(self):
        return (self.count == 0)


    def update(self, item, priority):
        inside = False
        l = []
        while True and len(self.pq):
            temp = heappop(self.pq)
            if item == temp[1] and priority < temp[0]:
                heappush(self.pq, (priority, item))
                inside = True
                break
            else:
                l.append(temp)
        for i in range(len(l)):
            tup = l.pop()
            heappush(self.pq, tup)
        if inside == False:
            self.count += 1
            heappush(self.pq, (priority, item))









def PQSort(l):
    h = PriorityQueue()
    count=0
    for number in l:
        h.push(number, number)
        count+=1
    l.clear()
    for i in range(count):
        sort=h.pop()
        l.append(sort)
    return l







