# 数字图像复制技术实验1：色度式分色模型的验证


def X(c, m, y):
    global Xc, Xm, Xy, Xcm, Xmy, Xcy, Xcmy, Xpaper
    result = c * (1 - m) * (1 - y) * Xc + m * (1 - c) * (1 - y) * Xm + y * (1 - m) * (
            1 - c) * Xy + c * m * y * Xcmy + c * y * (1 - m) * Xcy + c * m * (1 - y) * Xcm + m * y * (1 - c) * Xmy + (
                     1 - c) * (1 - m) * (1 - y) * Xpaper
    return result


def Y(c, m, y):
    global Yc, Ym, Yy, Ycm, Ymy, Ycy, Ycmy, Ypaper
    result = c * (1 - m) * (1 - y) * Yc + m * (1 - c) * (1 - y) * Ym + y * (1 - m) * (
            1 - c) * Yy + c * m * y * Ycmy + c * y * (1 - m) * Ycy + c * m * (1 - y) * Ycm + m * y * (1 - c) * Ymy + (
                     1 - c) * (1 - m) * (1 - y) * Ypaper
    return result


def Z(c, m, y):
    global Zc, Zm, Zy, Zcm, Zmy, Zcy, Zcmy, Zpaper
    result = c * (1 - m) * (1 - y) * Zc + m * (1 - c) * (1 - y) * Zm + y * (1 - m) * (
            1 - c) * Zy + c * m * y * Zcmy + c * y * (1 - m) * Zcy + c * m * (1 - y) * Zcm + m * y * (1 - c) * Zmy + (
                     1 - c) * (1 - m) * (1 - y) * Zpaper
    return result


def XYZ2Lab(X, Y, Z):
    L = 116 * (Y / 100.0) ** (1 / 3) - 16
    a = 500 * ((X / 95.04) ** (1 / 3) - (Y / 100.0) ** (1 / 3))
    b = 500 * ((Y / 100.0) ** (1 / 3) - (Z / 108.88) ** (1 / 3))

    return [L, a, b]

def delta(Lab1,Lab2):
    return ((Lab1[0]-Lab2[0])**2+(Lab1[1]-Lab2[1])**2+(Lab1[2]-Lab2[2])**2)**(1/2)


# 声明变量
Xpaper = 83.57
Ypaper = 86.79
Zpaper = 71.43
Xc = 12.77
Yc = 19.79
Zc = 49.59
Xm = 36.02
Ym = 19.46
Zm = 19.11
Xy = 68.83
Yy = 74.69
Zy = 6.94
Xmy = 33.88
Ymy = 19.54
Zmy = 2.97
Xcy = 7.91
Ycy = 18.14
Zcy = 6.34
Xcm = 6.24
Ycm = 5.29
Zcm = 20.16
Xcmy = 1.09
Ycmy = 1.18
Zcmy = 1.07

Xce = 60.47
Yce = 64.38
Zce = 44.81

Labce = XYZ2Lab(Xce,Yce,Zce)
deltaE = 10000

c_result = 0.0
m_result = 0.0
y_result = 0.0


for c in range(0, 101, 1):
    for m in range(0, 101, 1):
        for y in range(0, 101, 1):
            Xji = X(c / 100, m / 100, y / 100)
            Yji = Y(c / 100, m / 100, y / 100)
            Zji = Z(c / 100, m / 100, y / 100)
            Labji = XYZ2Lab(Xji,Yji,Zji)
            deltaE_temp = delta(Labji,Labce)
            print(deltaE_temp)
            if(deltaE_temp < deltaE):
                deltaE = deltaE_temp
                c_result = c
                m_result = m
                y_result = y

print(c_result,m_result,y_result)