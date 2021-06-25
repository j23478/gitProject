def insertion_sort(lst):
    for i in range(1, len(lst)):
        while lst[i - 1] > lst[i] and i - 1 > -1:
            #swap
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i =  i - 1
    return lst




        












if __name__ == "__main__":
    a = [5,2,4,6,1,3,7,10,11,9,6,4,3]
    ans =  insertion_sort(a.copy())
    print(f"unsorted list {a}")
    print(f"sorted list {ans}")
   



