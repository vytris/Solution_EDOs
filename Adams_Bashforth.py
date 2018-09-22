from math import *

RK=[]
F=[]

def RungeKutta(expre,t0,y0,h,n):
        #print("T="+str(t0))
        #print("Y="+str(y0))
        #print()
        yA=y0
        t=t0
        y=y0
        print("T="+str(t))
        print("Y(T)="+str(y))
        print("")
        RK.append([y,t])
        for i in range(0,n):
                K1=eval(expre)
                t=t+h/2
                y=yA+(h/2)*K1
                K2=eval(expre)
                y=yA+(h/2)*K2
                K3=eval(expre)
                y=yA+h*K3
                t=t+h/2
                K4=eval(expre)
                yP=yA+(K1+2*K2+2*K3+K4)*(h/6)
                yA=yP
                y=yA
                print("T="+str(t))
                print("Y(T)="+str(y))
                print("")
                RK.append([y,t])
        return

def AB_G(grau,i,h):
        if(grau==2):
                FN=F[i+1-grau][0]
                FN_1=F[i-grau][0]
                return (h/2)*(3*FN-FN_1)
        elif(grau==3):
                FN=F[i+2-grau][0]
                FN_1=F[i+1-grau][0]
                FN_2=F[i-grau][0]
                return ((h/12)*(23*FN-16*FN_1+5*FN_2)) 
        elif(grau==4):
                FN=F[i+3-grau][0]
                FN_1=F[i+2-grau][0]
                FN_2=F[i+1-grau][0]
                FN_3=F[i-grau][0]
                return ((h/24)*(55*FN-59*FN_1+37*FN_2-9*FN_3)) 
        elif(grau==5):
                FN=F[i+4-grau][0]
                FN_1=F[i+3-grau][0]
                FN_2=F[i+2-grau][0]
                FN_3=F[i+1-grau][0]
                FN_4=F[i-grau][0]
                return ((h/720)*(1901*FN-2774*FN_1+2616*FN_2-1274*FN_3+251*FN_4)) 
        elif(grau==6):
                FN=F[i+5-grau][0]
                FN_1=F[i+4-grau][0]
                FN_2=F[i+3-grau][0]
                FN_3=F[i+2-grau][0]
                FN_4=F[i+1-grau][0]
                FN_5=F[i-grau][0]
                return (h/1440)*(4277*FN-7923*FN_1+9982*FN_2-7298*FN_3+2877*FN_4-475*FN_5)

def TY(grau,expre):
        for i in range(0,grau):
                y=RK[i][0]
                t=RK[i][1]
                F.append([eval(expre),t])
        return

def Adams__Bashforth(expre,t0,tf,y0,h,n,grau):
        RungeKutta(expre,t0,y0,h,grau-1)
        TY(grau,expre)
        yA=RK[grau-1][0]
        tA=t0+h*grau
        for i in range(grau,n+1):
                yP=yA+AB_G(grau,i,h)
                yA=yP
                y=yP
                t=tA
                print("T="+str(t))
                print("Y(T)="+str(y))
                print("")
                if(t==tf):
                        return
                F.append([eval(expre),t])
                tA=tA+h

        
myfile=open("funcoes.txt","r")
print("Bem-Vindo ao Metodo Numerico de Adams-Bashforth")
print("Voce deseja que todas as funcoes contidas no arquivo usem o mesmo ponto inicial(t0), valor do ponto inicial(y(t0)), passo(h) para calcular o valor da funcao no ponto final(tf)?")
opcao=int(input("Digite 1 para sim e 2 para nao:"))
if(opcao==1):
        t0=float(input("Insira o valor de t0:"))
        y0=float(input("Insira o valor de y0:"))
        h=float(input("Insira o valor de h:"))
        tf=float(input("Insira o valor de t que voce deseja calcular a f(t):"))
        grau=int(input("Insira a grau da formula de Adams-Bashforth:"))
        n=int(round((tf-t0)/h))#deve ser >=grau
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                Adams__Bashforth(expre,t0,tf,y0,h,n,grau)
                F.clear()
                RK.clear()
else:
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                t0=float(input("Insira o valor de t0:"))
                y0=float(input("Insira o valor de y0:"))
                h=float(input("Insira o valor de h:"))
                tf=float(input("Insira o valor de t que voce deseja calcular a f(t):"))
                grau=int(input("Insira a grau da formula de Adams-Bashforth:"))
                n=int(round((tf-t0)/h))#deve ser >=grau
                Adams__Bashforth(expre,t0,tf,y0,h,n,grau)
                F.clear()
                RK.clear()

myfile.close()