import intel_jtag_uart
import re

READ_ACCPROC_COMMAND = "R ACCPROC"
READ_ACCRAW_COMMAND = "R ACCRAW"
READ_BUTTON_COMMAND = "R BUTTON"
READ_SWITCH_COMMAND = "R SWITCH"
WRITE_HEXTEXT = "W HEXTEXT"
WRITE_LEDFLASH = "W LEDFLASH"

ACCPROC_REGEX = r"K ACCPROC X([\da-fA-F])Y([\da-fA-F])Z([\da-fA-F]) ([\da-fA-F])"
ACCRAW_REGEX = r"K ACCRAW X([\da-fA-F]+)Y([\da-fA-F]+)Z([\da-fA-F]+) ([\da-fA-F])"
BUTTON_REGEX = r"K BUTTON ([\da-fA-F]+) ([\da-fA-F])"
SWITCH_REGEX = r"K SWITCH ([\da-fA-F]) ([\da-fA-F])"
HEXTEXT_REGEX = r"K HEXTEXT ([\da-fA-F])"
LEDFLASH_REGEX = r"K LEDFLASH ([\da-fA-F])"


class FPGACommunicator:
    def __init__(self):
        try:
            self.ju = intel_jtag_uart.intel_jtag_uart()

        except Exception as e:
            print(e)

    def __get_command_output(self, command):
        self.ju.write((command + "\n").encode("utf-8"))
        return self.ju.read().decode("utf-8")

    def __read_value_and_error(self, command, regex):
        fpga_out = self.__get_command_output(command)
        response = {"value": 0, "error_code": 0}
        re_match = re.match(regex, fpga_out)
        if re_match is not None:
            response["value"] = int(re_match.group(1), 16)
            response["error_code"] = int(re_match.group(2), 16)
        return response

    def __read_acc(self, command, regex):
        fpga_out = self.__get_command_output(command)
        response = {"x": 0, "y": 0, "z": 0, "error_code": 0}
        re_match = re.match(regex, fpga_out)
        if re_match is not None:
            response["x"] = int(re_match.group(1))
            response["y"] = int(re_match.group(2))
            response["z"] = int(re_match.group(3))
            response["error_code"] = int(re_match.group(4))
        return response

    def __write_request(self, command, value, regex):
        final_command = command + " " + str(value) + "\n"
        fpga_out = self.__get_command_output(final_command)
        re_match = re.match(regex, fpga_out)
        if re_match is not None:
            return int(re_match.group(1), 16)
        return -1

    def read_acc_proc(self):
        return self.__read_acc(READ_ACCPROC_COMMAND, ACCPROC_REGEX)

    def read_acc_raw(self):
        return self.__read_acc(READ_ACCRAW_COMMAND, ACCRAW_REGEX)

    def read_button(self):
        return self.__read_value_and_error(READ_BUTTON_COMMAND, BUTTON_REGEX)

    def read_switch(self):
        return self.__read_value_and_error(READ_SWITCH_COMMAND, SWITCH_REGEX)

    def write_hextext(self, value):
        return self.__write_request(WRITE_HEXTEXT, value, HEXTEXT_REGEX)

    def write_ledflash(self, value):
        return self.__write_request(WRITE_LEDFLASH, value, LEDFLASH_REGEX)