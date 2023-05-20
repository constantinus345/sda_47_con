# from collections import OrderedDict
#
# dict_ordered = OrderedDict()
# dict_ordered['cheia_1'] = 11
# dict_ordered['cheia_2'] = 2
# dict_ordered['cheia_3'] = 3
# dict_ordered['cheia_4'] = "patru"
#
# for key, value in dict_ordered.items():
#     print(f"(dict_ordered) La cheia {key} avem valoarea = {value}")
#
# #construim un dictionar clasic
# dict_unordered = dict()
# dict_unordered['cheia_1'] = 11
# dict_unordered['cheia_2'] = 2
# dict_unordered['cheia_3'] = 3
# dict_unordered['cheia_4'] = "patru"
#
# #la dictionarele clasice nu avem garantata o ordine a cheilor,
# # pot fi printate haotic, mai ales dupa operatiuni pe acel dictionar
# for key, value in dict_unordered.items():
#     print(f"(dict_unordered) La cheia {key} avem valoarea = {value}")

# frozen_setx = frozenset([1,2,3,4,2,3,1,4,5])
# print(frozen_setx, type(frozen_setx))
#
# classic_setx = set([1,2,3,4,2,3,1,4,5])
# print(classic_setx, type(classic_setx))
#
# classic_setx.add(10)
# classic_setx.remove(4)
# print(f"classic_setx new = {classic_setx}")
#
# #in frozenset nu mai putem modifica elementele!
# #frozen_setx.add(10)
# # frozen_setx.remove(4)
# # print(f"frozen_setx new = {frozen_setx}")

from collections import deque
#deque este un fel de lista, dar la care putem manipula elementele atat din stanga cat si din dreapta
elx = deque()
elx.appendleft(1)
elx.appendleft(2) #append left adauga un element la stanga colectiei
elx.append(3) #append este append la dreapta, adauga un element la dreapta colectiei
print(elx, type(elx))

elx.popleft()
print(elx, type(elx))




