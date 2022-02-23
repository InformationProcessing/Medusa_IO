import intel_jtag_uart
import re

ACC_FILTERED_READ_COMMAND = "r acc_fil"
ACC_RAW_READ_COMMAND = "r acc_raw"
START_COMMAND = "start"
START_COMMAND_ACK = "start ack"
END_COMMAND = "end"
END_COMMAND_ACK = "end ack"


class FPGACommunicator:
    def __init__(self):
        self.is_alive = False
        try:
            self.ju = intel_jtag_uart.intel_jtag_uart()

        except Exception as e:
            print(e)

    def start_comm(self):
        self.ju.write((START_COMMAND + "\n").encode("utf-8"))
        fpga_out = self.ju.read().decode("utf-8").replace("\n", "")
        if fpga_out == START_COMMAND_ACK:
            self.is_alive = True
            return True
        else:
            return False

    def end_comm(self):
        self.ju.write((END_COMMAND_ACK + "\n").encode("utf-8"))
        fpga_out = self.ju.read().decode("utf-8").replace("\n", "")
        if fpga_out == END_COMMAND_ACK:
            self.is_alive = False
            return True
        else:
            return False

    def __read_acc_samples(self, command, samples):
        self.ju.write((command + " " + str(samples) + "\n").encode("utf-8"))
        fpga_out_lines = self.ju.read().decode("utf-8").split("\n")

        samples = []

        for line in fpga_out_lines:
            re_match = re.match(r"acc: (\d+)", line)
            if re_match is not None:
                samples.append(int(re_match.group(1)))

        return samples

    def __read_acc(self, command):
        samples = self.__read_acc_samples(command, 1)
        if len(samples) == 1:
            return samples[0]
        return 0

    def read_acc_filtered(self):
        return self.__read_acc(ACC_FILTERED_READ_COMMAND)

    def read_acc_filtered_samples(self, samples=5):
        return self.__read_acc_samples(ACC_RAW_READ_COMMAND, samples)

    def read_acc_raw(self):
        return self.__read_acc(ACC_RAW_READ_COMMAND)

    def read_acc_raw_samples(self, samples=5):
        return self.__read_acc_samples(ACC_RAW_READ_COMMAND, samples)
