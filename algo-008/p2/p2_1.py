comp = 0


def partition(A, p, r):
    global comp
    i = p + 1
    for j in range(p+1, r+1):
        comp += 1
        if A[j] <= A[p]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            # print i, j, A
    temp = A[i-1]
    A[i-1] = A[p]
    A[p] = temp
    # print i+1, A
    return i - 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

# A = [2, 8, 7, 1, 3, 5, 6, 4]
# quicksort(A, 0, len(A)-1)
# A


def main():
    with open('QuickSort.txt', 'rU') as f:
        array = f.read().strip('\n').split('\n')
        for i in range(len(array)):
            array[i] = int(array[i])
        quicksort(array, 0, len(array)-1)
        print comp
        # print array
if __name__ == '__main__':
    main()
