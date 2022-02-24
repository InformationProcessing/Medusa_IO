from fpga_communicator import FPGACommunicator


def test_print_of_all_values():
    while True:
        acc_proc_reading = communicator.read_acc_proc()
        print("accproc x: " + str(acc_proc_reading['x']) + " accproc y: " + str(acc_proc_reading['y']) + " accproc z: "
              + str(acc_proc_reading['z']) + " error code: " + str(acc_proc_reading['error_code']))
        acc_raw_reading = communicator.read_acc_raw()
        print("accraw x: " + str(acc_raw_reading['x']) + " accraw y: " + str(acc_raw_reading['y']) + " accraw z: "
              + str(acc_raw_reading['z']) + " error code: " + str(acc_raw_reading['error_code']))
        button_response = communicator.read_button()
        print("button value: " + str(button_response['value']) + " error_code " + str(button_response['error_code']))
        switch_response = communicator.read_switch()
        print("switch value: " + str(switch_response['value']) + " error_code " + str(switch_response['error_code']))
        hextext_error_code = communicator.write_hextext(123)
        print("hextext error code: " + str(hextext_error_code))
        ledflash_error_code = communicator.write_ledflash(11)
        print("ledflash error code: " + str(hextext_error_code))


if __name__ == '__main__':
    counter = 0
    acc_sum = 0
    communicator = FPGACommunicator()

    while True:
        acc_raw_reading = communicator.read_acc_raw()
        acc_value = acc_raw_reading['y']
        if acc_value > 200:
            acc_value = acc_value - 4294967295
        acc_value = acc_value + 10
        print(acc_value)
        if acc_value > 120:
            print("DOWN")
        elif acc_value < -120:
            print("UP")
        else:
            print("MIDDLE")
