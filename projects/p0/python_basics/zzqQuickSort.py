import sys

def zzqQuickSort(lst):
    if len(lst) <= 1:
        return lst
    larger = [x for x in lst[1:] if x > lst[0]]
    smaller = [x for x in lst[1:] if x <= lst[0]]
    # print larger
    # print smaller
    return zzqQuickSort(larger) + [lst[0]] + zzqQuickSort(smaller)

if __name__ == '__main__':
    # lst = [1,5,2,4,3,5,4,3,2,4,3,2,1]
    lst = eval(sys.argv[1])
    print 'the original dataset is:'
    print lst
    print 'the result of quick sort is:'
    print zzqQuickSort(lst)
    # print 'the system args is:'
    # print sys.argv