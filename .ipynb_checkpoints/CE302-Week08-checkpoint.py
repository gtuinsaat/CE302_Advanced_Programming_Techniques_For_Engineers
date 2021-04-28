##############################################
# 2021_0414-AAD: Multhithreading Example #
##############################################
# There are two approaches in code efficiency: 
# 1. Parallel process : splitting the cpus
# 2. Creating paralle threads
###############################

#%% IMPORTS

import os, pandas as pd , time , datetime, numpy as np 

import threading # module for multithreading

#%% 
exitFlag = 0

class MyThread( threading.Thread) :
    def __init__( self , threatID , name , my_delay) :
        threading.Thread.__init__(self)
        self.threatID = threatID
        self.name  = name 
        self.delay = my_delay
        
    def run(self):
        print( f"Starting : {self.name}" )

        print_time( self.name , self.delay , 5 )

        print( f"Exiting : {self.name}")

def print_time( threadName ,  my_delay , counter ):

    while counter :
        if exitFlag : 
            threadName.exit()
        time.sleep( my_delay )

        print( f"{threadName} : time is {time.ctime(time.time())}")

        counter -= 1

#%%
# Crate the threats

thread_1 = MyThread( 1 , "Thread name 1" , 1)

thread_2 = MyThread( 2 , "Thread name 2" , 5)

# Start the threads

#%%

thread_1.start()
thread_2.start()

print( f"The file is ok")

# %%
