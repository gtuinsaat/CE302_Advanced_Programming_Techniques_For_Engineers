##########################################################
#
#
#
##########################################################

#%%
import multiprocessing as mp 
print( f"cpu {mp.cpu_count()}")

# %%
import numpy as np
import time
def random_squared( seed) :
    np.random.seed(seed)
    random_num = np.random.randint(0,10)
    return random_num ** 2

#%%
rakam = 500_000
#%%
t0 = time.time()

results = []

for i in range( rakam):
    results.append( random_squared( i))
t1 = time.time()

print( f"Serial {t1-t0}s")

# %%
if __name__ = "__main__":
    t0 = time.time()
    n_cpu = mp.cpu_count()

    pool = mp.Pool( processes = n_cpu)

    results = [ pool.map( random_squared , range(rakam))]
    t1 = time.time()
    print( f"Parallel {t1-t0}s")

# %%
