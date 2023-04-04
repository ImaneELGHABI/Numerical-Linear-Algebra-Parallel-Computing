from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    num = int(input("Enter an integer: "))
    comm.send(num, dest=1)
    print("Process ", rank, " sent ", num)
else:
    num = comm.recv(source=rank-1)
    num += rank
    if rank == size - 1:
        comm.send(num, dest=0)
        print("Process ", rank, " sent ", num, " back to process 0")
    else:
        comm.send(num, dest=rank+1)
        print("Process ", rank, " received ", num, " and sent it to process ", rank+1)

MPI.Finalize()

