import itertools

# Multiplication in F2
def computeLinear(x,a,b,c,d):
    x = "{0:b}".format(x).zfill(4)
    s0 = (int(a[0])*int(x[0]) + int(b[0])*int(x[1]) + int(c[0])*int(x[2]) + int(d[0])*int(x[3]))%2
    s1 = (int(a[1])*int(x[0]) + int(b[1])*int(x[1]) + int(c[1])*int(x[2]) + int(d[1])*int(x[3]))%2
    s2 = (int(a[2])*int(x[0]) + int(b[2])*int(x[1]) + int(c[2])*int(x[2]) + int(d[2])*int(x[3]))%2
    s3 = (int(a[3])*int(x[0]) + int(b[3])*int(x[1]) + int(c[3])*int(x[2]) + int(d[3])*int(x[3]))%2
    return int(str(s0) + str(s1) + str(s2) + str(s3),base=2)

# Is the function l a permutation ?
def isPermutation(l):
    for i in range(16):
        for j in range(i+1,16):
            if(l[i] == l[j]):
                return False
    return True

# Return the lexicographic order of the list L
def lexicographicOrder(L):
    lex = [(sum([L[i][j]*16**(15-j) for j in range(len(L[i]))]),i) for i in range(len(L))]
    lex.sort(key=lambda x:x[0])
    return [L[lex[i][1]] for i in range(len(L))]

# Wire crossings
def switch(s,x):
    x = "{0:b}".format(x).zfill(4)
    out = [0 for i in range(5)]
    i = 0
    for sw in s:
        if(sw != 4):
            out[3-i] = x[sw]
        else:
            out[3-i] = str(sum([int(x[j]) for j in range(len(x))])%2)
        i += 1
    r = ""
    for sw in range(4):
        r += out[3-sw]
    return(int(r,2))

# ID of a function in the lexicogrphic order
def ID(l):
    return sum([l[j]*16**(15-j) for j in range(len(l))])

# Return the list of 4-bit affine permutations
def getAffineList():
    affineList = []                                                             # 4-bit affine functions
    for a in range(16):                                    
        a = "{0:b}".format(a).zfill(4)
        for b in range(16):
            b = "{0:b}".format(b).zfill(4)
            for c in range(16):
                c = "{0:b}".format(c).zfill(4)
                for d in range(16):
                    d = "{0:b}".format(d).zfill(4)
                    tmp = []
                    for x in range(16):
                        tmp.append(computeLinear(x, a, b, c, d))
                    for k in range(16):
                        affineList.append([tmp[i]^k for i in range(len(tmp))])
    permutations = []                                                           # 4-bit affine permutations
    for l in affineList:
        if(isPermutation(l)):
            permutations.append(l)
    return lexicographicOrder(permutations)                                     # Lexicographically ordered 4-bit affine permutations


# Return the list of wire equivalence classes representatives using 4-bit wire crossings
def getWireListWith4bitCrossings():
    affine = getAffineList()
    wire = []
    for a in affine:
        w = False
        for l in itertools.permutations([i for i in range(4)]):
            for l_ in itertools.permutations([i for i in range(4)]):
                a_ = [switch(l, a[switch(l_,i)]) for i in range(len(a))]
                if(ID(a_) < ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    return wire

# Return the list of wire equivalence classes representatives using 4-bit wire crossings
def getWireListWith5bitCrossings():
    affine = getAffineList()
    wire = []
    for a in affine:
        w = False
        for l in itertools.permutations([i for i in range(5)]):
            for l_ in itertools.permutations([i for i in range(5)]):
                a_ = [switch(l, a[switch(l_,i)]) for i in range(len(a))]
                if(ID(a_) < ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    return wire
