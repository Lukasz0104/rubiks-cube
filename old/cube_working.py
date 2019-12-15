import sys
import tkinter as tk
import math

c = ['w','w','w','w','w','w','w','w','w','o','o','o','o','o','o','o','o','o','g','g','g','g','g','g','g','g','g','r','r','r','r','r','r','r','r','r','b','b','b','b','b','b','b','b','b','y','y','y','y','y','y','y','y','y']
cube = c
'''
	temp = c[]
	temp0 = c[]
	temp1 = c[]
	temp2 = c[]
	cube[] = temp
	cube[] = temp0
	cube[] = temp1
	cube[] = temp2
'''
def R(c):
	cube = c 
	temp = c[20]
	temp0 = c[2]
	temp1 = c[42]
	temp2 = c[47]
	cube[2] = temp
	cube[42] = temp0
	cube[47] = temp1
	cube[20] =temp2
	#
	temp = c[23]
	temp0 = c[5]
	temp1 = c[39]
	temp2 = c[50]
	cube[5] = temp
	cube[39] = temp0
	cube[50] = temp1
	cube[23] = temp2
	#
	temp = c[26]
	temp0 = c[8]
	temp1 = c[36]
	temp2 = c[53]
	cube[8] = temp
	cube[36] = temp0
	cube[53] = temp1
	cube[26] = temp2
	#
	temp = c[27]
	temp0 = c[29]
	temp1 = c[35]
	temp2 = c[33]
	cube[29] = temp
	cube[35] = temp0
	cube[33] = temp1
	cube[27] = temp2
	#
	temp = c[28]
	temp0 = c[32]
	temp1 = c[34]
	temp2 = c[30]
	cube[32] = temp
	cube[34] = temp0
	cube[30] = temp1
	cube[28] = temp2
	return cube
#
def R2(c):
	return R(R(c))
#
def Rp(c):
	return R(R(R(c)))
#
def L(c):
	cube = c
	
	temp = c[0]
	temp0 = c[18]
	temp1 = c[45]
	temp2 = c[44]
	cube[18] = temp
	cube[45] = temp0
	cube[44] = temp1
	cube[0] = temp2
	#
	temp = c[3]
	temp0 = c[21]
	temp1 = c[48]
	temp2 = c[41]
	cube[21] = temp
	cube[48] = temp0
	cube[41] = temp1
	cube[3] = temp2
	
	#
	temp = c[6]
	temp0 = c[24]
	temp1 = c[51]
	temp2 = c[38]
	cube[24] = temp
	cube[51] = temp0
	cube[38] = temp1
	cube[6] = temp2
	#
	temp = c[9]
	temp0 = c[11]
	temp1 = c[17]
	temp2 = c[15]
	cube[11] = temp
	cube[17] = temp0
	cube[15] = temp1
	cube[9] = temp2
	#
	temp = c[10]
	temp0 = c[14]
	temp1 = c[16]
	temp2 = c[12]
	cube[14] = temp
	cube[16] = temp0
	cube[12] = temp1
	cube[10] = temp2
	
	return cube
#
def L2(c):
	return L(L(c))
#
def Lp(c):
	return L(L(L(c)))
#
def U(c):
	cube = c
	temp = c[9]
	temp0 = c[36]
	temp1 = c[27]
	temp2 = c[18]
	cube[36] = temp
	cube[27] = temp0
	cube[18] = temp1
	cube[9] = temp2
	#
	temp = c[10]
	temp0 = c[37]
	temp1 = c[28]
	temp2 = c[19]
	cube[37] = temp
	cube[28] = temp0
	cube[19] = temp1
	cube[10] = temp2
	#
	temp = c[11]
	temp0 = c[38]
	temp1 = c[29]
	temp2 = c[20]
	cube[38] = temp
	cube[29] = temp0
	cube[20] = temp1
	cube[11] = temp2
	
	temp = c[0]
	temp0 = c[2]
	temp1 = c[8]
	temp2 = c[6]
	cube[2] = temp
	cube[8] = temp0
	cube[6] = temp1
	cube[0] = temp2
	
	temp = c[1]
	temp0 = c[5]
	temp1 = c[7]
	temp2 = c[3]
	cube[5] = temp
	cube[7] = temp0
	cube[3] = temp1
	cube[1] = temp2
	
	return cube
