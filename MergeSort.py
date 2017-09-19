# Merge Sort

#Merge sort is a recursive algorithm that continually splits a list in to the half. No matters, If the list is empty or has one item,
#If the list has more than one item, we'll split the list and recursively invoke a merge sort on both halves.
#Once the two halves are sorted, the fundamental operation, called a merge, is performed.
#Complexity : O(nlogn)

def mergeSort(alist):
    print("Splitting >>",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # Recursive call
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging >>",alist)

alist = [24,17,28,73,56,12,3,8,124,864,2,2,76,864, 10]
mergeSort(alist)
print(alist)