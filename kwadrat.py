# Zadanie 4.  Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury:
# 𝑑𝑎𝑛𝑒 = [(𝑥1,𝑦1),(𝑥2,𝑦2),(𝑥3,𝑦3),...(𝑥𝑁 ,𝑦𝑁 )].
# Proszę napisać funkcję, która zwraca wartość 𝑇𝑟𝑢𝑒 jeżeli w zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach
# równoległych do osi układu współrzędnych, a wewnątrz tego kwadratu nie ma żadnych innych punktów.
# Do funkcji należy przekazać strukturę opisującą położenie punktów.

import math


def empty_square(coordinates):
    print(coordinates)
    if len(coordinates) < 4:
        return "Z tych punktów nie da się stworzyć kwadratu"
    for i, element in enumerate(coordinates):
        flag = 1
        for j in range(i+1, len(coordinates)):
            if flag == 0:
                break
            if element[0] == coordinates[j][0] and element[1] != coordinates[j][1]:
                a = element
                b = coordinates[j]
                side_len = math.fabs(element[1] - coordinates[j][1])
                for point in coordinates:
                    if flag == 0:
                        break
                    if math.fabs(point[0] - a[0]) == side_len and point[1] == a[1]:
                        c = point
                        for point2 in coordinates:
                            if flag == 0:
                                break
                            if point2[0] == c[0] and point2[1] == b[1]:
                                d = point2
                                print("\nIstnieje kwadrat z tych współrzędnych\n")
                                if a[0] > c[0]:
                                    h = a
                                    a = c
                                    c = h
                                    h = b
                                    b = d
                                    d = h
                                if a[1] < b[1]:
                                    h = a
                                    a = b
                                    b = h
                                    h = c
                                    c = d
                                    d = h
                                print(f"Jego współrzędne to:\na = {a}\nb = {b}\nc = {c}\nd = {d}\n")
                                for k, p in enumerate(coordinates):
                                    if a[0] < p[0] < c[0] and a[1] > p[1] > b[1]:
                                        print(f"W środku kwadratu znajduje się punkt {p}")
                                        flag = False
                                        break
                                    elif k == len(coordinates) - 1:
                                        print("\nW środku nie ma innego punktu\n")
                                        return True
    return "Z tych punktów nie da się stworzyć kwadratu"


# points = [(1, 5), (8, 4), (5, 5), (1, 1), (5, 1)]
# points = [(-3, 1), (1, 1), (-2, -1), (4, -2), (-3, -3), (1, -3)]
# points = [(-3, -3), (4, -2), (1, -3), (-3, 1), (1, 1), (-2, -1)]
# points = [(2, -3), (-4, -3), (-4, 3), (2, 3), (-3, 1), (1, 1)]
# points = [(-1, -1), (2, 2), (-1, 2), (1, 1), (2, -1), (6, 2), (4, 2), (4, 4), (6, 4)]
# points = [(0, 0), (0, 0), (0, 0), (0, 0)]
print(empty_square(points))