def U2(c):
	return U(U(c))
def Up(c):
	return U(U(U(c)))
def D(c):
	cube = c
	temp = c[24]
	temp0 = c[33]
	temp1 = c[42]
	temp2 = c[15]
	cube[33] = temp
	cube[42] = temp0
	cube[15] = temp1
	cube[24] = temp2
	
	temp = c[25]
	temp0 = c[34]
	temp1 = c[43]
	temp2 = c[16]
	cube[34] = temp
	cube[43] = temp0
	cube[16] = temp1
	cube[25] = temp2
	
	temp = c[26]
	temp0 = c[35]
	temp1 = c[44]
	temp2 = c[17]
	cube[35] = temp
	cube[44] = temp0
	cube[17] = temp1
	cube[26] = temp2
	
	temp = c[45]
	temp0 = c[47]
	temp1 = c[53]
	temp2 = c[51]
	cube[47] = temp
	cube[53] = temp0
	cube[51] = temp1
	cube[45] = temp2
	
	temp = c[48]
	temp0 = c[46]
	temp1 = c[50]
	temp2 = c[52]
	cube[46] = temp
	cube[50] = temp0
	cube[52] = temp1
	cube[48] = temp2
	return cube
def D2(c):
	return D(D(c))
def Dp(c):
	return D(D(D(c)))
def F(c):
	cube = c
	temp = c[6]
	temp0 = c[27]
	temp1 = c[47]
	temp2 = c[17]
	cube[27] = temp
	cube[47] = temp0
	cube[17] = temp1
	cube[6] = temp2
	
	temp = c[7]
	temp0 = c[30]
	temp1 = c[46]
	temp2 = c[14]
	cube[30] = temp
	cube[46] = temp0
	cube[14] = temp1
	cube[7] = temp2
	
	temp = c[8]
	temp0 = c[33]
	temp1 = c[45]
	temp2 = c[11]
	cube[33] = temp
	cube[45] = temp0
	cube[11] = temp1
	cube[8] = temp2
	
	temp = c[18]
	temp0 = c[20]
	temp1 = c[26]
	temp2 = c[24]
	cube[20] = temp
	cube[26] = temp0
	cube[24] = temp1
	cube[18] = temp2
	
	temp = c[19]
	temp0 = c[23]
	temp1 = c[25]
	temp2 = c[21]
	cube[23] = temp
	cube[25] = temp0
	cube[21] = temp1
	cube[19] = temp2
	return cube
def F2(c):
	return F(F(c))
def Fp(c):
	return F(F(F(c)))
def B(c):
	temp = c[0]
	temp0 = c[15]
	temp1 = c[53]
	temp2 = c[29]
	cube[15] = temp
	cube[53] = temp0
	cube[29] = temp1
	cube[0] = temp2
	
	temp = c[1]
	temp0 = c[12]
	temp1 = c[52]
	temp2 = c[32]
	cube[12] = temp
	cube[52] = temp0
	cube[32] = temp1
	cube[1] = temp2
	
	temp = c[2]
	temp0 = c[9]
	temp1 = c[51]
	temp2 = c[35]
	cube[9] = temp
	cube[51] = temp0
	cube[35] = temp1
	cube[2] = temp2
	
	temp = c[36]
	temp0 = c[38]
	temp1 = c[44]
	temp2 = c[42]
	cube[38] = temp
	cube[44] = temp0
	cube[42] = temp1
	cube[36] = temp2
	
	temp = c[37]
	temp0 = c[41]
	temp1 = c[43]
	temp2 = c[39]
	cube[41] = temp
	cube[43] = temp0
	cube[39] = temp1
	cube[37] = temp2
	return cube
