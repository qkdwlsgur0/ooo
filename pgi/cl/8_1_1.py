#_______________________________ 삽입정렬 ________________________________ 

def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left+[x]+ss
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left


def insertion_sort(xs):
    if xs != []:
        return insert(xs[0],xs[1:])
    else:
        return []
# 꼬리재귀 아님

def insertion_sort(xs):
    def loop(xs,ss):
        if xs != []:
            return loop(xs[1:],insert(xs[0],ss))
        else:
            return ss
    return loop(xs,[])
# 꼬리재귀

def insertion_sort(xs):
    ss = []
    while xs != []:
        ss = insert(xs[0],ss)
        xs = xs[1:]
    return ss


def insertion_sort(xs):
    ss = []
    for i in xs:
        ss = insert(i,ss)
    return ss


#_______________________________ 합병정렬 ________________________________
 
def merge(left,right):
    if not (left == [] or right == []):
        if left[0] >= right[0]:
            return [right[0]]+merge(left,right[1:])
        else:
            return [left[0]]+merge(left[1:],right)
    else:
        left+right

def merge(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                return loop(left[1:],right,ss+[left[0]])
            else:
                return loop(left,right[1:],ss+[right[0]])
        else:
            return ss+left+right
    return loop(left,right,[])

def merge(left,right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    return ss+left+right


def merge_sort(xs):
    mid = len(xs)//2
    if len(xs) >= 2 :
        return merge(merge_sort(xs[:mid]),merge_sort(xs[mid:]))
    else:
        return xs


#________________________________ 퀵정렬 ________________________________ 

def partition(pivot,xs):
    if xs != []:
        left, right = partition(pivot,xs[1:])
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []

def partition(pivot,xs):
    def loop(xs,left,right):
        if xs != []:
            if xs[0] <= pivot:
                left.append(xs[0])
            else:
                right.append(xs[0])
            return loop(xs[1:],left,right)
        else:
            return left,right
    return loop(xs,[],[])

def partition(pivot,xs):
    left, right = [], []
    while xs != []:
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        xs = xs[1:]
    return left, right

def partitton(pivot,xs):
    left, right = [], []
    for x in xs:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right


def quicksort(xs):
    if len(xs) > 1:
        pivot = xs[0]
        left, right = partition(pivot,xs[1:])
        return quicksort(left)+[pivot]+quicksort(right)
    else:
        return xs

print(quicksort([9,8,7,6,4,5,3,2,1]))