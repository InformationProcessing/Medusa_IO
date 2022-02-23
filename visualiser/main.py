from fpga_communicator import FPGACommunicator

communicator = FPGACommunicator()

if communicator.start_comm():
    print("Communication started!")
    for x in range(0, 10):
        acc_value = communicator.read_acc_raw()
        print("accelerometer value: " + str(acc_value))
    communicator.end_comm()
    print("Communication ended!")
else:
    print("Communication wasn't established")
