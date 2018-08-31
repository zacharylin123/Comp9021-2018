
import copy
class FriezeError(Exception):
    def __init__(self, message):
        self.message = message

class Frieze:
    def __init__(self, filename = None):
        self.filename = filename
        file = open(filename)
        self.L = []

        for line in file:
            n = []
            for e in line.split(' '):
                if e.strip():
                    n.append(int(e))
            if n:
                self.L.append(n)

        len1 = len(self.L)
        file.close()

        # convert to binary str
        self.L2 = []
        for e in self.L:
            l1 = []
            for d in e:
                l1.append(str(bin(d)[2:].zfill(4)))
            self.L2.append(l1)

        # height
 #       print(len1)
        if (len1 < 3) or (len1 > 17):
            raise FriezeError('Incorrect input.')
        # length
        length_1 = []
        for i in range(len1):
            length_1.append(len(self.L[i]))
        for e in length_1:
            if e < 5 or e > 51:
                raise FriezeError('Incorrect input.')
        #print(length_1)
            # miss or more num

        length_2 = set(length_1)
       # print(length_2)
        if len(length_2) != 1:
            raise FriezeError('Incorrect input.')

        # num 0-15
        for a in self.L:
            for b in a:
                if b not in range(16):
                    raise FriezeError('Incorrect input.')
        ##### above is incorrect input



        # in first line, last bin should be '0000' and not up going
        if self.L[0][-1] != 0:
            raise FriezeError('Input does not represent a frieze.')
        # no up going
        for e in self.L2[0]:
            if e[-1] == '1' or e[-2] == '1':
                raise FriezeError('Input does not represent a frieze.')
        # no horizontal line in first line
        for i in range(len(self.L2[0]) - 1):
            if self.L2[0][i][1] != '1':
                raise FriezeError('Input does not represent a frieze.')

        # no down going
        for e in self.L2[-1]:
            if e[0] == '1':
                raise FriezeError('Input does not represent a frieze.')

        # no horizontal line in last line
        for i in range(len(self.L2[-1]) - 1):
            if self.L2[-1][i][1] != '1':
                raise FriezeError('Input does not represent a frieze.')

        # last num in other lines should be 0 or 1
        for i in range(1, len(self.L)):
            if not (self.L[i][-1] == 0 or self.L[i][-1] == 1):
                raise FriezeError('Input does not represent a frieze.')

        # no crossing line
        for i in range(len(self.L2) - 1):
            for j in range(len(self.L2)):
                if self.L2[i][j][0] == '1' and self.L2[i + 1][j][2] == '1':
                    raise FriezeError('Input does not represent a frieze.')

        # frieze should have period, at least period == 2
        # odd or even
        L_period = copy.deepcopy(self.L2)
        #print(L_period)
        d1 = ''
        d1 = L_period[0][-1][0] + '1' + L_period[0][-1][2] + L_period[0][-1][3]
        L_period[0][-1] = d1
        #print(L_period[0][-1])
        d2 = ''
        d2 = L_period[-1][-1][0] + '1' + L_period[-1][-1][2] + L_period[-1][-1][3]
        L_period[-1][-1] = d2
        #print(L_period)
#        L_period[0][-1][1] = '1'
#        L_period[-1][-1][1] = '1'
        len_length = len(self.L[0])
        if len_length % 2 == 0:
            len2 = len_length // 2
        else:
            len2 = (len_length - 1) // 2
        period = []
        start_point = []

        print(len_length)
        print(len2)
        for i in range(len2):
            for j in range(i + 1, len2):
                L_01 = []
                for k in range(len1):
                    if L_period[k][i: j] == L_period[k][j: j + j - i]:
                        L_01.append(1)
                    else:
                        L_01.append(0)
                if 0 not in L_01:
                    period.append(j - i)
                    #print(f'period{period}')
                    start_point.append(j)
                    #print(f'start{start_point}')
        if len_length % 2 != 0:
            for i in range(0, len2+1):
                for j in range(i + 1, len2 +1):
                    L_01 = []
                    for k in range(len1):
                        if L_period[k][i: j] == L_period[k][j: j + j - i]:
                            L_01.append(1)
                        else:
                            L_01.append(0)
                    if 0 not in L_01 and L_01:
                        period.append(j - i)
                       # print(f'i{i}')
 #                       print(f'j{j}')
                        #print(f'jjj{j + j - i}')
                        start_point.append(i)
        # period error

        if min(period) == 1:
            raise FriezeError('Input does not represent a frieze.')
        print(f'period{period}')
        print(f'start{start_point}')
        #### start and period1

        self.period1 = min(period)
        self.start = start_point[period.index(min(period))]
 #       self.start = min(start_point)
        print(f'period{self.period1}')

