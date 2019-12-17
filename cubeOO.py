from re import findall as fa
class Cube:
    state = ['w','w','w','w','w','w','w','w','w',
    'o','o','o','o','o','o','o','o','o',
    'g','g','g','g','g','g','g','g','g',
    'r','r','r','r','r','r','r','r','r',
    'b','b','b','b','b','b','b','b','b',
    'y','y','y','y','y','y','y','y','y']
    def __init__(self,moves=''):
        self.doMoves(moves)

    #regular moves   
    def R(self):
        self.state[2],self.state[20],self.state[47],self.state[42] = self.state[20],self.state[47], self.state[42],self.state[2]
        self.state[5],self.state[23],self.state[50],self.state[39] = self.state[23],self.state[50],self.state[39],self.state[5]
        self.state[8],self.state[26],self.state[53],self.state[36] = self.state[26],self.state[53],self.state[36],self.state[8]
        self.state[27],self.state[29],self.state[35],self.state[33] = self.state[29],self.state[35],self.state[33],self.state[27]
        self.state[30],self.state[28],self.state[32],self.state[34] = self.state[28],self.state[32],self.state[34],self.state[30]
    def L(self):
        self.state[0],self.state[18],self.state[45],self.state[44] = self.state[44],self.state[0], self.state[18],self.state[45]
        self.state[3],self.state[21],self.state[48],self.state[41] = self.state[41],self.state[3],self.state[21],self.state[48]
        self.state[6],self.state[24],self.state[51],self.state[38] = self.state[38],self.state[6],self.state[24],self.state[51]
        self.state[9],self.state[11],self.state[17],self.state[15] = self.state[11],self.state[9],self.state[11],self.state[17]
        self.state[10],self.state[14],self.state[16],self.state[12] = self.state[12],self.state[10],self.state[14],self.state[16]
    def U(self):
        self.state[9],self.state[18],self.state[27],self.state[36] = self.state[18],self.state[27], self.state[36],self.state[9]
        self.state[10],self.state[19],self.state[28],self.state[37] = self.state[19],self.state[28],self.state[37],self.state[10]
        self.state[11],self.state[20],self.state[29],self.state[38] = self.state[20],self.state[29],self.state[38],self.state[11]
        self.state[0],self.state[2],self.state[8],self.state[6] = self.state[6],self.state[0],self.state[2],self.state[8]
        self.state[3],self.state[1],self.state[5],self.state[7] = self.state[7],self.state[3],self.state[1],self.state[3]
    def D(self):
        self.state[24],self.state[33],self.state[42],self.state[15] = self.state[15],self.state[24], self.state[33],self.state[42]
        self.state[25],self.state[34],self.state[43],self.state[16] = self.state[16],self.state[25],self.state[34],self.state[43]
        self.state[26],self.state[35],self.state[44],self.state[17] = self.state[17],self.state[26],self.state[35],self.state[44]
        self.state[45],self.state[47],self.state[53],self.state[51] = self.state[51],self.state[45],self.state[47],self.state[53]
        self.state[46],self.state[50],self.state[52],self.state[48] = self.state[48],self.state[46],self.state[50],self.state[52]
    def F(self):
        self.state[6],self.state[27],self.state[47],self.state[17] = self.state[17],self.state[6], self.state[27],self.state[47]
        self.state[7],self.state[30],self.state[46],self.state[14] = self.state[14],self.state[7],self.state[30],self.state[46]
        self.state[8],self.state[33],self.state[45],self.state[11] = self.state[11],self.state[8],self.state[33],self.state[45]
        self.state[18],self.state[20],self.state[26],self.state[24] = self.state[24],self.state[18],self.state[20],self.state[26]
        self.state[19],self.state[23],self.state[25],self.state[21] = self.state[21],self.state[19],self.state[23],self.state[21]
    def B(self):
        self.state[0],self.state[29],self.state[53],self.state[15] = self.state[29],self.state[53], self.state[15],self.state[0]
        self.state[1],self.state[32],self.state[52],self.state[12] = self.state[32],self.state[52],self.state[12],self.state[1]
        self.state[2],self.state[35],self.state[51],self.state[9] = self.state[35],self.state[51],self.state[9],self.state[2]
        self.state[37],self.state[41],self.state[43],self.state[39] = self.state[39],self.state[37],self.state[41],self.state[43]
        self.state[36],self.state[38],self.state[44],self.state[42] = self.state[42],self.state[36],self.state[38],self.state[44]
    
    #double moves
    def R2(self):
        self.R()
        self.R()
    def U2(self):
        self.U()
        self.U()
    def L2(self):
        self.L()
        self.L()
    def F2(self):
        self.F()
        self.F()
    def B2(self):
        self.B()
        self.B()
    def D2(self):
        self.D()
        self.D()
    
    #counterclockwise moves
    def Rprime(self):
        self.R()
        self.R()
        self.R()
    def Uprime(self):
        self.U()
        self.U()
        self.U()
    def Lprime(self):
        self.L()
        self.L()
        self.L()
    def Dprime(self):
        self.D()
        self.D()
        self.D()
    def Fprime(self):
        self.F()
        self.F()
        self.F()
    def Bprime(self):
        self.B()
        self.B()
        self.B()
    
    #slice moves
    def M(self):
        self.state[1],self.state[19],self.state[46],self.state[43] = self.state[43],self.state[1], self.state[19],self.state[46]
        self.state[4],self.state[22],self.state[49],self.state[40] = self.state[40],self.state[4],self.state[22],self.state[49]
        self.state[7],self.state[25],self.state[52],self.state[37] = self.state[37],self.state[7],self.state[25],self.state[52]
    def E(self):
        self.state[12],self.state[21],self.state[30],self.state[39] = self.state[39],self.state[12], self.state[21],self.state[30]
        self.state[13],self.state[22],self.state[31],self.state[40] = self.state[40],self.state[13],self.state[22],self.state[31]
        self.state[14],self.state[23],self.state[32],self.state[41] = self.state[41],self.state[14],self.state[23],self.state[32]
    def S(self):
        self.state[16],self.state[3],self.state[28],self.state[50] = self.state[50],self.state[16], self.state[3],self.state[28]
        self.state[13],self.state[4],self.state[31],self.state[49] = self.state[49],self.state[13],self.state[4],self.state[31]
        self.state[10],self.state[5],self.state[34],self.state[48] = self.state[48],self.state[10],self.state[5],self.state[34]
    def M2(self):
        self.M()
        self.M()
    def E2(self):
        self.E()
        self.E()
    def S2(self):
        self.S()
        self.S()
    def Mprime(self):
        self.M()
        self.M()
        self.M()
    def Eprime(self):
        self.E()
        self.E()
        self.E()
    def Sprime(self):
        self.S()
        self.S()
        self.S()
    
    #wide moves
    def r(self):
        self.R()
        self.Mprime()
    def l(self):
        self.L()
        self.M()
    def u(self):
        self.U()
        self.Eprime()
    def d(self):
        self.D()
        self.E()
    def f(self):
        self.F()
        self.S()
    def b(self):
        self.B()
        self.Sprime()
    def r2(self):
        self.r()
        self.r()
    def l2(self):
        self.l()
        self.l()
    def u2(self):
        self.u()
        self.u()
    def d2(self):
        self.d()
        self.d()
    def f2(self):
        self.f()
        self.f()
    def b2(self):
        self.b()
        self.b()
    def rprime(self):
        self.r()
        self.r()
        self.r()
    def lprime(self):
        self.l()
        self.l()
        self.l()
    def uprime(self):
        self.u()
        self.u()
        self.u()
    def dprime(self):
        self.d()
        self.d()
        self.d()
    def fprime(self):
        self.f()
        self.f()
        self.f()
    def bprime(self):
        self.b()
        self.b()
        self.b()

    #rotations
    def x(self):
        self.R()
        self.Mprime()
        self.Lprime()
    def y(self):
        self.U()
        self.Eprime()
        self.Dprime()
    def z(self):
        self.F()
        self.Bprime()
        self.S()
    def x2(self):
        self.x()
        self.x()
    def y2(self):
        self.y()
        self.y()
    def z2(self):
        self.z()
        self.z()
    def xprime(self):
        self.x()
        self.x()
        self.x()
    def yprime(self):
        self.y()
        self.y()
        self.y()
    def zprime(self):
        self.z()
        self.z()
        self.z()
    
    def doMoves(self, moves):
        movesList = fa(r"[RUFBDLMESxyzruflbd][w]?[2']?",moves)
        for move in movesList:
            if move == "R": self.R()
            elif move == "R2": self.R2()
            elif move == "R'": self.Rprime()
            elif move == "L": self.L()
            elif move == "L2": self.L2()
            elif move == "L'": self.Lprime()
            elif move == "U": self.U()
            elif move == "U2": self.U2()
            elif move == "U'": self.Uprime()
            elif move == "D": self.D()
            elif move == "D2": self.D2()
            elif move == "D'": self.Dprime()
            elif move == "F": self.F()
            elif move == "F2": self.F2()
            elif move == "F'": self.Fprime()
            elif move == "B": self.B()
            elif move == "B2": self.B2()
            elif move == "B'": self.Bprime()
            elif move == "M": self.M()
            elif move == "M2": self.M2()
            elif move == "M'": self.Mprime()
            elif move == "E": self.E()
            elif move == "E2": self.E2()
            elif move == "E'": self.Eprime()
            elif move == "S": self.S()
            elif move == "S2": self.S2()
            elif move == "S'": self.Sprime()
            elif move == "x": self.x()
            elif move == "x2": self.x2()
            elif move == "x'": self.xprime()
            elif move == "y": self.y()
            elif move == "y2": self.y2()
            elif move == "y'": self.yprime()
            elif move == "z": self.z()
            elif move == "z2": self.z2()
            elif move == "z'": self.zprime()
            elif move == "r" or move =='Rw': self.r()
            elif move == "r2" or move =='Rw2': self.r2()
            elif move == "r'" or move =="Rw'": self.rprime()
            elif move == "l" or move =="Lw": self.l()
            elif move == "l2" or move =='Lw2': self.l2()
            elif move == "l'" or move =="Lw'": self.lprime()
            elif move == "u" or move =="Uw": self.u()
            elif move == "u2" or move =="Uw2": self.u2()
            elif move == "u'" or move =="Uw'": self.uprime()
            elif move == "d" or move =="Dw": self.d()
            elif move == "d2" or move =="Dw2": self.d2()
            elif move == "d'" or move =="Dw'": self.dprime()
            elif move == "f" or move =="Fw": self.f()
            elif move == "f2" or move =="Fw2": self.f2()
            elif move == "f'" or move =="Fw'": self.fprime()
            elif move == "b" or move =='Bw': self.b()
            elif move == "b2" or move =='Bw2': self.b2()
            elif move == "b'" or move=="Bw'": self.bprime()
        self.positions()
    
    def positions(self):
        self.UB = self.state[1] + self.state[37]
        self.UL = self.state[3] + self.state[10]
        self.UR = self.state[5] + self.state[28]
        self.UF = self.state[7] + self.state[19]
        self.LU = self.state[10] + self.state[3]
        self.LB = self.state[12] + self.state[41]
        self.LF = self.state[14] + self.state[21]
        self.LD = self.state[16] + self.state[48]
        self.FD = self.state[25] + self.state[46]
        self.FU = self.state[19] + self.state[7]
        self.FL = self.state[21] + self.state[14]
        self.FR = self.state[23] + self.state[30]
        self.RU = self.state[28] + self.state[5]
        self.RF = self.state[30] + self.state[23]
        self.RD = self.state[34] + self.state[50]
        self.RB = self.state[32] + self.state[39]
        self.BU = self.state[37] + self.state[5]
        self.BL = self.state[41] + self.state[12]
        self.BD = self.state[43] + self.state[50]
        self.BR = self.state[39] + self.state[32]
        self.DF = self.state[46] + self.state[25]
        self.DR = self.state[50] + self.state[34]
        self.DL = self.state[48] + self.state[16]
        self.DB = self.state[50] + self.state[43]
        self.UBL = self.state[0] + self.state[38] + self.state[9]
        self.UBR = self.state[2] + self.state[36] + self.state[29]
        self.UFR = self.state[8] + self.state[20] + self.state[27]
        self.UFL = self.state[6] + self.state[18] + self.state[11]
        self.LUB = self.state[9] + self.state[0] + self.state[38]
        self.LUF = self.state[11] + self.state[6] + self.state[18]
        self.LDF = self.state[17] + self.state[45] + self.state[24]
        self.LDB = self.state[15] + self.state[51] + self.state[44]
        self.FUL = self.state[18] + self.state[6] + self.state[11]
        self.FUR = self.state[20] + self.state[8] + self.state[27]
        self.FDR = self.state[26] + self.state[47] + self.state[33]
        self.FDL = self.state[24] + self.state[45] + self.state[17]
        self.RUF = self.state[27] + self.state[8] + self.state[20]
        self.RUB = self.state[29] + self.state[2] + self.state[36]
        self.RDB = self.state[35] + self.state[53] + self.state[42]
        self.RDF = self.state[33] + self.state[47] + self.state[26]
        self.BUR = self.state[36] + self.state[2] + self.state[29]
        self.BUL = self.state[38] + self.state[0] + self.state[9]
        self.BDL = self.state[44] + self.state[53] + self.state[15]
        self.BDR = self.state[42] + self.state[53] + self.state[35]
        self.DBR = self.state[53] + self.state[42] + self.state[35]
        self.DFR = self.state[47] + self.state[26] + self.state[33]
        self.DFL = self.state[45] + self.state[24] + self.state[17]
        self.DBL = self.state[51] + self.state[44] + self.state[15]
    
def reverse(alg):
    a=""
    alg = alg.replace('Rw','r').replace('Lw','l').replace('Uw','u').replace('Bw','b').replace('Fw','f').replace('Dw','d')
    for x in fa(r"[RUFBDLMESxyzruflbd][2']?",alg)[::-1]:
        if "2" in x:
            a += x+' '
        elif "'" in x:
            a += x[0]+' '
        else:
            a += x+"' "
    return a.replace('r','Rw').replace('l','Lw').replace('u','Uw').replace('b','Bw').replace('f','Fw').replace('d','Dw')