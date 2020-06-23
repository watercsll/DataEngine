import numpy as np
personaltype = np.dtype({
    'names':['name','Chinese','Math','English'],
    'formats':['S32','f','f','f']
    })
score = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98),("LiuBei",98,86,88),("DianWei",90,88,77),("XuChu",80,90,90)],dtype = personaltype)
Chineses = score[:]['Chinese']
Maths = score[:]['Math']
Englishs = score[:]['English']
def statics(course,x):
    print(course,"/",np.mean(x),"/",np.amin(x),"/",np.amax(x),"/",np.std(x),"/",np.var(x));
print('Course',"/",'Average',"/",'Minimal',"/",'Max',"/",'Standard',"/",'Variation')
statics("Chinese",Chineses)
statics("Math",Maths)
statics("English",Englishs)
paiming = sorted(score,key=lambda x:x[1] + x[2] + x[3],reverse = True)
print(paiming)