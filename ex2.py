# python3 ./number.py 42

import sys

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

number=np.array([0])

if rank==0:
    number[0] = sys.argv[1]

print(f"From process of rank {rank} the passnumber is {number[0]}")

comm.Bcast(number, root=0)

print (f"After collective in process of rank {rank} the passnumber is {number[0]}")