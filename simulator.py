import random
import time
from location import Location
import mysql.connector as mc

mydb=mc.connect(host='localhost',user='root',passwd='password')
curse=mydb.cursor(buffered=True)
curse.execute('use hackaccino')

no_of_bins=3
def garbage_fill():
    for i in range(1,no_of_bins+1):
        print("bin ",i)
        min_garbage=0
        max_garbage=100
        threshold=95
        num=str(i)
        table="bin"+num
        globals()["bin_"+str(i)]=Location(i)
        q = "CREATE TABLE {} (Time varchar(255) Primary key, Capacity int)".format(table)  # Corrected query
        #curse.execute(q)
    
        while True:
            garbage_level = random.randint(min_garbage, max_garbage)
            current_time = time.ctime()
            garbage_time = str(current_time)
            x= "INSERT INTO {} (Time, Capacity) VALUES ('{}', {})".format(table, garbage_time, garbage_level)
            #curse.execute(x)
            print(current_time, garbage_level)
            min_garbage = garbage_level
            if garbage_level > threshold:
                globals()["bin_" + str(i)].signal()
                print("RED LIGHT")
                print("LID HAS BEEN CLOSED")
                #globals()["bin_" + str(i)].email()
                break

            time.sleep(3)
            mydb.commit()

    
#MENU BASED PROGRAM
#show data
def analytics():
    for i in range(1,no_of_bins+1):
        table="bin"+str(i)
        y="select * from {}".format(table)
        curse.execute(y)
        print("\n")
        print(table)
        print("   Time    Capacity")
        for row in curse.fetchall():
            print("\n")
            for l in row:
                print(l,end="\t")
                mydb.commit()


garbage_fill()
analytics()
curse.close()
mydb.close()



       
