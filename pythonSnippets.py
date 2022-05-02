# var 21

def t1(x):
    #x = 0.63 # 0.7
    a = 14 * x * x - \
        3 * (x ** 7)
    b = ((x ** 3 + 11 * x) ** 2) / 99
    c = math.cos(x * x - 36 * x * x * x - 0.01) ** 4
    d = a / (b - c)
    e = x ** 5 + math.log(x, 10) ** 7
    f = math.sqrt(d) - math.sqrt(e)
    return format(f, '.2E')


print(t1(0.63))

#######################################################################################

def t2(y):
    # y = 279, 242
    if 128 <= y < 149:
        return ((y * y / 68) ** 6) / 85
    elif 149 <= y < 205:
        return 32 * math.log(74 * (y ** 3), 10) + 37 * (y ** 5)
    elif y < 128:
        return 66 * (y ** 3) - math.ceil(y * y - 1) ** 4 - (y * y - (y ** 3))
    elif y >= 205:
        return y ** 3 - ((y ** 3) / 92) ** 4
    else:
        raise Exception()


print(format(t2(279), '.2E'))

#######################################################################################

# TODO: recover this task
def t3(m, p, b, a):
    # <unknown>
    aa = 0
    for i in range(1, m + 1):
        aa += 72 + 22 * (((p ** 3) / 41 + 56 * i * i + 88) ** 2)

    bb = 1
    for c in range(1, m + 1):
        bb2 = 0
        for i in range(1, a + 1):
            bb1 = 0
            for j in range(1, b + 1):
                bb1 += 85 * (((j ** 2) - 1) ** 5) - \
                       32 * (c ** 7) - math.sin(41 * (i ** 3) + 7 * i) ** 2
            bb2 += bb1
        bb *= bb2

    return aa - bb


print(format(t3(8, 0.54, 5, 3), '.2E'))
print(format(t3(7, -0.93, 5, 6), '.2E'))

#######################################################################################

def t4(n):
    # n = 9, 3
    if n == 0:
        return 0.73
    elif n == 1:
        return 0.56
    elif n >= 2:
        return 0.02 + (math.tan(t4(n - 1)) ** 3) / 72 + t4(n - 2) ** 2


print(format(t4(9), '.2E'))

#######################################################################################

def t5(a):
    # a = [-0.01, 0.41, 0.5, 0.27], [0.33, -0.49, -0.51, -0.32]
    n = len(a)
    b = 0
    for i in range(1, n + 1):
        b += (a[n + 1 - 1 - math.ceil(i / 4)] ** 4) / 53
    return b


print(format(t5([-0.01, 0.41, 0.5, 0.27]), '.2E'))

#######################################################################################

def t6(ar, lv=0):
    match lv:
        case 0:
            return {
                'JSX': lambda: t6(ar, 33),
                'QMAKE': lambda: t6(ar, 1),
                'NIM': lambda: 11
            }[ar[0]]()
        case 1:
            return {
                1989: lambda: t6(ar, 2),
                1979: lambda: t6(ar, 3),
                1957: lambda: t6(ar, 333)
            }[ar[1]]()
        case 2:
            return {
                1968: 5,
                2017: 6
            }[ar[2]]
        case 3:
            return {
                'PERL6': 7,
                'INI': 8
            }[ar[3]]
        case 333:
            return {
                'PERL6': 9,
                'INI': 10
            }[ar[3]]
        case 111:
            return {
                1989: 2,
                1979: 3,
                1957: 4
            }[ar[1]]
        case 33:
            return {
                'PERL6': lambda: t6(ar, 22),
                'INI': lambda: t6(ar, 111)
            }[ar[3]]()
        case 22:
            return {
                1968: 0,
                2017: 1
            }[ar[2]]
        case _:
            raise Exception


print(t6(['QMAKE', 1989, 1968, 'PERL6']))
print(t6(['NIM', 1957, 2017, 'INI']))

#######################################################################################