def B2(c):
	return B(B(c))
def Bp(c):
	return B(B(B(c)))
def M(c):
	cube = c
	temp = c[1]
	temp0 = c[19]
	temp1 = c[46]
	temp2 = c[43]
	cube[19] = temp
	cube[46] = temp0
	cube[43] = temp1
	cube[1] = temp2
	
	temp = c[4]
	temp0 = c[22]
	temp1 = c[49]
	temp2 = c[40]
	cube[22] = temp
	cube[49] = temp0
	cube[40] = temp1
	cube[4] = temp2
	
	temp = c[7]
	temp0 = c[25]
	temp1 = c[52]
	temp2 = c[37]
	cube[25] = temp
	cube[52] = temp0
	cube[37] = temp1
	cube[7] = temp2
	return cube
def M2(c):
	return M(M(c))
def Mp(c):
	return M(M(M(c)))
def E(c):
	cube = c
	temp = c[21]
	temp0 = c[30]
	temp1 = c[39]
	temp2 = c[12]
	cube[30] = temp
	cube[39] = temp0
	cube[12] = temp1
	cube[21] = temp2
	
	temp = c[22]
	temp0 = c[31]
	temp1 = c[40]
	temp2 = c[13]
	cube[31] = temp
	cube[40] = temp0
	cube[13] = temp1
	cube[22] = temp2
	
	temp = c[23]
	temp0 = c[32]
	temp1 = c[41]
	temp2 = c[14]
	cube[32] = temp
	cube[41] = temp0
	cube[14] = temp1
	cube[23] = temp2
	return cube
def E2(c):
	return E(E(c))
def Ep(c):
	return E(E(E(c)))
def S(c):
	cube = c
	temp = c[3]
	temp0 = c[28]
	temp1 = c[50]
	temp2 = c[16]
	cube[28] = temp
	cube[50] = temp0
	cube[16] = temp1
	cube[3] = temp2
	
	temp = c[4]
	temp0 = c[31]
	temp1 = c[49]
	temp2 = c[13]
	cube[31] = temp
	cube[49] = temp0
	cube[13] = temp1
	cube[4] = temp2
	
	temp = c[5]
	temp0 = c[34]
	temp1 = c[48]
	temp2 = c[10]
	cube[34] = temp
	cube[48] = temp0
	cube[10] = temp1
	cube[5] = temp2
	return cube
def S2(c):
	return S(S(c))
def Sp(c):
	return S(S(S(c)))

def x(c):
	return(R(Lp(Mp(c))))
def x2(c):
	return x(x(c))
def xp(c):
	return x(x(x(c)))
	
def y(c):
	return U(Dp(Ep(c)))
def y2(c):
	return y(y(c))
def yp(c):
	return y(y(y(c)))

def z(c):
	return F(Bp(S(c)))
def z2(c):
	return z(z(c))
def zp(c):
	return z(z(z(c)))
def r(c):
    return R(Mp(c))
def r2(c):
    return r(r(c))
def rp(c):
    return r(r(r(c)))
def l(c):
    return L(M(c))
def l2(c):
    return l(l(c))
def lp(c):
    return l(l(l(c)))
def u(c):
    return U(Ep(c))
def u2(c):
    return u(u(c))
def up(c):
    return u(u(u(c)))
def d(c):
    return D(E(c))
def d2(c):
    return d(d(c))
def dp(c):
    return d(d(d(c)))
def f(c):
    return F(S(c))
def f2(c):
    return f(f(c))
def fp(c):
    return f(f(f(c)))
def b(c):
    return B(Sp(c))
def b2(c):
    return B2(S2(c))
def bp(c):
    return Bp(S(c))

