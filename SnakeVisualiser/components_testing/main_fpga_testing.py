import time
from SnakeVisualiser.components.fpga_communicator import FPGACommunicator

TEST_ALL_PRINTS = True


def test_print_of_all_values():
    while True:
        print("---using R commands---")
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
        hextext_error_code = communicator.write_hextext("GAME_OVER_SCORE_25_PLACE_2")
        print("hextext error code: " + str(hextext_error_code))
        ledflash_error_code = communicator.write_ledflash("100010001")
        print("ledflash error code: " + str(ledflash_error_code))
        ledwrite_error_code = communicator.write_led(3)
        print("ledwrite error code: " + str(ledwrite_error_code))
        print("----using R ALL----")
        all_readings = communicator.read_all()
        print("accproc x: " + str(all_readings['ACCPROC']['x']) + " accproc y: " + str(all_readings['ACCPROC']['y'])
              + " accproc z: " + str(all_readings['ACCPROC']['z']) + " accproc error_code: " + str(
            all_readings['ACCPROC']['error_code'])
              + " accraw x: " + str(all_readings['ACCRAW']['x']) + " accraw y: " + str(
            all_readings['ACCRAW']['y']) + " accraw z: " + str(all_readings['ACCRAW']['z'])
              + " accraw error_code: " + str(all_readings['ACCRAW']['error_code']) + " button: " + str(
            all_readings['BUTTON']['value'])
              + " button error_code: " + str(all_readings['BUTTON']['value']) + " switch: " + str(
            all_readings['SWITCH']['value'])
              + " switch error_code: " + str(all_readings['SWITCH']['error_code']))


def test_directions():
    while True:
        acc_read = communicator.read_acc_proc()
        print("accproc x: " + str(acc_read['x']))
        print("accproc y: " + str(acc_read['y']))
        if 75 < acc_read['x'] < 250 and not 75 <= acc_read['y'] <= 4021:
            print('Left')
        elif 3750 < acc_read['x'] < 4021 and not 75 <= acc_read['y'] <= 4021:
            print('Right')
        elif 3750 < acc_read['y'] < 4021 and not 75 <= acc_read['x'] <= 4021:
            print('Up')
        if 75 < acc_read['y'] < 250 and not 75 <= acc_read['x'] <= 4021:
            print('Down')


if __name__ == '__main__':
    counter = 0
    acc_sum = 0
    communicator = FPGACommunicator()
    if TEST_ALL_PRINTS:
        test_print_of_all_values()
    else:
        test_directions()