def t7(nn):
    aa = {1: 0b00000000000000000000000000011111, 2: 5,  4: 0}
    bb = {1: 0b00000000000000000000001111100000, 2: 5,  4: 5}
    cc = {1: 0b00000000001111111111110000000000, 2: 12, 4: 10}
    dd = {1: 0b00000001110000000000000000000000, 2: 3,  4: 22}
    ee = {1: 0b00011110000000000000000000000000, 2: 4,  4: 25}
    ff = {1: 0b01100000000000000000000000000000, 2: 2,  4: 29}
    gg = {1: 0b10000000000000000000000000000000, 2: 1,  4: 31}

    a = (nn & aa[1]) >> aa[4]
    b = (nn & bb[1]) >> bb[4]
    c = (nn & cc[1]) >> cc[4]
    d = (nn & dd[1]) >> dd[4]
    e = (nn & ee[1]) >> ee[4]
    f = (nn & ff[1]) >> ff[4]
    g = (nn & gg[1]) >> gg[4]

    # b f c g a d e

    r = b
    r = (r << ff[2]) | f
    r = (r << cc[2]) | c
    r = (r << gg[2]) | g
    r = (r << aa[2]) | a
    r = (r << dd[2]) | d
    r = (r << ee[2]) | e

    return r


print(hex(t7(0x92590dc5)))
print(hex(t7(0xf03f08d0)))

#######################################################################################

def t8(s):
    def lm(_a): return re.split(
        '\\s+' if re.search('\\s', _a)
        else '::=', _a)[1]

    st = re.findall('store\\s+\\w+', s)
    st = list(map(lm, st))

    ts = re.findall('::=\\s*\\w+', s)
    ts = list(map(lm, ts))

    dc = {}
    for j, i in enumerate(st):
        dc[i] = ts[j]

    return dc


print(t8('begin || store arin_670::= tiusat ||, || store rebeor::= xetequ_696\n||,end'))
print(t8('begin ||store isanes ::= laes ||, ||store isve_884 ::=bizace_52 ||,end'))

#######################################################################################

class Ml:
    st = ''
    aa = 'a'
    bb = 'b'
    cc = 'c'
    dd = 'd'
    ee = 'e'
    ff = 'f'

    def __init__(self):
        self.st = self.aa

    def view(self):
        match self.st:
            case self.aa:
                self.st = self.bb
                return 0
            case self.bb:
                self.st = self.cc
                return 1
            case self.cc:
                self.st = self.dd
                return 3
            case self.ee:
                self.st = self.ff
                return 6
            case _:
                raise KeyError

    def coat(self):
        match self.st:
            case self.bb:
                self.st = self.ff
                return 2
            case self.cc:
                self.st = self.ee
                return 4
            case self.dd:
                self.st = self.ee
                return 5
            case self.ee:
                self.st = self.aa
                return 7
            case self.ff:
                return 8
            case _:
                raise KeyError


def t9():
    return Ml()


o = t9()
print(a := o.view(), a == 0)
print(a := o.view(), a == 1)
print(a := o.coat(), a == 4)
print(a := o.coat(), a == 7)
print(a := o.view(), a == 0)
print(a := o.view(), a == 1)
print(a := o.view(), a == 3)
try: print(o.view(), 'KeyError')
except: KeyError
print(a := o.coat(), a == 5)
print(a := o.coat(), a == 7)
print(a := o.view(), a == 0)
print(a := o.coat(), a == 2)
print(a := o.coat(), a == 8)

#######################################################################################

import re


def t10(ar):
    pr = []
    ph = []
    nm = []
    rs = []

    def _pr(i):
        el = ar[i][0]
        p = el.split('%#')[0]
        s = str(int(p) / 100)
        pr.append(s + '0' if len(s) < 4 else s)

    def _ph(i):
        el = ar[i][2].split(' ')[1]
        c = el.split('-')
        _l = c[0]
        r = c[1]
        ph.append(f'{_l}-{r[0:2]}-{r[2:4]}')

    def _nm(i):
        el = ar[i][0]
        n = el.split('%#')[1]
        a = n.split(' ')[0]
        b = re.search(' .\\.', n)[0][1:3]
        nm.append(f'{a} {b}')

    for j, _ in enumerate(ar):
        _pr(j)
        _ph(j)
        _nm(j)

        rs.append([pr[j], ph[j], nm[j]])

    return rs


