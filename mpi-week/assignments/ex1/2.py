from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("Hello World from process ", rank, " out of ", size, " processes")

MPI.Finalize()

