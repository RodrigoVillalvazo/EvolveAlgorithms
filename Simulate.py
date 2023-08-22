import csv
from Importer import *
def Evasion2Robots(ind,tf,td,FILED,Rob1,Rob2,rRob1,rRob2,Cd):
    #print(str(ind))
    #Numero de robots
    n=2
    rCen=0.1
    phi=3.1415/18
    dt=0.001
    #Vector direccion
    theta=np.arange(0,2*np.pi,2*np.pi/n)
    Vdir1=[np.cos(theta[0]),np.sin(theta[0])]
    Vdir2=[np.cos(theta[1]),np.sin(theta[1])]
    #....#
    #Posicion deseada
    cd=CirclevirtualModel(Cd,phi,dt)
    #cd=DaisyvirtualModel(Cd,dt)
    #cd=GeronovirtualModel(Cd,dt)
    PdR1=Plus(cd,Times(rCen,Vdir1))
    PdR2=Plus(cd,Times(rCen,Vdir2))     
    r=[rRob1,rRob2]#Radio de los robots y obstaculos
    pos=[Rob1,Rob2,PdR1,PdR2]#Vector de Condiciones iniciales
    pd=[pos[2],pos[3]]#Vector de posiciones deseadas
    TF=0
    zF=0
    OF=0
    EF=0
    tR1=0
    tR2=0
    aux1=1
    aux2=1
    zeroF=[]#Contador de banderas por division cero
    TypeF=[]#Contador de banderas por error de tipo
    OverF=[]#Contador de banderas por sobreflujo de datos
    ErrorF=[]#Contador de banderas por error de valor
    aux10=[]
    FLR1=[]
    FLR2=[]
    vxR1=[]#list
    vxR2=[]#list
    vyR1=[]#list
    vyR2=[]#list
    VxR1=[]#list
    VxR2=[]#list
    VyR1=[]#list
    VyR2=[]#list
    dsR1a=[]#list
    dsR2a=[]#list
    doR1a=[]#list
    doR2a=[]#list
    dR1a=[]#list
    dR2a=[]#list
    drR1a=[]#list
    drR2a=[]#list
    Try1=[]
    Try2=[]
    Try3=[] 
    Try4=[]
    cdxa=[]
    cdya=[]
    vrR1=[]
    drR1=[]
    drR2=[]
    drR3=[]
    tR1saved=0.0
    tR2saved=0.0
    tsR1=[]#list
    tsR2=[]#list
    vrR2=[]#list
    r1=r[0]
    r2=r[1]

    xo1=[0]
    yo1=[0]
    xo2=[0]
    yo2=[0]

    xRob1=[0.0]
    yRob1=[0.0]
    xRob2=[0.0]
    yRob2=[0.0]

    tR1=tR1+dt
    tR2=tR2+dt

    #Posicion del obstaculo
    posR1x=float(eval(str(pos[0][0]).replace('"', '').replace("'", '')))#float
    posR1y=float(eval(str(pos[0][1]).replace('"', '').replace("'", '')))#float
    posR2x=float(eval(str(pos[1][0]).replace('"', '').replace("'", '')))#float
    posR2y=float(eval(str(pos[1][1]).replace('"', '').replace("'", '')))#float

    pdR1=[float(pd[0][0]),float(pd[0][1])]
    pdR2=[float(pd[1][0]),float(pd[1][1])]
    #Inicializar el vector u
    u=[posR1x,posR1y,posR2x,posR2y,pdR1,pdR2,0,0,0,0,0,0,0,0,0,0,td]
    #u=[posR1x,pdR1,0,posR1y,pdR2,0,posR2x,posR2y,pdR3,pdR4,0,0,0,0,0,0,posR3x,posR3y,0,0,0,0,posR4x,posR4y]   
    u0R1=[u[0],u[1]]
    u0R2=[u[2],u[3]]

    VxR1=u[6]
    VyR1=u[7]
    VxR2=u[8]
    VyR2=u[9]
    tR1=u[10]
    tR2=u[11]

    #distancia inicial del robot al objetivo
    qR1=list([posR1x,posR1y])
    qR2=list([posR2x,posR2y])

    doR1=Norm(Minus(qR1,pdR1))
    dR1=doR1
    doR2=Norm(Minus(qR2,pdR2))
    dR2=doR2

    #distancia del robot al obstaculo
    dsR1=Norm(Minus(qR1,qR2))
    dsR2=Norm(Minus(qR2,qR1))

    drR1=0        #distancia recorrida
    drR2=0

    ep=0.0001;   #epsilon al objetivo
    i=1
    #Obtener velocidades
    radiO=(r1+r2)+ep
    FlagsR1,vR1=ModelKaF1TestRobot1(u,ind,r,u0R1)
    FlagsR2,vR2=ModelKaF1TestRobot2(u,ind,r,u0R2)

    #vR1=[vR1]
    #vR2=[vR2]

    qR1=[qR1]
    qR2=[qR2]
     
    while (tR1<=tf)and(tR2<=tf)and(dsR1>radiO)and(dsR2>radiO)and(zF==0)and(TF==0)and(OF==0)and(EF==0):
        if(dsR1<radiO):
            print(dsR1)
        if(dsR2<radiO):
            print(dsR2)

        vR1.append(vR1)
        vR2.append(vR2)
        #auxz=Times(dt,vR1[i-1])

        
        qR1.append(Plus(Times(dt,vR1[i-1]),qR1[i-1]))#actualizar posiciones del Robot 1
        qR2.append(Plus(Times(dt,vR2[i-1]),qR2[i-1]))


        drR1=drR1+Norm(Minus(qR1[i],qR1[i-1]))#distancia recorrida
        drR2=drR2+Norm(Minus(qR2[i],qR2[i-1]))


        u[0]=qR1[i][0]
        u[1]=qR1[i][1]
        u[2]=qR2[i][0]
        u[3]=qR2[i][1]

        #Robot 1
        x1=qR1[i][0]
        y1=qR1[i][1]
        xRob1=x1
        yRob1=y1
        #Robot2
        x2=qR2[i][0]
        y2=qR2[i][1]
        xRob2=x2
        yRob2=y2

        dR1=Norm(Minus(qR1[i],pdR1))                #nueva distancia al objetivo
        dR2=Norm(Minus(qR2[i],pdR2))
        
        dsR1=Norm(Minus(qR1[i],qR2[i]))
        dsR2=Norm(Minus(qR2[i],qR1[i]))

        cd=CirclevirtualModel(Cd,phi,tR1)
        #cd=DaisyvirtualModel(Cd,tR1)
        #cd=GeronovirtualModel(Cd,tR1)
        PdR1=Plus(cd,Times(rCen,Vdir1))
        PdR2=Plus(cd,Times(rCen,Vdir2))    
        FlagsR1,vR1[i]=ModelKaF1TestRobot1(u,ind,r,u0R1)                 #obtener una nueva velocidad del robot 1
        VxR1,VyR1=vR1[i]
        FLR1.append(FlagsR1)
        FlagsR2,vR2[i]=ModelKaF1TestRobot2(u,ind,r,u0R2)                 #obtener una nueva velocidad del robot 2
        VxR2,VyR2=vR2[i]
        FLR2.append(FlagsR2)
        zeroF=FlagsR1[0]+FlagsR2[0]
        zF=zeroF
        TypeF=FlagsR1[1]+FlagsR2[1]
        TF=TypeF
        OverF=FlagsR1[2]+FlagsR2[2]
        OF=OverF
        ErrorF=FlagsR1[3]+FlagsR2[3]
        EF=ErrorF
        u[6]=VxR1
        u[7]=VyR1
        u[8]=VxR2
        u[9]=VyR2
        u[4]=PdR1
        u[5]=PdR2
        vrR1.append(vR1[i])
        tsR1.append(tR1)
        tsR2.append(tR2)

        Try1.append(qR1[i-1][0])#s.try
        Try2.append(qR1[i-1][1])
        
        Try3.append(qR2[i-1][0])
        Try4.append(qR2[i-1][1])
        
        
        dsR1a.append(dsR1)
        dsR2a.append(dsR2)

        doR1a.append(doR1)
        doR2a.append(doR2)
        dR1a.append(dR1)
        dR2a.append(dR2)
        drR1a.append(drR1)
        drR2a.append(drR2)
        vxR1.append(VxR1)
        vxR2.append(VxR2)
        vyR1.append(VyR1)
        vyR2.append(VyR2)
        cdxa.append(cd[0])
        cdya.append(cd[1])
        #Seccion de banderas
        i=i+1
        if(dR1<0.02)and((VxR1<0.001)and(VyR1<0.001)and(aux1==1)):
            aux1=2
            tR1saved=tR1
        if(dR2<0.02)and((VxR2<0.001)and(VyR2<0.001)and(aux2==1)):
            aux2=2
            tR2saved=tR2

        tR1=tR1+dt
        tR2=tR2+dt

        u[14]=tR1
        u[15]=tR2

        #archivo.write(str(xo1[i-1])+","+str(yo1[i-1])+","+str(v[i-1][0])+","+str(v[i-1][1])+","+str(t)+","+str(dr)+","+str(do)+","+str(d)+","+str(ds)+","+str(xc1)+","+str(yc1)+","+str(p[i-1])+"\n")
        s=[tR1saved,tR2saved,Try1,vxR1,vyR1,tsR1,drR1a,doR1a,dR1a,0,Try2,Try3,Try4,dsR1a,dR2a,vrR2,doR2a,drR2a,dsR2a,tsR2,dsR1,dsR2,vxR2,vyR2,zeroF,TypeF,OverF,ErrorF,0,0,0,0,cdxa,cdya]
        pdT=[PdR1,PdR2]
        vect=[r,pd,pdT]
    return s,vect


def CirclevirtualModel(Ci,phi,dt):
    vd=0.0
    x=Ci[0]+(np.sin(phi*dt)*vd)
    y=Ci[1]-(np.cos(phi*dt)*vd)
    return [x,y]

def DaisyvirtualModel(Ci,t):
    m=3
    st=30
    o=2*(3.1416)/st
    bt = 0.6
    at = 0.5
    rt = 0.6
    x= Ci[0] + bt*(at - rt*Cos(m*o*t))*Cos(o*t)
    y= Ci[1] + bt*(at -rt*Cos(m*o*t))*Sin(o*t)
    return [np.real(x),np.real(y)]
def GeronovirtualModel(Ci,t):
    a=0.50
    b=0.45
    st=10
    o=2*(3.1416)/st
    x = Ci[0]+a*Sin(o*t)
    y = Ci[1]+b*Sin(o*t)*Cos(o*t)
    return[np.real(x),np.real(y)]
