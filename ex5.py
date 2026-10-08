import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

teams=np.zeros(size, dtype=int)

if rank==0:
    teams = np.random.randint(2, size=size, dtype=int)
    print(f"The file contains {teams}")

my_team = np.zeros(1, dtype=int)
comm.Scatter(teams, my_team, root=0)

colors = {0: 'blue', 1:'green'}

# import time
# time.sleep(rank/100)

print(f'I am {rank} and my team is {colors[my_team[0]]}')
