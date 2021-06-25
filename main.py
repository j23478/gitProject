#compare sort algorithm time


#mange sort algorithm list
class algorithmList:

    def __init__(self):
        self.algorithm_list = []

    def _isHave(self, algorithmName, flag = False):
        for  i in self.algorithm_list:
            if algorithmName == i:
                flag = True
                return flag
        return flag

    def add(self, algorithmName, algorithmFun):
        if not self._isHave(algorithmName):
            self.algorithm_list.append((algorithmName, algorithmFun))


#select algorithm menu
class menu:
    
    def __init__(self, algorithmList):
        self._algorithm_list = algorithmList.algorithm_list

    def display(self, lst):
        """1. xxxxxxx#
           2. xxxxxxx"""
        joinAlgorithmList = [str(index+1) + ". " +  value[0] for index, value in enumerate(self._algorithm_list)]
        print("\n".join(joinAlgorithmList))
        selectList = input("select sort algorithms : ").split(",")
        for i in selectList:
            tempList = lst[:]
            print(self._algorithm_list[int(i)-1][0])
            print(self._algorithm_list[int(i)-1][1](tempList))
            print("=================")


#manage algorithm library

if __name__ == "__main__":
    import Heapsort, Insertion_sort
    algoList = algorithmList()
    algoList.add("Heap", Heapsort.Heapsort)
    algoList.add("Insert", Insertion_sort.insertion_sort)
    m = menu(algoList)
    m.display([4,1,3,2,16,9,10,14,8,7])