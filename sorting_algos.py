# listx = [1,454,32352,443,6436,34754, 545435,54353463,5453]
# listx.sort()
# print(listx)

# def bubble_sort(arr):
#     #traverseaza lista
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             #schimbam cu locul elementele daca primul e mai mare ca urmatorul
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr
#
# listx = [1, 454, 32352, 443, 6436, 34754, 545435, 54353463, 5453]
# listx_bubble_sorted = bubble_sort(listx)
# print(listx_bubble_sorted)

# def insertion_sort(arr):
#     #Traversam lista incepand cu al doilea element
#     for i in range(1, len(arr)):
#         #selectam elementul curent
#         key = arr[i]
#         j = i -1
#         while key < arr[j]:
#             arr[j+1] = arr[j]
#             j = j -1 # j -= 1 sau j += -1
#
#         arr[j + 1] = key
#
#     return arr
#
# listx = [1, 454, 32352, 443, 6436, 34754, 545435, 54353463, 5453]
# listx_insertion_sort = insertion_sort(listx)
# print(listx_insertion_sort)

def merge(arr_left, arr_right):
    #intializam rezultatul
    result = []

    #initializam index pentru ambele liste
    i = j =0

    #Merge la ambele liste pana cand una din ele este goala
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            result.append(arr_left[i])
            i += 1
        else:
            result.append(arr_right[j])
            j += 1

    #Adaugam elementele ramase dupa traversarea listelor
    result.extend(arr_right[j:])
    result.extend(arr_left[i:])

    return result

def merge_sort(arr):

    #in caz in care lista are 0 sau 1 elemente, returnam lista insasi
    if len(arr) <= 1:
        return arr

    #Impartim lista in 2 subliste aprox egale
    mid = len(arr)//2 #// inseamna imprartit fara rest
    left = arr[:mid]
    right = arr[mid:]

    #sortam listele create left & right folosing functia merge_sort intr-o forma recurenta
    #recurent = se apeleaza pe ea insasi in interiorul functiei
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

listx = [1, 454, 32352, 443, 6436, 34754, 545435, 54353463, 5453]
listx_merge_sort = merge_sort(listx)
print(f"lista sortata prin merge sort = {listx_merge_sort}")
