from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # If we are rank 0, print message
    print("Hello World")

MPI.Finalize()

