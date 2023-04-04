from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

while True:
    if rank == 0:
        num = int(input("Enter an integer: "))
        comm.bcast(num, root=0)
        if num < 0:
            break
    else:
        num = comm.bcast(None, root=0)
        if num < 0:
            break
    print("Process ", rank, " got ", num)

MPI.Finalize()

