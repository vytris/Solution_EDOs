from math import*

def RungeKutta(expre,t0,tf,y0,h,n):
        print("T="+str(t0))
        print("Y="+str(y0))
        print()
        yA=y0
        t=t0
        y=y0
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

myfile=open("funcoes.txt","r")
print("Bem-Vindo ao Metodo Numerico de Runge Kutta de Quarta Ordem")
print("Voce deseja que todas as funcoes contidas no arquivo usem o mesmo ponto inicial(t0), valor do ponto inicial(y(t0)), passo(h) para calcular o valor da funcao no ponto final(tf)?")
opcao=int(input("Digite 1 para sim e 2 para nao:"))
if(opcao==1):
        t0=float(input("Insira o valor de t0:"))
        y0=float(input("Insira o valor de y0:"))
        h=float(input("Insira o valor de h:"))
        tf=float(input("Insira o valor de t que voce deseja calcular a f(t):"))
        n=int(round((tf-t0)/h))
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                RungeKutta(expre,t0,tf,y0,h,n)
else:
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                t0=float(input("Insira o valor de t0:"))
                y0=float(input("Insira o valor de y0:"))
                h=float(input("Insira o valor de h:"))
                tf=float(input("Insira o valor de t que voce deseja calcular a f(t):"))
                n=int(round((tf-t0)/h))
                RungeKutta(expre,t0,tf,y0,h,n)

myfile.close()