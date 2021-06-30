
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
import time
class menu:
    
    def __init__(self, algorithmList):
        self._algorithm_list = algorithmList.algorithm_list

    @staticmethod
    def run(func, lst):
        start = time.process_time()
        result = func(lst)
        end = time.process_time()
        return result, end - start


    def display(self):
        """1. xxxxxxx#
           2. xxxxxxx"""
        joinAlgorithmList = [str(index+1) + ". " +  value[0] for index, value in enumerate(self._algorithm_list)]
        print("\n".join(joinAlgorithmList))
        selectList = input("select sort algorithms : ").split(",")
        lst = [ int(_) for _ in input("lst: ").split(",")]
        for i in selectList:
            tempList = lst[:]
            print(self._algorithm_list[int(i)-1][0])
            result, spend = self.run(self._algorithm_list[int(i)-1][1], tempList)
            print(f"Result: {result[:10]}.... \nSpending time: {spend}")
            print("=================")


#manage algorithm library dynamic loading

if __name__ == "__main__":
    import Heapsort, Insertion_sort
    algoList = algorithmList()
    algoList.add("Heap", Heapsort.Heapsort)
    algoList.add("Insert", Insertion_sort.insertion_sort)
    m = menu(algoList)
    m.display()