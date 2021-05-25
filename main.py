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


def delta(Lab1, Lab2):
    return ((Lab1[0] - Lab2[0]) ** 2 + (Lab1[1] - Lab2[1]) ** 2 + (Lab1[2] - Lab2[2]) ** 2) ** (1 / 2)


# 声明变量
Xpaper, Ypaper, Zpaper = map(float, input('输入纸张XYZ并以空格隔开:').split())
Xc, Yc, Zc = map(float, input('输入C色元XYZ并以空格隔开:').split())
Xm, Ym, Zm = map(float, input('输入M色元XYZ并以空格隔开:').split())
Xy, Yy, Zy = map(float, input('输入Y色元XYZ并以空格隔开:').split())
Xmy, Ymy, Zmy = map(float, input('输入MY色元XYZ并以空格隔开:').split())
Xcy, Ycy, Zcy = map(float, input('输入CY色元XYZ并以空格隔开:').split())
Xcm, Ycm, Zcm = map(float, input('输入CM色元XYZ并以空格隔开:').split())
Xcmy, Ycmy, Zcmy = map(float, input('输入CMY色元XYZ并以空格隔开:').split())

while (True):
    deltaE = 10000
    c_result = 0.0
    m_result = 0.0
    y_result = 0.0

    Xce, Yce, Zce = map(float, input('输入XYZ并以空格隔开:').split())
    print("计算中")
    Labce = XYZ2Lab(Xce, Yce, Zce)

    for c in range(0, 101, 1):
        for m in range(0, 101, 1):
            for y in range(0, 101, 1):
                Xji = X(c / 100, m / 100, y / 100)
                Yji = Y(c / 100, m / 100, y / 100)
                Zji = Z(c / 100, m / 100, y / 100)
                Labji = XYZ2Lab(Xji, Yji, Zji)
                deltaE_temp = delta(Labji, Labce)
                if (deltaE_temp < deltaE):
                    deltaE = deltaE_temp
                    c_result = c
                    m_result = m
                    y_result = y
    print("c=" + str(c_result) + " m=" + str(m_result) + " y=" + str(y_result))
