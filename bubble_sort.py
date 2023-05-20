def binary_search(arr, target):
    #initializam index de start si index de final
    start = 0
    end = len(arr) - 1

    #Implimentam un while care va imparti lista in jumate pana gaseste numarul
    while start <= end:
        #calculam indexul de mijloc
        mid = (start+end)//2 # // inseamna impartire fara rest, intreaga

        #Compar elementul din mijloc cu target value
        if arr[mid] == target:
            return mid #mid este indexul
        elif arr[mid] < target:
            # daca mijocul e mai mic ca target, vom considera lista din dreapta
            start = mid + 1
        else:
            #implicit daca mijlocul e mai mare ca target, vom considera lista din stanga
            end = mid - 1

    return 'Not found'

lista_mea = [1,2,5,7,8,12,34,59]
target = 89
index_el = binary_search(lista_mea, target)
print(index_el)