def do_move(move, cube):
    if move == "R":
        return R(cube)
    elif move == " ":
            pass
    elif move == "R2":
        return R2(cube)
    elif move == "R'":
        return Rp(cube)
    elif move == "L":
        return L(cube)
    elif move == "L2":
        return L2(cube)
    elif move == "L'":
        return Lp(cube)
    elif move == "U":
        return U(cube)
    elif move == "U2":
        return U2(cube)
    elif move == "U'":
        return Up(cube)
    elif move == "D":
        return D(cube)
    elif move == "D2":
        return D2(cube)
    elif move == "D'":
        return Dp(cube)
    elif move == "F":
        return F(cube)
    elif move == "F2":
        return F2(cube)
    elif move == "F'":
        return Fp(cube)
    elif move == "B":
        return B(cube)
    elif move == "B2":
        return B2(cube)
    elif move == "B'":
        return Bp(cube)
    elif move == "M":
        return M(cube)
    elif move == "M2":
        return M2(cube)
    elif move == "M'":
        return Mp(cube)
    elif move == "E":
        return E(cube)
    elif move == "E2":
        return E2(cube)
    elif move == "E'":
        return Ep(cube)
    elif move == "S":
        return S(cube)
    elif move == "S2":
        return S2(cube)
    elif move == "S'":
        return Sp(cube)
    elif move == "x":
        return x(cube)
    elif move == "x2":
        return x2(cube)
    elif move == "x'":
        return xp(cube)
    elif move == "y":
        return y(cube)
    elif move == "y2":
        return y2(cube)
    elif move == "y'":
        return yp(cube)
    elif move == "z":
        return z(cube)
    elif move == "z2":
        return z2(cube)
    elif move == "z'":
        return zp(cube)
    elif move == "r":
        return r(cube)
    elif move == "r2":
        return r2(cube)
    elif move == "r'":
        return rp(cube)
    elif move == "l":
        return l(cube)
    elif move == "l2":
        return l2(cube)
    elif move == "l'":
        return lp(cube)
    elif move == "u":
        return u(cube)
    elif move == "u2":
        return u2(cube)
    elif move == "u'":
        return up(cube)
    elif move == "d":
        return d(cube)
    elif move == "d2":
        return d2(cube)
    elif move == "d'":
        return dp(cube)
    elif move == "f":
        return f(cube)
    elif move == "f2":
        return f2(cube)
    elif move == "f'":
        return fp(cube)
    elif move == "b":
        return b(cube)
    elif move == "b2":
        return b2(cube)
    elif move == "b'":
        return bp(cube)
    else:
        pass

cube = c

#create a window
root = tk.Tk()
root.title("Rubik's cube")
root.configure(background = 'black')

#include photos
g = tk.PhotoImage(file='g.png')
o = tk.PhotoImage(file='o.png')
blue = tk.PhotoImage(file='blue.png')
bl=tk.PhotoImage(file='fb.png')
w = tk.PhotoImage(file='w.png')
red = tk.PhotoImage(file='r.png')
yellow = tk.PhotoImage(file='y.png')

#assign photo to colour
def fu(s, x, y):
    if (s == 'g'):
         lab = tk.Label(root, bg = 'black', image = g)
         lab.grid(row = (x+3), column = y)
    elif s == 'o':
        lab = tk.Label(root, bg = 'black', image = o)
        lab.grid(row = (x+3), column = y)
    elif s == 'b':
        lab = tk.Label(root, bg = 'black', image = blue)
        lab.grid(row = (x+3), column = y)
    elif s =='w':
        lab = tk.Label(root, bg = 'black', image = w)
        lab.grid(row = (x+3), column = y)
    elif s =='r':
        lab = tk.Label(root, bg = 'black', image = red)
        lab.grid(row = (x+3), column = y)
    elif s == 'y':
            lab = tk.Label(root, bg = 'black', image = yellow)
            lab.grid(row = (x+3), column = y)
    elif s == 'bl':
        lab = tk.Label(root, bg = 'black', image = bl)
        lab.grid(row = (x+3), column = y)

t = tk.Text(root, height=1, width=15, bg='black', fg='white', bd=0, font =('Comic Sans MS', 20))
t.insert(tk.INSERT, "Podaj algorytm:")
t.grid(columnspan = 9, column = 0, row = 0)