##        result = []
##        for j in range(len(self.L[0]) - self.period1 * 2):
##            L_start_1 = []
##            for i in range(len1):
##                if L_period[i][j: j + self.period1] == L_period[i][j + self.period1: j + self.period1 * 2]:
##                    L_start_1.append(1)
##                else:
##                    L_start_1.append(0)
##            if 0 not in L_start_1:
##                result.append(j)
##        print(result)




    def analyse(self):
        def N(x, y):
            if self.L2[x][y][-1] == '1':
                return True
            else:
                return False
        def NE(x, y):
            if self.L2[x][y][2] == '1':
                return True
            else:
                return False
        def E(x, y):
            if self.L2[x][y][1] == '1':
                return True
            else:
                return False
        def SE(x, y):
            if self.L2[x][y][0] == '1':
                return True
            else:
                return False

        # horizontal reflection, odd and even
        diagonal_h = 0
        len3 = len(self.L)
        horizontal_result = False
        if len3 % 2 == 0:
            middle = len3 // 2
            diagonal = []
            for e in self.L2[middle - 1]:
                if e[0] == '1':
                    diagonal.append(0)
                else:
                    diagonal.append(1)
            for e in self.L2[middle]:
                if e[2] == '1':
                    diagonal.append(0)
                else:
                    diagonal.append(1)
            if 0 not in diagonal:
                diagonal_h = 1
                horizontal = []
                for i in range(middle):
                    for j in range(len(self.L[0])):
                        # if it's not diagonal
                        # test E
                        if E(i, j):
                            if E(len3 - i - 1, j):
                                horizontal.append(1)
                            else:
                                horizontal.append(0)
                        if N(i, j):
                            if N(len3 - i, j):
                                horizontal.append(1)
                            else:
                                horizontal.append(0)
                        if SE(i, j):
                            if NE(len3 - i - 1, j):
                                horizontal.append(1)
                            else:
                                horizontal.append(0)
                        if NE(i, j):
                            if SE(len3 - i - 1, j):
                                horizontal.append(1)
                            else:
                                horizontal.append(0)
                if 0 not in horizontal:
                    horizontal_result = True
        else:
            horizontal = []
            len4 = (len3 - 1) // 2
            for i in range(len4 + 1):
                for j in range(len(self.L[0])):
                    if N(i, j):
                        if (len3 - i, j):
                            horizontal.append(1)
                        else:
                            horizontal.append(0)
                    if E(i, j):
                        if E(len3 - i - 1, j):
                            horizontal.append(1)
                        else:
                            horizontal.append(0)
                    if SE(i, j):
                        if NE(len3 - i - 1, j):
                            horizontal.append(1)
                        else:
                            horizontal.append(0)
                    if NE(i, j):
                        if SE(len3 - i - 1, j):
                            horizontal.append(1)
                        else:
                            horizontal.append(0)
            if 0 not in horizontal:
                horizontal_result = True
        print(f'horizontal_result{horizontal_result}')
        print(f'len3{len3}')

        # glid horizontal reflection

        glid_result = False
        glid =[[] for _ in range(len(self.L[0]) - self.period1)]
        if diagonal_h == 1 and len3 % 2 == 0:
            middle = len3 // 2
        #    glid =[[] for _ in range(len(self.L[0]) - self.period1)]

            for i in range(len(self.L[0]) - self.period1):
                for j in range(middle):
                    for k in range(i, i + self.period1 // 2):
                        # up
                        if E(j, k):
                            if E(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        # down
                        if E(len3 - j - 1, k):
                            if E(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)


                        if N(j, k):
                            if N(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if N(len3 - j - 1, k):
                            if N(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)


                        if SE(j, k):
                            if NE(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if SE(len3 - j - 1, k):
                            if NE(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)

                        if NE(j, k):
                            if SE(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if NE(len3 - j - 1, k):
                            if SE(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
        if len3 % 2 != 0:
            len5 = (len3 - 1) // 2
            for i in range(len(self.L[0]) - self.period1):
                for j in range(len5 + 1):
                    for k in range(i, i + self.period1 // 2):
                        if N(j, k):
                            if (len3 - j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if N(len3 - j, k):
                            if N(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)

                        if E(j, k):
                            if E(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if E(len3 - j - 1, k):
                            if E(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)

                        if SE(j, k):
                            if NE(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if SE(len3 - j - 1, k):
                            if NE(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)

                        if NE(j, k):
                            if SE(len3 - j - 1, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)
                        if NE(len3 - j - 1, k):
                            if SE(j, k + self.period1 // 2):
                                glid[i].append(1)
                            else:
                                glid[i].append(0)


        for e in glid:
            if 1 in e and 0 not in e:
                glid_result = True
        print(glid)
        print(f'gild_result{glid_result}')
