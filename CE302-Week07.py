##############################################
# 2021_0414-AAD: Parallel Processing Example #
##############################################

#%% First coding

import multiprocessing as mp
import pandas as pd


n_cpu = mp.cpu_count()

print( f"your computer has {n_cpu} CPU's")
# %%

import numpy as np 

import time 

#%%

def random_squared( seed ):
    np.random.seed()
    random_num = np.random.randint(0,10);
    return random_num ** 2
# %%

rakam = 1_000

# %%
timeSerial = pd.DataFrame(columns=["Rakam","TimeElapsed"])

if __name__ == "__main__" :

    t0 = time.time()

    results1 = []

    for i in  range( rakam ):
        results1.append( random_squared(i) ) ;

    t1 = time.time()
    timeElapsed = round( t1-t0 , 3)

    print( f"Serial Process: Time elapsed {timeElapsed} secods")

# %%

if __name__ == "__main__" :


    t0 = time.time()

    n_cpu = mp.cpu_count()

    pool = mp.Pool( processes= 4 , )

    results2 = [ pool.map( random_squared ,  range(rakam))]

    t1 = time.time()

    print( f"Parallel Process: Time elapsed {round( t1-t0 , 3)} secods")

# %%
