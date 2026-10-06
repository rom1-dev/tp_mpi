import numpy as np
# np.random.seed(0)

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

numbers = np.random.randint(0, 99, 10)

minmax = np.array([min(numbers), max(numbers)])

# print(f"rank : {rank}, min : {minmax[0]}, max : {minmax[1]}")

if rank==0:
    res=np.empty((size, 2), dtype=int)
else:
    res=None

comm.Gather(minmax, res, root=0)
if rank==0:
    ref_min = res[0][0]
    ref_max = res[0][1]
    all_min_same = all(i[0]==ref_min for i in res)
    all_max_same = all(i[1]==ref_max for i in res)
    print(all_min_same and all_max_same)