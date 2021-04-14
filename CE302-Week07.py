##############################################
# 2021_0414-AAD: Parallel Processing Example #
##############################################

#%% First coding

import multiprocessing as mp


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

rakam = 100_000

# %%

if __name__ == "__main__" :

    t0 = time.time()

    results = []

    for i in  range( rakam ):
        results.append( random_squared(i) ) ;

    t1 = time.time()

    print( f"Serial Process: Time elapsed {round( t1-t0 , 3)} secods")

# %%

if __name__ == "__main__" :

    t0 = time.time()

    n_cpu = mp.cpu_count()

    pool = mp.Pool( processes= 4 , )

    results = [ pool.map( random_squared ,  range(rakam))]

    t1 = time.time()

    print( f"Parallel Process: Time elapsed {round( t1-t0 , 3)} secods")

# %%