#make an entry box
e = tk.Entry(root, bg = 'white', exportselection = 0, fg = 'black', width = 74)
e.grid(columnspan = 9, row = 1, column = 0)

#reset
def reset():
        cube = ['w','w','w','w','w','w','w','w','w','o','o','o','o','o','o','o','o','o','g','g','g','g','g','g','g','g','g','r','r','r','r','r','r','r','r','r','b','b','b','b','b','b','b','b','b','y','y','y','y','y','y','y','y','y']
        fu('bl', 0, 0)
        fu('bl', 0, 1)
        fu('bl', 0, 2)
        fu(cube[0], 0, 3)
        fu(cube[1], 0, 4)
        fu(cube[2], 0, 5)
        fu('bl', 0, 6)
        fu('bl', 0, 7)
        fu('bl', 0, 8)
        fu('bl', 1, 0)
        fu('bl', 1, 1)
        fu('bl', 1, 2)
        fu(cube[3], 1, 3)
        fu(cube[4], 1, 4)
        fu(cube[5], 1, 5)
        fu('bl', 1, 6)
        fu('bl', 1, 7)
        fu('bl', 1, 8)
        fu('bl', 1, 9)
        fu('bl', 1, 10)
        fu('bl', 1, 11)
        fu('bl', 2, 0)
        fu('bl', 2, 1)
        fu('bl', 2, 2)
        fu(cube[6], 2, 3)
        fu(cube[7], 2, 4)
        fu(cube[8], 2, 5)
        fu('bl', 2, 6)
        fu('bl', 2, 7)
        fu('bl', 2, 8)
        fu('bl', 2, 9)
        fu('bl', 2, 10)
        fu('bl', 2, 11)     
        fu(cube[9], 3, 0)
        fu(cube[10], 3, 1)
        fu(cube[11], 3, 2)
        fu(cube[18], 3, 3)
        fu(cube[19], 3, 4)
        fu(cube[20], 3, 5)
        fu(cube[27], 3, 6)
        fu(cube[28], 3, 7)
        fu(cube[29], 3, 8)
        fu(cube[36], 3, 9)
        fu(cube[37], 3, 10)
        fu(cube[38], 3, 11)
        fu(cube[12], 4, 0)
        fu(cube[13], 4, 1)
        fu(cube[14], 4, 2)
        fu(cube[21], 4, 3)
        fu(cube[22], 4, 4)
        fu(cube[23], 4, 5)
        fu(cube[30], 4, 6)
        fu(cube[31], 4, 7)
        fu(cube[32], 4, 8)
        fu(cube[39], 4, 9)
        fu(cube[40], 4, 10)
        fu(cube[41], 4, 11)
        fu(cube[15], 5, 0)
        fu(cube[16], 5, 1)
        fu(cube[17], 5, 2)
        fu(cube[24], 5, 3)
        fu(cube[25], 5, 4)
        fu(cube[26], 5, 5)
        fu(cube[33], 5, 6)
        fu(cube[34], 5, 7)
        fu(cube[35], 5, 8)
        fu(cube[42], 5, 9)
        fu(cube[43], 5, 10)
        fu(cube[44], 5, 11)
        fu('bl', 6, 0)
        fu('bl', 6, 1)
        fu('bl', 6, 2)
        fu(cube[45], 6, 3)
        fu(cube[46], 6, 4)
        fu(cube[47], 6, 5)
        fu('bl', 6, 6)
        fu('bl', 6, 7)
        fu('bl', 6, 8)
        fu('bl', 6, 9)
        fu('bl', 6, 10)
        fu('bl', 6, 11)
        fu('bl', 7, 0)
        fu('bl', 7, 1)
        fu('bl', 7, 2)
        fu(cube[48], 7, 3)
        fu(cube[49], 7, 4)
        fu(cube[50], 7, 5)
        fu('bl', 7, 6)
        fu('bl', 7, 7)
        fu('bl', 7, 8)
        fu('bl', 7, 9)
        fu('bl', 7, 10)
        fu('bl', 7, 11)
        fu('bl', 8, 0)
        fu('bl', 8, 1)
        fu('bl', 8, 2)
        fu(cube[51], 8, 3)
        fu(cube[52], 8, 4)
        fu(cube[53], 8, 5)
        fu('bl', 8, 6)
        fu('bl', 8, 7)
        fu('bl', 8, 8)
        fu('bl', 8, 9)
        fu('bl', 8, 10)
        fu('bl', 8, 11)
        s = ' '

