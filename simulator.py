import random
import time
from location import Location
import mysql.connector as mc

mydb=mc.connect(host='localhost',user='root',passwd='password')
curse=mydb.cursor(buffered=True)
curse.execute('use hackaccino')

min_garbage=0
max_garbage=100

no_of_bins=25
for i in range(1,no_of_bins+1):
    print("bin ",i)
    min_garbage=0
    max_garbage=100
    threshold=95
    j=1
    table="bin"+str(i)
    globals()["bin_"+str(i)]=Location(i,table)
    tablenaam=globals()["bin_"+str(i)].tablename
    #curse.execute("create table {}(Time varchar(100),Capacity integer)".format(tablenaam))
    
    while True:
        garbage_level=random.randint(min_garbage,max_garbage)
        current_time=time.ctime()
        garbage_time=str(current_time)
        #curse.execute("insert into {} values({},{})".format(tablenaam,garbage_time,garbage_level))
        print(current_time,garbage_level)
        min_garbage=garbage_level
        if garbage_level>threshold:
            globals()["bin_"+str(i)].signal()
            break
            
        time.sleep(10)
        mydb.commit()
    
    

print(bin_1.number)
print(bin_1.capacity)
print(bin_2.number)
print(bin_2.capacity)



       
