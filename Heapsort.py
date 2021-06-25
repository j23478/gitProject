#note root of tree: first element in the array, corresponding to i = 1
# parent(i) =i/2: returns index of node's parent
# left(i)=2i: returns index of node's left child
# right(i)=2i+1: returns index of node's right child





#build_max_heap 
def build_max_heap(lst):
    #from n/2 to 1 剛好可排除leaf
    lst.insert(0, 0)
    n = int((len(lst) - 1)/2)
    for i in range(n, 0, -1):
        max_heapify(lst, i)    



#max_heapify correct a single violation of the heap property in a subtree at its root
def max_heapify(lst, parentindex):
    #不管index = 0
    #find max value
    leftchild = 2 * parentindex
    rightchild = 2 * parentindex + 1
    
    largestindex = parentindex

    if  (rightchild <= len(lst) - 1):
        if (lst[parentindex] <= lst[rightchild]):
            largestindex = parentindex
        else:
            largestindex = rightchild

    if (leftchild <= len(lst) - 1) and (lst[leftchild] < lst[largestindex]):
        largestindex = leftchild

    #exhange
    if largestindex != parentindex:
        lst[parentindex],  lst[largestindex] = lst[largestindex], lst[parentindex]
        #有交換時要往下檢查
        max_heapify(lst, largestindex)


#Heapsort

def Heapsort(lst):
    ans = []
    #build
    build_max_heap(lst)

    while 1 < len(lst):
        #find maximum element lst[1] and swap element lst[n] and lst[1] 把maximum 換到最後面
        lst[1],  lst[-1] = lst[-1], lst[1]
        #discard node n form heao
        ans.append(lst.pop())
        #run max_heap to fix
        max_heapify(lst, 1)
    return ans




if __name__ == "__main__":
    A = [4,1,3,2,16,9,10,14,8,7]
    
    print(Heapsort(A))