#define a fuction printing possible moves
def func2():
        root1 = tk.Tk()
        root1.title("Dostępne ruchy")
        root1.configure(background = 'black')

        t1 = tk.Text(root1, height = 12,width = 20, bg ='black',fg = 'white', bd= 0,font =  ('Comic Sans MS', 20))
        t1.insert(tk.INSERT, "R L U D F B \nR' L' U' D' F' B' \nR2 L2 U2 D2 F2 B2 \nr l u d f b \nr' l' u' d' f' b' \nr2 l2 u2 d2 f2 b2 \nM E S \nM' E' S' \nM2 E2 S2 \nx y z \nx' y' z' \nx2 y2 z2")
        t1.pack()
 #add button1
button1 = tk.Button(root,bg='white',bd = 1,fg='black',text="Pokaż dostępne ruchy", command = func2)
button1.grid(columnspan = 3, column = 9, row = 0)
#add button2
button2 = tk.Button(root,bg='white',bd = 1,fg='black',text="RESET", command = reset)
button2.grid(columnspan = 3, column = 9, row = 3)

fu('bl', 0, 0)
fu('bl', 0, 1)
fu('bl', 0, 2)
fu(cube[0], 0, 3)
fu(cube[1], 0, 4)
fu(cube[2], 0, 5)
fu('bl', 0, 6)
fu('bl', 0, 7)
fu('bl', 0, 8)
#fu('bl', 0, 9)
#fu('bl', 0, 10)
#fu('bl', 0, 11)
        
fu('bl', 1, 0)
fu('bl', 1, 1)
fu('bl', 1, 2)
fu(cube[3], 1, 3)
fu(cube[4], 1, 4)
fu(cube[5], 1, 5)
fu('bl', 1, 6)
fu('bl', 1, 7)
fu('bl', 1, 8)
fu('bl', 1, 9)
fu('bl', 1, 10)
fu('bl', 1, 11)

fu('bl', 2, 0)
fu('bl', 2, 1)
fu('bl', 2, 2)
fu(cube[6], 2, 3)
fu(cube[7], 2, 4)
fu(cube[8], 2, 5)
fu('bl', 2, 6)
fu('bl', 2, 7)
fu('bl', 2, 8)
fu('bl', 2, 9)
fu('bl', 2, 10)
fu('bl', 2, 11)
     
fu(cube[9], 3, 0)
fu(cube[10], 3, 1)
fu(cube[11], 3, 2)
fu(cube[18], 3, 3)
fu(cube[19], 3, 4)
fu(cube[20], 3, 5)
fu(cube[27], 3, 6)
fu(cube[28], 3, 7)
fu(cube[29], 3, 8)
fu(cube[36], 3, 9)
fu(cube[37], 3, 10)
fu(cube[38], 3, 11)

fu(cube[12], 4, 0)
fu(cube[13], 4, 1)
fu(cube[14], 4, 2)
fu(cube[21], 4, 3)
fu(cube[22], 4, 4)
fu(cube[23], 4, 5)
fu(cube[30], 4, 6)
fu(cube[31], 4, 7)
fu(cube[32], 4, 8)
fu(cube[39], 4, 9)
fu(cube[40], 4, 10)
fu(cube[41], 4, 11)

