from fpga_communicator import FPGACommunicator

communicator = FPGACommunicator()

counter = 0
sum = 0

while True:
    counter = counter + 1
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

#    if counter == 3:
#        value = sum // 3
#        if value > 60:
#            print("LEFT")
#        elif value < -60:
#            print("RIGHT")
#        else:
#            print("MIDDLE")
#        sum = 0
#        counter = 0

#acc_value = acc_reading['x']
#if acc_value > 200:
#    acc_value = acc_value - 4294967295
#acc_value = acc_value + 20
#sum = sum + acc_value
