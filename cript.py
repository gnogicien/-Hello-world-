from datetime import datetime

tampon = datetime.now()
tampon =str(tampon.time())

time_tableau = []
tp=""
t=0
l=0
tableau =[]
lignes_tableau=[]


for x in tampon[0:6]:
    if(x !=":"):
        t=int(x)+(t*10)
    else:
        time_tableau.append(t)
        t=0


with open("passwd","r" ) as textfile:
    tableau=textfile.read()
        
tableau = str(tableau)


for i in tableau:
    if (i=="\n"):
        l=l+1

with open("passwd","r" ) as textfile:
    for x in range(0,l):
      lignes_tableau.append(str(textfile.readline()))
         
for l in lignes_tableau:
    for x in str(l):
        if (x!= ":"):
            tp=tp+x
        else:
            print tp
            tp=""
            break
    
            
            