fu(cube[15], 5, 0)
fu(cube[16], 5, 1)
fu(cube[17], 5, 2)
fu(cube[24], 5, 3)
fu(cube[25], 5, 4)
fu(cube[26], 5, 5)
fu(cube[33], 5, 6)
fu(cube[34], 5, 7)
fu(cube[35], 5, 8)
fu(cube[42], 5, 9)
fu(cube[43], 5, 10)
fu(cube[44], 5, 11)

fu('bl', 6, 0)
fu('bl', 6, 1)
fu('bl', 6, 2)
fu(cube[45], 6, 3)
fu(cube[46], 6, 4)
fu(cube[47], 6, 5)
fu('bl', 6, 6)
fu('bl', 6, 7)
fu('bl', 6, 8)
fu('bl', 6, 9)
fu('bl', 6, 10)
fu('bl', 6, 11)

fu('bl', 7, 0)
fu('bl', 7, 1)
fu('bl', 7, 2)
fu(cube[48], 7, 3)
fu(cube[49], 7, 4)
fu(cube[50], 7, 5)
fu('bl', 7, 6)
fu('bl', 7, 7)
fu('bl', 7, 8)
fu('bl', 7, 9)
fu('bl', 7, 10)
fu('bl', 7, 11)

fu('bl', 8, 0)
fu('bl', 8, 1)
fu('bl', 8, 2)
fu(cube[51], 8, 3)
fu(cube[52], 8, 4)
fu(cube[53], 8, 5)
fu('bl', 8, 6)
fu('bl', 8, 7)
fu('bl', 8, 8)
fu('bl', 8, 9)
fu('bl', 8, 10)
fu('bl', 8, 11)

