//
//  main.c
//  xyz2cmy_neugebauer
//
//  Created by Brian Tang on 2021/5/25.
//

#include <stdio.h>
#include <math.h>

double Xc, Xm, Xy, Xcm, Xmy, Xcy, Xcmy, Xpaper;
double Yc, Ym, Yy, Ycm, Ymy, Ycy, Ycmy, Ypaper;
double Zc, Zm, Zy, Zcm, Zmy, Zcy, Zcmy, Zpaper;

struct Lab_Mode{
    double L,a,b;
};

struct Lab_Mode XYZ2Lab(double X, double Y, double Z) {
    struct Lab_Mode result;
    result.L = 116.0 * pow((Y / 100.0),(1 / 3.0))-16.0;
    result.a = 500 * (pow((X / 95.04), (1/3.0)) - pow((Y/100), (1/3.0)));
    result.b = 500 * (pow((Y / 95.04), (1/3.0)) - pow((Z/100), (1/3.0)));
    return result;
}

double X(double c,double m,double y){
    double X = c * (1 - m) * (1 - y) * Xc + m * (1 - c) * (1 - y) * Xm + y * (1 - m) * (1 - c) * Xy + c * m * y * Xcmy + c * y * (1 - m) * Xcy + c * m * (1 - y) * Xcm + m * y * (1 - c) * Xmy + (1 - c) * (1 - m) * (1 - y) * Xpaper;
    return X;
}

double Y(double c,double m,double y){
    double Y = c * (1 - m) * (1 - y) * Yc + m * (1 - c) * (1 - y) * Ym + y * (1 - m) * (1 - c) * Yy + c * m * y * Ycmy + c * y * (1 - m) * Ycy + c * m * (1 - y) * Ycm + m * y * (1 - c) * Ymy + (1 - c) * (1 - m) * (1 - y) * Ypaper;
    return Y;
}

double Z(double c,double m,double y){
    double Z = c * (1 - m) * (1 - y) * Zc + m * (1 - c) * (1 - y) * Zm + y * (1 - m) * (1 - c) * Zy + c * m * y * Zcmy + c * y * (1 - m) * Zcy + c * m * (1 - y) * Zcm + m * y * (1 - c) * Zmy + (1 - c) * (1 - m) * (1 - y) * Zpaper;
    return Z;
}

double delta(struct Lab_Mode Lab1,struct Lab_Mode Lab2) {
    return pow(pow(Lab1.L-Lab2.L, 2)+pow(Lab1.a-Lab2.a, 2)+pow(Lab1.b-Lab2.b, 2), (1/2.0));
}

int main(int argc, const char * argv[]) {
    printf("XYZpaper:");
    scanf("%lf %lf %lf",&Xpaper,&Ypaper,&Zpaper);
    printf("XYZc:");
    scanf("%lf %lf %lf",&Xc,&Yc,&Zc);
    printf("XYZm:");
    scanf("%lf %lf %lf",&Xm,&Ym,&Zm);
    printf("XYZy:");
    scanf("%lf %lf %lf",&Xy,&Yy,&Zy);
    printf("XYZmy:");
    scanf("%lf %lf %lf",&Xmy,&Ymy,&Zmy);
    printf("XYZcy:");
    scanf("%lf %lf %lf",&Xcy,&Ycy,&Zcy);
    printf("XYZcm:");
    scanf("%lf %lf %lf",&Xcm,&Ycm,&Zcm);
    printf("XYZcmy:");
    scanf("%lf %lf %lf",&Xcmy,&Ycmy,&Zcmy);
    
    while (1) {
        double deltaE = 10000;
        double c_result = 0,m_result = 0,y_result = 0;
        double Xce,Yce,Zce;
        double c,m,y;
        
        printf("XYZ:");
        scanf("%lf %lf %lf",&Xce,&Yce,&Zce);
        struct Lab_Mode Labce = XYZ2Lab(Xce, Yce, Zce);
        for (c=0;c<101;c++){
            for (m=0; m<101; m++) {
                for (y=0; y<101; y++) {
                    double Xji = X(c/100.0, m/100.0, y/100.0);
                    double Yji = Y(c/100.0, m/100.0, y/100.0);
                    double Zji = Z(c/100.0, m/100.0, y/100.0);
                    struct Lab_Mode Labji = XYZ2Lab(Xji, Yji, Zji);
                    double deltaE_temp = delta(Labji, Labce);
                    if (deltaE_temp < deltaE) {
                        deltaE = deltaE_temp;
                        c_result = c;
                        m_result = m;
                        y_result = y;
                    }
                }
            }
        }
        printf("c=%.0f m=%.0f y=%.0f\n",c_result,m_result,y_result);
    }
    return 0;
}
