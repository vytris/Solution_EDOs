from math import*

def euler(expre,t0,tf,y0,h,n):
        print("T="+str(t0))
        print("Y="+str(y0))
        print()
        y=y0
        t=t0
        for i in range(0,n):
                yP=y+(h*eval(expre))
                t=t+h
                y=yP
                print("T="+str(t))
                print("Y(T)="+str(y))
                print("")
        return

myfile=open("funcoes.txt","r")
print("Bem-Vindo ao Metodo Numerico de Euler")
print("Voce deseja que todas as funcoes contidas no arquivo usem o mesmo ponto inicial(t0), valor do ponto inicial(y(t0)), passo(h) para calcular o valor da funcao no ponto final(tf)?")
opcao=int(input("Digite 1 para sim e 2 para nao:"))
if(opcao==1):
        t0=float(input("Insira o valor de t0:"))
        y0=float(input("Insira o valor de y(t0):"))
        h=float(input("Insira o valor de h:"))
        tf=float(input("Insira o valor de t para o qual voce deseja calcular a y(t):"))
        n=int(round((tf-t0)/h))
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                euler(expre,t0,tf,y0,h,n)
else:
        for line in myfile:
                expre=line
                print("FUNCAO:",expre)
                t0=float(input("Insira o valor de t0:"))
                y0=float(input("Insira o valor de y(t0):"))
                h=float(input("Insira o valor de h:"))
                tf=float(input("Insira o valor de t que voce deseja calcular a y(t):"))
                n=int(round((tf-t0)/h))
                euler(expre,t0,tf,y0,h,n)

myfile.close()