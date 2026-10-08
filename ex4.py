import sys

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def cumul(a,b):
    return sum(range(a,b))

nb = int(sys.argv[1])

a = rank*(nb//size)
b = (rank+1)*(nb//size)

local_res = cumul(a,b)

global_res = comm.Reduce(local_res, op=MPI.SUM, root=0)

if rank==0:
    print(f"global result : {global_res}")



# import time
# time.sleep(rank/100)
# print(f"{rank=}, {a=}, {b=}, {local_res=}")