print(t10([['23%#SURNAME A.B.', None, '048 493-8445'],
      ['74%#SURNAME A.B.', None, '889 542-4954'],
      ['42%#SURNAME A.B.', None, '825 287-9258'],
      ['94%#SURNAME A.B.', None, '537 035-5048']]))

print(t10([
    ['24%#SURNAME A.B.', None, '391 440-7854'],
    ['17%#SURNAME A.B.', None, '870 406-3447'],
    ['59%#SURNAME A.B.', None, '771 521-8463']
]))

#######################################################################################

import struct as s


def t11(a):
    off = 4
    b = bytes(a[off:])

    al = 22
    aa = s.unpack('>IHQq', b[:al])
    a1 = (aa[0], aa[1])
    a2 = aa[2]
    a3 = aa[3]

    cl = al + 6
    cc = s.unpack('>HHh', b[al:cl])
    c1 = cc[0]
    c2 = cc[1]
    c3 = cc[2]

    al2 = cl + 20
    aa2 = s.unpack('>IIqI', b[cl:al2])
    aa5 = (aa2[0], aa2[1])
    a6 = aa2[2]
    a7 = aa2[3]

    a5l = aa5[0]
    a5d = aa5[1] - off
    a5 = s.unpack(f'>{a5l}s', b[a5d:(a5d + a5l)])[0]

    bar = []
    bal = s.calcsize('>H')
    bsz = a1[0]
    bad = a1[1] - off
    ba = s.unpack(f'>{bsz}H', b[bad:(bad + bsz * bal)])
    bln = s.calcsize('>IHHd')
    for i in ba:
        j = i - off
        bb = s.unpack('>IHHd', b[j:(j + bln)])

        arl = bb[1]
        ard = bb[2] - off
        ss = s.unpack(f'>{arl}s', b[ard:(ard + arl)])[0]

        bar.append((bb, ss))

    da = a7 - off
    dl = s.calcsize('HIB')
    dd = s.unpack('>HIB', b[da:(da + dl)])
    d2 = dd[2]

    drs = dd[0]
    drd = dd[1] - off
    drl = s.calcsize('b')
    dar = s.unpack(f'>{drs}b', b[drd:(drd + drs * drl)])

    c = {
        'A1': [],
        'A2': a2,
        'A3': a3,
        'A4': {'C1': c1, 'C2': c2, 'C3': c3},
        'A5': str(a5)[2:-1],
        'A6': a6,
        'A7': {'D1': [], 'D2': d2}
    }

    for i in bar:
        c.get('A1').append({
            'B1': i[0][0],
            'B2': str(i[1])[2:-1],
            'B3': i[0][3]})

    for i in dar:
        c.get('A7').get('D1').append(i)

    return c


print(t11((b'GBA\xa7\x00\x00\x00\x04\x00\x81\x0b\xde\x86\xc0;}\xc9\xf2\x980$3\x92G'
 b'\x01\xd8\x9a\x8e\t\xa1\xedj\x00\x00\x00\x07\x00\x00\x00\x89\xb1j(\x81\xb2u[('
 b'\x00\x00\x00\x92eblp\x99\x9bI~\x00\x04\x004\xbf\xec\xc8J\xfa\x81l\x88olwP'
 b'$\xc2\x16\x00\x03\x00H?\xd83\xb5g\xfb\xe3\xe0go\x8aK\xe1\xfa\x00\x02\x00'
 b'[\xbf\xed\x8fK\x8c\xa2\xe2`kubk\xfc+H\xb4\x00\x04\x00m?\xccr\x89\xc8\xf6\x17'
 b'x\x008\x00K\x00]\x00qnvjhwdf\xf2\x95\x00\x02\x00\x00\x00\x90\x90')))