def func1():
    s = e.get()
    tab1 = s.split(" ")
    global cube        
    le = len(tab1)

    for i in range(le):
        if not (tab1[i] in ["","R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "F", "F2", "F'", "D", "D2", "D'", "B","B2", "B'", 'r', 'r2', "r'", "l", "l2", "l'", 'u', "u2", "u'", "d", "d2", "d'", "f", "f2", "f'", "b", "b2", "b'", "M", "M2", "M'", "E", "E2", "E'", "S", "S2", "S'", 'x', 'x2', "x'", 'y', 'y2', "y'", 'z','z2', "z'"]):
            err = ("Wpisano niewłaściwy ruch!") #error message
            root2 = tk.Tk()
            root2.title("Błąd!")
            root2.configure(background= 'black')
            t2 = tk.Text(root2, height = 1, width = 20, bg ='black',fg = 'red', bd= 0,font =  ('Comic Sans MS', 22))
            t2.insert(tk.INSERT, err)
            t2.pack()
            s = ' '
            tab1 = s.split(' ')
            break
        
    x1 = le - 1
    e.delete(0, len(s) +1)
    if le > 1 and not (tab1[le - 1] in ["R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "F", "F2", "F'", "D", "D2", "D'", "B", "B2" "B'", 'r', 'r2', "r'", "l", "l2", "l'", 'u', "u2", "u'", "d", "d2", "d'", "f", "f2", "f'", "b", "b2", "b'", "M", "M2", "M'", "E", "E2", "E'", "S", "S2", "S'", 'x', 'x2', "x'", 'y', 'y2', "y'", 'z','z2', "z'"]):
        del tab1[x1]
    if ((le > 0) and (tab1[0] != '') and (tab1[0] != '')):
        for i in range(len(tab1)):
            cube = do_move(tab1[i], cube)
        
        fu('bl', 0, 0)
        fu('bl', 0, 1)
        fu('bl', 0, 2)
        fu(cube[0], 0, 3)
        fu(cube[1], 0, 4)
        fu(cube[2], 0, 5)
        fu('bl', 0, 6)
        fu('bl', 0, 7)
        fu('bl', 0, 8)
        #fu('bl', 0, 9)
        #fu('bl', 0, 10)
        #fu('bl', 0, 11)
        
        fu('bl', 1, 0)
        fu('bl', 1, 1)
        fu('bl', 1, 2)
        fu(cube[3], 1, 3)
        fu(cube[4], 1, 4)
        fu(cube[5], 1, 5)
        fu('bl', 1, 6)
        fu('bl', 1, 7)
        fu('bl', 1, 8)
        fu('bl', 1, 9)
        fu('bl', 1, 10)
        fu('bl', 1, 11)
        
        fu('bl', 2, 0)
        fu('bl', 2, 1)
        fu('bl', 2, 2)
        fu(cube[6], 2, 3)
        fu(cube[7], 2, 4)
        fu(cube[8], 2, 5)
        fu('bl', 2, 6)
        fu('bl', 2, 7)
        fu('bl', 2, 8)
        fu('bl', 2, 9)
        fu('bl', 2, 10)
        fu('bl', 2, 11)
        
        fu(cube[9], 3, 0)
        fu(cube[10], 3, 1)
        fu(cube[11], 3, 2)
        fu(cube[18], 3, 3)
        fu(cube[19], 3, 4)
        fu(cube[20], 3, 5)
        fu(cube[27], 3, 6)
        fu(cube[28], 3, 7)
        fu(cube[29], 3, 8)
        fu(cube[36], 3, 9)
        fu(cube[37], 3, 10)
        fu(cube[38], 3, 11)
        
        fu(cube[12], 4, 0)
        fu(cube[13], 4, 1)
        fu(cube[14], 4, 2)
        fu(cube[21], 4, 3)
        fu(cube[22], 4, 4)
        fu(cube[23], 4, 5)
        fu(cube[30], 4, 6)
        fu(cube[31], 4, 7)
        fu(cube[32], 4, 8)
        fu(cube[39], 4, 9)
        fu(cube[40], 4, 10)
        fu(cube[41], 4, 11)
        
        fu(cube[15], 5, 0)
        fu(cube[16], 5, 1)
        fu(cube[17], 5, 2)
        fu(cube[24], 5, 3)
        fu(cube[25], 5, 4)
        fu(cube[26], 5, 5)
        fu(cube[33], 5, 6)
        fu(cube[34], 5, 7)
        fu(cube[35], 5, 8)
        fu(cube[42], 5, 9)
        fu(cube[43], 5, 10)
        fu(cube[44], 5, 11)
        
        fu('bl', 6, 0)
        fu('bl', 6, 1)
        fu('bl', 6, 2)
        fu(cube[45], 6, 3)
        fu(cube[46], 6, 4)
        fu(cube[47], 6, 5)
        fu('bl', 6, 6)
        fu('bl', 6, 7)
        fu('bl', 6, 8)
        fu('bl', 6, 9)
        fu('bl', 6, 10)
        fu('bl', 6, 11)
        
        fu('bl', 7, 0)
        fu('bl', 7, 1)
        fu('bl', 7, 2)
        fu(cube[48], 7, 3)
        fu(cube[49], 7, 4)
        fu(cube[50], 7, 5)
        fu('bl', 7, 6)
        fu('bl', 7, 7)
        fu('bl', 7, 8)
        fu('bl', 7, 9)
        fu('bl', 7, 10)
        fu('bl', 7, 11)
        
        fu('bl', 8, 0)
        fu('bl', 8, 1)
        fu('bl', 8, 2)
        fu(cube[51], 8, 3)
        fu(cube[52], 8, 4)
        fu(cube[53], 8, 5)
        fu('bl', 8, 6)
        fu('bl', 8, 7)
        fu('bl', 8, 8)
        fu('bl', 8, 9)
        fu('bl', 8, 10)
        fu('bl', 8, 11)
        print(s)
        print(tab1)
        s = ' '
        tab1 = s.split(' ')
        
        print(s)
        print(tab1)
        
#make a button to do the moves     
b1 = tk.Button(root,bg='white',bd = 2,fg='red',text="Wykonaj!", command = func1, width="17")
b1.grid(column = 9, row = 1, columnspan = 3)


root.mainloop()
