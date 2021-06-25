#compare sort algorithm time


#sort algorithm list

#select algorithm menu
class menu:
    
    def __init__(self, algorithmList):
        self._algorithm_list = algorithmList

    def display(self, lst):
        """1. xxxxxxx#
           2. xxxxxxx"""
        joinAlgorithmList = [str(index+1) + ". " +  value[0] for index, value in enumerate(self._algorithm_list)]
        print("\n".join(joinAlgorithmList))
        selectList = input("select sort algorithms : ").split(",")
        for i in selectList:
            print(self._algorithm_list[int(i)-1][0])
            print(self._algorithm_list[int(i)-1][1](lst))


#manage algorithm library

if __name__ == "__main__":
    import Heapsort, Insertion_sort, countingSort
    algorithmList = [("Insert", Insertion_sort.insertion_sort), ("Heap", Heapsort.Heapsort)]
    m = menu(algorithmList)
    m.display([4,1,3,2,16,9,10,14,8,7])