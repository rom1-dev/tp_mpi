import numpy as np
np.random.seed(0)

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

numbers = np.random.randint(0, 99, 10)

mins = np.empty_like(numbers) if rank==0 else None
maxs = np.empty_like(numbers) if rank==0 else None

comm.Reduce(numbers, mins, op=MPI.MIN, root=0)
comm.Reduce(numbers, maxs, op=MPI.MAX, root=0)

if rank==0:
    print(np.array_equal(mins, maxs))