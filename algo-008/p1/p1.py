def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    # print "Merging", p, q, r, A, L, R, "\n"
    i = 0
    j = 0
    inversion = 0
    for k in range(p, r + 1):
        if j > r - q - 1:
            A[k] = L[i]
            i += 1
        elif i > q - p:
            A[k] = R[j]
            j += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            # inserting R[j] before L runs out here
            inversion += (q + 1 - p) - i
    # print inversion, "\n"
    return inversion

inversion = 0
def merge_sort(A, p, r):
    global inversion
    if p < r:
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        inversion += merge(A, p, q, r)
        return inversion
    else:
        return 0
        
# x = [5, 4, 3, 2, 1]
# print merge_sort(x, 0, len(x)-1)
# x

def main():
    with open('IntegerArray.txt', 'rU') as f:
        array = f.read().strip('\n').split('\n')
        for i in range(len(array)):
            array[i] = int(array[i])
        print merge_sort(array, 0, len(array) - 1)
if __name__=='__main__':
    main()
