cube = ['w','w','w','w','w','w','w','w','w',
        'o','o','o','o','o','o','o','o','o',
        'g','g','g','g','g','g','g','g','g',
        'r','r','r','r','r','r','r','r','r',
        'b','b','b','b','b','b','b','b','b',
        'y','y','y','y','y','y','y','y','y',]
#clockwise moves
def R():
    cube[2],cube[20],cube[47],cube[42] = cube[20],cube[47], cube[42],cube[2]
    cube[5],cube[23],cube[50],cube[39] = cube[23],cube[50],cube[39],cube[5]
    cube[8],cube[26],cube[53],cube[36] = cube[26],cube[53],cube[36],cube[8]
    cube[27],cube[29],cube[35],cube[33] = cube[29],cube[35],cube[33],cube[27]
    cube[30],cube[28],cube[32],cube[34] = cube[28],cube[32],cube[34],cube[30]
def L():
    cube[0],cube[18],cube[45],cube[44] = cube[44],cube[0], cube[18],cube[45]
    cube[3],cube[21],cube[48],cube[41] = cube[41],cube[3],cube[21],cube[48]
    cube[6],cube[24],cube[51],cube[38] = cube[38],cube[6],cube[24],cube[51]
    cube[9],cube[11],cube[17],cube[15] = cube[11],cube[9],cube[11],cube[17]
    cube[10],cube[14],cube[16],cube[12] = cube[12],cube[10],cube[14],cube[16]
def U():
    cube[9],cube[18],cube[27],cube[36] = cube[18],cube[27], cube[36],cube[9]
    cube[10],cube[19],cube[28],cube[37] = cube[19],cube[28],cube[37],cube[10]
    cube[11],cube[20],cube[29],cube[38] = cube[20],cube[29],cube[38],cube[11]
    cube[0],cube[2],cube[8],cube[6] = cube[6],cube[0],cube[2],cube[8]
    cube[3],cube[1],cube[5],cube[7] = cube[7],cube[3],cube[1],cube[3]
def D():
    cube[24],cube[33],cube[42],cube[15] = cube[15],cube[24], cube[33],cube[42]
    cube[25],cube[34],cube[43],cube[16] = cube[16],cube[25],cube[34],cube[43]
    cube[26],cube[35],cube[44],cube[17] = cube[17],cube[26],cube[35],cube[44]
    cube[45],cube[47],cube[53],cube[51] = cube[51],cube[45],cube[47],cube[53]
    cube[46],cube[50],cube[52],cube[48] = cube[48],cube[46],cube[50],cube[52]
def F():
    cube[6],cube[27],cube[47],cube[17] = cube[17],cube[6], cube[27],cube[47]
    cube[7],cube[30],cube[46],cube[14] = cube[14],cube[7],cube[30],cube[46]
    cube[8],cube[33],cube[45],cube[11] = cube[11],cube[8],cube[33],cube[45]
    cube[18],cube[20],cube[26],cube[24] = cube[24],cube[18],cube[20],cube[26]
    cube[19],cube[23],cube[25],cube[21] = cube[21],cube[19],cube[23],cube[21]
def B():
    cube[0],cube[29],cube[53],cube[15] = cube[29],cube[53], cube[15],cube[0]
    cube[1],cube[32],cube[52],cube[12] = cube[32],cube[52],cube[12],cube[1]
    cube[2],cube[35],cube[51],cube[9] = cube[35],cube[51],cube[9],cube[2]
    cube[37],cube[41],cube[43],cube[39] = cube[39],cube[37],cube[41],cube[43]
    cube[36],cube[38],cube[44],cube[42] = cube[42],cube[36],cube[38],cube[44]
#double moves
def R2():
    R()
    R()
def U2():
    U()
    U()
def L2():
    L()
    L()
def F2():
    F()
    F()
def B2():
    B()
    B()
def D2():
    D()
    D()
#counterclockwise moves
def Rprime():
    R()
    R()
    R()
def Uprime():
    U()
    U()
    U()
def Lprime():
    L()
    L()
    L()
def Dprime():
    D()
    D()
    D()
def Fprime():
    F()
    F()
    F()
def Bprime():
    B()
    B()
    B()
#slice moves



