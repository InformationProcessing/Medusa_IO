/*
 * system.h - SOPC Builder system and BSP software package information
 *
 * Machine generated for CPU 'cpu' in SOPC Builder design 'snake'
 * SOPC Builder design path: ../../snake.sopcinfo
 *
 * Generated: Sat Mar 19 18:38:25 UTC 2022
 */

/*
 * DO NOT MODIFY THIS FILE
 *
 * Changing this file will have subtle consequences
 * which will almost certainly lead to a nonfunctioning
 * system. If you do modify this file, be aware that your
 * changes will be overwritten and lost when this file
 * is generated again.
 *
 * DO NOT MODIFY THIS FILE
 */

/*
 * License Agreement
 *
 * Copyright (c) 2008
 * Altera Corporation, San Jose, California, USA.
 * All rights reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 *
 * This agreement shall be governed in all respects by the laws of the State
 * of California and by the laws of the United States of America.
 */

#ifndef __SYSTEM_H_
#define __SYSTEM_H_

/* Include definitions from linker script generator */
#include "linker.h"


/*
 * CPU configuration
 *
 */

#define ALT_CPU_ARCHITECTURE "altera_nios2_gen2"
#define ALT_CPU_BIG_ENDIAN 0
#define ALT_CPU_BREAK_ADDR 0x01000820
#define ALT_CPU_CPU_ARCH_NIOS2_R1
#define ALT_CPU_CPU_FREQ 120000000u
#define ALT_CPU_CPU_ID_SIZE 1
#define ALT_CPU_CPU_ID_VALUE 0x00000000
#define ALT_CPU_CPU_IMPLEMENTATION "tiny"
#define ALT_CPU_DATA_ADDR_WIDTH 0x19
#define ALT_CPU_DCACHE_LINE_SIZE 0
#define ALT_CPU_DCACHE_LINE_SIZE_LOG2 0
#define ALT_CPU_DCACHE_SIZE 0
#define ALT_CPU_EXCEPTION_ADDR 0x00800020
#define ALT_CPU_FLASH_ACCELERATOR_LINES 0
#define ALT_CPU_FLASH_ACCELERATOR_LINE_SIZE 0
#define ALT_CPU_FLUSHDA_SUPPORTED
#define ALT_CPU_FREQ 120000000
#define ALT_CPU_HARDWARE_DIVIDE_PRESENT 0
#define ALT_CPU_HARDWARE_MULTIPLY_PRESENT 0
#define ALT_CPU_HARDWARE_MULX_PRESENT 0
#define ALT_CPU_HAS_DEBUG_CORE 1
#define ALT_CPU_HAS_DEBUG_STUB
#define ALT_CPU_HAS_ILLEGAL_INSTRUCTION_EXCEPTION
#define ALT_CPU_HAS_JMPI_INSTRUCTION
#define ALT_CPU_ICACHE_LINE_SIZE 0
#define ALT_CPU_ICACHE_LINE_SIZE_LOG2 0
#define ALT_CPU_ICACHE_SIZE 0
#define ALT_CPU_INST_ADDR_WIDTH 0x19
#define ALT_CPU_NAME "cpu"
#define ALT_CPU_OCI_VERSION 1
#define ALT_CPU_RESET_ADDR 0x00800000


/*
 * CPU configuration (with legacy prefix - don't use these anymore)
 *
 */

#define NIOS2_BIG_ENDIAN 0
#define NIOS2_BREAK_ADDR 0x01000820
#define NIOS2_CPU_ARCH_NIOS2_R1
#define NIOS2_CPU_FREQ 120000000u
#define NIOS2_CPU_ID_SIZE 1
#define NIOS2_CPU_ID_VALUE 0x00000000
#define NIOS2_CPU_IMPLEMENTATION "tiny"
#define NIOS2_DATA_ADDR_WIDTH 0x19
#define NIOS2_DCACHE_LINE_SIZE 0
#define NIOS2_DCACHE_LINE_SIZE_LOG2 0
#define NIOS2_DCACHE_SIZE 0
#define NIOS2_EXCEPTION_ADDR 0x00800020
#define NIOS2_FLASH_ACCELERATOR_LINES 0
#define NIOS2_FLASH_ACCELERATOR_LINE_SIZE 0
#define NIOS2_FLUSHDA_SUPPORTED
#define NIOS2_HARDWARE_DIVIDE_PRESENT 0
#define NIOS2_HARDWARE_MULTIPLY_PRESENT 0
#define NIOS2_HARDWARE_MULX_PRESENT 0
#define NIOS2_HAS_DEBUG_CORE 1
#define NIOS2_HAS_DEBUG_STUB
#define NIOS2_HAS_ILLEGAL_INSTRUCTION_EXCEPTION
#define NIOS2_HAS_JMPI_INSTRUCTION
#define NIOS2_ICACHE_LINE_SIZE 0
#define NIOS2_ICACHE_LINE_SIZE_LOG2 0
#define NIOS2_ICACHE_SIZE 0
#define NIOS2_INST_ADDR_WIDTH 0x19
#define NIOS2_OCI_VERSION 1
#define NIOS2_RESET_ADDR 0x00800000


/*
 * Define for each module class mastered by the CPU
 *
 */

#define __ALTERA_AVALON_JTAG_UART
#define __ALTERA_AVALON_NEW_SDRAM_CONTROLLER
#define __ALTERA_AVALON_PIO
#define __ALTERA_AVALON_SYSID_QSYS
#define __ALTERA_AVALON_TIMER
#define __ALTERA_NIOS2_GEN2
#define __ALTERA_UP_AVALON_ACCELEROMETER_SPI
#define __ALTPLL


/*
 * System configuration
 *
 */

#define ALT_DEVICE_FAMILY "MAX 10"
#define ALT_IRQ_BASE NULL
#define ALT_LEGACY_INTERRUPT_API_PRESENT
#define ALT_LOG_PORT "/dev/null"
#define ALT_LOG_PORT_BASE 0x0
#define ALT_LOG_PORT_DEV null
#define ALT_LOG_PORT_TYPE ""
#define ALT_NUM_EXTERNAL_INTERRUPT_CONTROLLERS 0
#define ALT_NUM_INTERNAL_INTERRUPT_CONTROLLERS 1
#define ALT_NUM_INTERRUPT_CONTROLLERS 1
#define ALT_STDERR "/dev/jtag_uart"
#define ALT_STDERR_BASE 0x1001278
#define ALT_STDERR_DEV jtag_uart
#define ALT_STDERR_IS_JTAG_UART
#define ALT_STDERR_PRESENT
#define ALT_STDERR_TYPE "altera_avalon_jtag_uart"
#define ALT_STDIN "/dev/jtag_uart"
#define ALT_STDIN_BASE 0x1001278
#define ALT_STDIN_DEV jtag_uart
#define ALT_STDIN_IS_JTAG_UART
#define ALT_STDIN_PRESENT
#define ALT_STDIN_TYPE "altera_avalon_jtag_uart"
#define ALT_STDOUT "/dev/jtag_uart"
#define ALT_STDOUT_BASE 0x1001278
#define ALT_STDOUT_DEV jtag_uart
#define ALT_STDOUT_IS_JTAG_UART
#define ALT_STDOUT_PRESENT
#define ALT_STDOUT_TYPE "altera_avalon_jtag_uart"
#define ALT_SYSTEM_NAME "snake"


/*
 * acc_timer configuration
 *
 */

#define ACC_TIMER_ALWAYS_RUN 0
#define ACC_TIMER_BASE 0x10010c0
#define ACC_TIMER_COUNTER_SIZE 32
#define ACC_TIMER_FIXED_PERIOD 0
#define ACC_TIMER_FREQ 120000000
#define ACC_TIMER_IRQ 9
#define ACC_TIMER_IRQ_INTERRUPT_CONTROLLER_ID 0
#define ACC_TIMER_LOAD_VALUE 119999
#define ACC_TIMER_MULT 0.001
#define ACC_TIMER_NAME "/dev/acc_timer"
#define ACC_TIMER_PERIOD 1
#define ACC_TIMER_PERIOD_UNITS "ms"
#define ACC_TIMER_RESET_OUTPUT 0
#define ACC_TIMER_SNAPSHOT 1
#define ACC_TIMER_SPAN 32
#define ACC_TIMER_TICKS_PER_SEC 1000
#define ACC_TIMER_TIMEOUT_PULSE_OUTPUT 0
#define ACC_TIMER_TYPE "altera_avalon_timer"
#define ALT_MODULE_CLASS_acc_timer altera_avalon_timer


/*
 * accelerometer_spi configuration
 *
 */

#define ACCELEROMETER_SPI_BASE 0x1001280
#define ACCELEROMETER_SPI_IRQ 0
#define ACCELEROMETER_SPI_IRQ_INTERRUPT_CONTROLLER_ID 0
#define ACCELEROMETER_SPI_NAME "/dev/accelerometer_spi"
#define ACCELEROMETER_SPI_SPAN 2
#define ACCELEROMETER_SPI_TYPE "altera_up_avalon_accelerometer_spi"
#define ALT_MODULE_CLASS_accelerometer_spi altera_up_avalon_accelerometer_spi


/*
 * altpll configuration
 *
 */

#define ALTPLL_BASE 0x1001260
#define ALTPLL_IRQ -1
#define ALTPLL_IRQ_INTERRUPT_CONTROLLER_ID -1
#define ALTPLL_NAME "/dev/altpll"
#define ALTPLL_SPAN 16
#define ALTPLL_TYPE "altpll"
#define ALT_MODULE_CLASS_altpll altpll


/*
 * button configuration
 *
 */

#define ALT_MODULE_CLASS_button altera_avalon_pio
#define BUTTON_BASE 0x10011d0
#define BUTTON_BIT_CLEARING_EDGE_REGISTER 0
#define BUTTON_BIT_MODIFYING_OUTPUT_REGISTER 0
#define BUTTON_CAPTURE 0
#define BUTTON_DATA_WIDTH 2
#define BUTTON_DO_TEST_BENCH_WIRING 0
#define BUTTON_DRIVEN_SIM_VALUE 0
#define BUTTON_EDGE_TYPE "NONE"
#define BUTTON_FREQ 120000000
#define BUTTON_HAS_IN 1
#define BUTTON_HAS_OUT 0
#define BUTTON_HAS_TRI 0
#define BUTTON_IRQ -1
#define BUTTON_IRQ_INTERRUPT_CONTROLLER_ID -1
#define BUTTON_IRQ_TYPE "NONE"
#define BUTTON_NAME "/dev/button"
#define BUTTON_RESET_VALUE 0
#define BUTTON_SPAN 16
#define BUTTON_TYPE "altera_avalon_pio"


/*
 * hal configuration
 *
 */

#define ALT_INCLUDE_INSTRUCTION_RELATED_EXCEPTION_API
#define ALT_MAX_FD 4
#define ALT_SYS_CLK none
#define ALT_TIMESTAMP_CLK TIMESTAMP_TIMER


/*
 * hardware_clocks configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_clocks altera_avalon_pio
#define HARDWARE_CLOCKS_BASE 0x10011a0
#define HARDWARE_CLOCKS_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_CLOCKS_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_CLOCKS_CAPTURE 0
#define HARDWARE_CLOCKS_DATA_WIDTH 4
#define HARDWARE_CLOCKS_DO_TEST_BENCH_WIRING 0
#define HARDWARE_CLOCKS_DRIVEN_SIM_VALUE 0
#define HARDWARE_CLOCKS_EDGE_TYPE "NONE"
#define HARDWARE_CLOCKS_FREQ 120000000
#define HARDWARE_CLOCKS_HAS_IN 0
#define HARDWARE_CLOCKS_HAS_OUT 1
#define HARDWARE_CLOCKS_HAS_TRI 0
#define HARDWARE_CLOCKS_IRQ -1
#define HARDWARE_CLOCKS_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_CLOCKS_IRQ_TYPE "NONE"
#define HARDWARE_CLOCKS_NAME "/dev/hardware_clocks"
#define HARDWARE_CLOCKS_RESET_VALUE 0
#define HARDWARE_CLOCKS_SPAN 16
#define HARDWARE_CLOCKS_TYPE "altera_avalon_pio"


/*
 * hardware_in_x configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_in_x altera_avalon_pio
#define HARDWARE_IN_X_BASE 0x10011b0
#define HARDWARE_IN_X_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_IN_X_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_IN_X_CAPTURE 0
#define HARDWARE_IN_X_DATA_WIDTH 31
#define HARDWARE_IN_X_DO_TEST_BENCH_WIRING 0
#define HARDWARE_IN_X_DRIVEN_SIM_VALUE 0
#define HARDWARE_IN_X_EDGE_TYPE "NONE"
#define HARDWARE_IN_X_FREQ 120000000
#define HARDWARE_IN_X_HAS_IN 1
#define HARDWARE_IN_X_HAS_OUT 0
#define HARDWARE_IN_X_HAS_TRI 0
#define HARDWARE_IN_X_IRQ -1
#define HARDWARE_IN_X_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_IN_X_IRQ_TYPE "NONE"
#define HARDWARE_IN_X_NAME "/dev/hardware_in_x"
#define HARDWARE_IN_X_RESET_VALUE 0
#define HARDWARE_IN_X_SPAN 16
#define HARDWARE_IN_X_TYPE "altera_avalon_pio"


/*
 * hardware_in_y configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_in_y altera_avalon_pio
#define HARDWARE_IN_Y_BASE 0x1001190
#define HARDWARE_IN_Y_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_IN_Y_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_IN_Y_CAPTURE 0
#define HARDWARE_IN_Y_DATA_WIDTH 31
#define HARDWARE_IN_Y_DO_TEST_BENCH_WIRING 0
#define HARDWARE_IN_Y_DRIVEN_SIM_VALUE 0
#define HARDWARE_IN_Y_EDGE_TYPE "NONE"
#define HARDWARE_IN_Y_FREQ 120000000
#define HARDWARE_IN_Y_HAS_IN 1
#define HARDWARE_IN_Y_HAS_OUT 0
#define HARDWARE_IN_Y_HAS_TRI 0
#define HARDWARE_IN_Y_IRQ -1
#define HARDWARE_IN_Y_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_IN_Y_IRQ_TYPE "NONE"
#define HARDWARE_IN_Y_NAME "/dev/hardware_in_y"
#define HARDWARE_IN_Y_RESET_VALUE 0
#define HARDWARE_IN_Y_SPAN 16
#define HARDWARE_IN_Y_TYPE "altera_avalon_pio"


/*
 * hardware_in_z configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_in_z altera_avalon_pio
#define HARDWARE_IN_Z_BASE 0x1001160
#define HARDWARE_IN_Z_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_IN_Z_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_IN_Z_CAPTURE 0
#define HARDWARE_IN_Z_DATA_WIDTH 31
#define HARDWARE_IN_Z_DO_TEST_BENCH_WIRING 0
#define HARDWARE_IN_Z_DRIVEN_SIM_VALUE 0
#define HARDWARE_IN_Z_EDGE_TYPE "NONE"
#define HARDWARE_IN_Z_FREQ 120000000
#define HARDWARE_IN_Z_HAS_IN 1
#define HARDWARE_IN_Z_HAS_OUT 0
#define HARDWARE_IN_Z_HAS_TRI 0
#define HARDWARE_IN_Z_IRQ -1
#define HARDWARE_IN_Z_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_IN_Z_IRQ_TYPE "NONE"
#define HARDWARE_IN_Z_NAME "/dev/hardware_in_z"
#define HARDWARE_IN_Z_RESET_VALUE 0
#define HARDWARE_IN_Z_SPAN 16
#define HARDWARE_IN_Z_TYPE "altera_avalon_pio"


/*
 * hardware_out_x configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_out_x altera_avalon_pio
#define HARDWARE_OUT_X_BASE 0x10011c0
#define HARDWARE_OUT_X_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_OUT_X_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_OUT_X_CAPTURE 0
#define HARDWARE_OUT_X_DATA_WIDTH 31
#define HARDWARE_OUT_X_DO_TEST_BENCH_WIRING 0
#define HARDWARE_OUT_X_DRIVEN_SIM_VALUE 0
#define HARDWARE_OUT_X_EDGE_TYPE "NONE"
#define HARDWARE_OUT_X_FREQ 120000000
#define HARDWARE_OUT_X_HAS_IN 0
#define HARDWARE_OUT_X_HAS_OUT 1
#define HARDWARE_OUT_X_HAS_TRI 0
#define HARDWARE_OUT_X_IRQ -1
#define HARDWARE_OUT_X_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_OUT_X_IRQ_TYPE "NONE"
#define HARDWARE_OUT_X_NAME "/dev/hardware_out_x"
#define HARDWARE_OUT_X_RESET_VALUE 0
#define HARDWARE_OUT_X_SPAN 16
#define HARDWARE_OUT_X_TYPE "altera_avalon_pio"


/*
 * hardware_out_y configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_out_y altera_avalon_pio
#define HARDWARE_OUT_Y_BASE 0x1001180
#define HARDWARE_OUT_Y_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_OUT_Y_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_OUT_Y_CAPTURE 0
#define HARDWARE_OUT_Y_DATA_WIDTH 31
#define HARDWARE_OUT_Y_DO_TEST_BENCH_WIRING 0
#define HARDWARE_OUT_Y_DRIVEN_SIM_VALUE 0
#define HARDWARE_OUT_Y_EDGE_TYPE "NONE"
#define HARDWARE_OUT_Y_FREQ 120000000
#define HARDWARE_OUT_Y_HAS_IN 0
#define HARDWARE_OUT_Y_HAS_OUT 1
#define HARDWARE_OUT_Y_HAS_TRI 0
#define HARDWARE_OUT_Y_IRQ -1
#define HARDWARE_OUT_Y_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_OUT_Y_IRQ_TYPE "NONE"
#define HARDWARE_OUT_Y_NAME "/dev/hardware_out_y"
#define HARDWARE_OUT_Y_RESET_VALUE 0
#define HARDWARE_OUT_Y_SPAN 16
#define HARDWARE_OUT_Y_TYPE "altera_avalon_pio"


/*
 * hardware_out_z configuration
 *
 */

#define ALT_MODULE_CLASS_hardware_out_z altera_avalon_pio
#define HARDWARE_OUT_Z_BASE 0x1001170
#define HARDWARE_OUT_Z_BIT_CLEARING_EDGE_REGISTER 0
#define HARDWARE_OUT_Z_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HARDWARE_OUT_Z_CAPTURE 0
#define HARDWARE_OUT_Z_DATA_WIDTH 31
#define HARDWARE_OUT_Z_DO_TEST_BENCH_WIRING 0
#define HARDWARE_OUT_Z_DRIVEN_SIM_VALUE 0
#define HARDWARE_OUT_Z_EDGE_TYPE "NONE"
#define HARDWARE_OUT_Z_FREQ 120000000
#define HARDWARE_OUT_Z_HAS_IN 0
#define HARDWARE_OUT_Z_HAS_OUT 1
#define HARDWARE_OUT_Z_HAS_TRI 0
#define HARDWARE_OUT_Z_IRQ -1
#define HARDWARE_OUT_Z_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HARDWARE_OUT_Z_IRQ_TYPE "NONE"
#define HARDWARE_OUT_Z_NAME "/dev/hardware_out_z"
#define HARDWARE_OUT_Z_RESET_VALUE 0
#define HARDWARE_OUT_Z_SPAN 16
#define HARDWARE_OUT_Z_TYPE "altera_avalon_pio"


/*
 * hex0 configuration
 *
 */

#define ALT_MODULE_CLASS_hex0 altera_avalon_pio
#define HEX0_BASE 0x10011f0
#define HEX0_BIT_CLEARING_EDGE_REGISTER 0
#define HEX0_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX0_CAPTURE 0
#define HEX0_DATA_WIDTH 8
#define HEX0_DO_TEST_BENCH_WIRING 0
#define HEX0_DRIVEN_SIM_VALUE 0
#define HEX0_EDGE_TYPE "NONE"
#define HEX0_FREQ 120000000
#define HEX0_HAS_IN 0
#define HEX0_HAS_OUT 1
#define HEX0_HAS_TRI 0
#define HEX0_IRQ -1
#define HEX0_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX0_IRQ_TYPE "NONE"
#define HEX0_NAME "/dev/hex0"
#define HEX0_RESET_VALUE 137
#define HEX0_SPAN 16
#define HEX0_TYPE "altera_avalon_pio"


/*
 * hex1 configuration
 *
 */

#define ALT_MODULE_CLASS_hex1 altera_avalon_pio
#define HEX1_BASE 0x1001200
#define HEX1_BIT_CLEARING_EDGE_REGISTER 0
#define HEX1_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX1_CAPTURE 0
#define HEX1_DATA_WIDTH 8
#define HEX1_DO_TEST_BENCH_WIRING 0
#define HEX1_DRIVEN_SIM_VALUE 0
#define HEX1_EDGE_TYPE "NONE"
#define HEX1_FREQ 120000000
#define HEX1_HAS_IN 0
#define HEX1_HAS_OUT 1
#define HEX1_HAS_TRI 0
#define HEX1_IRQ -1
#define HEX1_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX1_IRQ_TYPE "NONE"
#define HEX1_NAME "/dev/hex1"
#define HEX1_RESET_VALUE 146
#define HEX1_SPAN 16
#define HEX1_TYPE "altera_avalon_pio"


/*
 * hex2 configuration
 *
 */

#define ALT_MODULE_CLASS_hex2 altera_avalon_pio
#define HEX2_BASE 0x1001210
#define HEX2_BIT_CLEARING_EDGE_REGISTER 0
#define HEX2_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX2_CAPTURE 0
#define HEX2_DATA_WIDTH 8
#define HEX2_DO_TEST_BENCH_WIRING 0
#define HEX2_DRIVEN_SIM_VALUE 0
#define HEX2_EDGE_TYPE "NONE"
#define HEX2_FREQ 120000000
#define HEX2_HAS_IN 0
#define HEX2_HAS_OUT 1
#define HEX2_HAS_TRI 0
#define HEX2_IRQ -1
#define HEX2_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX2_IRQ_TYPE "NONE"
#define HEX2_NAME "/dev/hex2"
#define HEX2_RESET_VALUE 136
#define HEX2_SPAN 16
#define HEX2_TYPE "altera_avalon_pio"


/*
 * hex3 configuration
 *
 */

#define ALT_MODULE_CLASS_hex3 altera_avalon_pio
#define HEX3_BASE 0x1001220
#define HEX3_BIT_CLEARING_EDGE_REGISTER 0
#define HEX3_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX3_CAPTURE 0
#define HEX3_DATA_WIDTH 8
#define HEX3_DO_TEST_BENCH_WIRING 0
#define HEX3_DRIVEN_SIM_VALUE 0
#define HEX3_EDGE_TYPE "NONE"
#define HEX3_FREQ 120000000
#define HEX3_HAS_IN 0
#define HEX3_HAS_OUT 1
#define HEX3_HAS_TRI 0
#define HEX3_IRQ -1
#define HEX3_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX3_IRQ_TYPE "NONE"
#define HEX3_NAME "/dev/hex3"
#define HEX3_RESET_VALUE 199
#define HEX3_SPAN 16
#define HEX3_TYPE "altera_avalon_pio"


/*
 * hex4 configuration
 *
 */

#define ALT_MODULE_CLASS_hex4 altera_avalon_pio
#define HEX4_BASE 0x1001230
#define HEX4_BIT_CLEARING_EDGE_REGISTER 0
#define HEX4_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX4_CAPTURE 0
#define HEX4_DATA_WIDTH 8
#define HEX4_DO_TEST_BENCH_WIRING 0
#define HEX4_DRIVEN_SIM_VALUE 0
#define HEX4_EDGE_TYPE "NONE"
#define HEX4_FREQ 120000000
#define HEX4_HAS_IN 0
#define HEX4_HAS_OUT 1
#define HEX4_HAS_TRI 0
#define HEX4_IRQ -1
#define HEX4_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX4_IRQ_TYPE "NONE"
#define HEX4_NAME "/dev/hex4"
#define HEX4_RESET_VALUE 142
#define HEX4_SPAN 16
#define HEX4_TYPE "altera_avalon_pio"


/*
 * hex5 configuration
 *
 */

#define ALT_MODULE_CLASS_hex5 altera_avalon_pio
#define HEX5_BASE 0x1001240
#define HEX5_BIT_CLEARING_EDGE_REGISTER 0
#define HEX5_BIT_MODIFYING_OUTPUT_REGISTER 0
#define HEX5_CAPTURE 0
#define HEX5_DATA_WIDTH 8
#define HEX5_DO_TEST_BENCH_WIRING 0
#define HEX5_DRIVEN_SIM_VALUE 0
#define HEX5_EDGE_TYPE "NONE"
#define HEX5_FREQ 120000000
#define HEX5_HAS_IN 0
#define HEX5_HAS_OUT 1
#define HEX5_HAS_TRI 0
#define HEX5_IRQ -1
#define HEX5_IRQ_INTERRUPT_CONTROLLER_ID -1
#define HEX5_IRQ_TYPE "NONE"
#define HEX5_NAME "/dev/hex5"
#define HEX5_RESET_VALUE 255
#define HEX5_SPAN 16
#define HEX5_TYPE "altera_avalon_pio"


/*
 * hex_timer configuration
 *
 */

#define ALT_MODULE_CLASS_hex_timer altera_avalon_timer
#define HEX_TIMER_ALWAYS_RUN 0
#define HEX_TIMER_BASE 0x10010e0
#define HEX_TIMER_COUNTER_SIZE 32
#define HEX_TIMER_FIXED_PERIOD 0
#define HEX_TIMER_FREQ 120000000
#define HEX_TIMER_IRQ 8
#define HEX_TIMER_IRQ_INTERRUPT_CONTROLLER_ID 0
#define HEX_TIMER_LOAD_VALUE 119999
#define HEX_TIMER_MULT 0.001
#define HEX_TIMER_NAME "/dev/hex_timer"
#define HEX_TIMER_PERIOD 1
#define HEX_TIMER_PERIOD_UNITS "ms"
#define HEX_TIMER_RESET_OUTPUT 0
#define HEX_TIMER_SNAPSHOT 1
#define HEX_TIMER_SPAN 32
#define HEX_TIMER_TICKS_PER_SEC 1000
#define HEX_TIMER_TIMEOUT_PULSE_OUTPUT 0
#define HEX_TIMER_TYPE "altera_avalon_timer"


/*
 * jtag_uart configuration
 *
 */

#define ALT_MODULE_CLASS_jtag_uart altera_avalon_jtag_uart
#define JTAG_UART_BASE 0x1001278
#define JTAG_UART_IRQ 1
#define JTAG_UART_IRQ_INTERRUPT_CONTROLLER_ID 0
#define JTAG_UART_NAME "/dev/jtag_uart"
#define JTAG_UART_READ_DEPTH 64
#define JTAG_UART_READ_THRESHOLD 8
#define JTAG_UART_SPAN 8
#define JTAG_UART_TYPE "altera_avalon_jtag_uart"
#define JTAG_UART_WRITE_DEPTH 64
#define JTAG_UART_WRITE_THRESHOLD 8


/*
 * led configuration
 *
 */

#define ALT_MODULE_CLASS_led altera_avalon_pio
#define LED_BASE 0x1001250
#define LED_BIT_CLEARING_EDGE_REGISTER 0
#define LED_BIT_MODIFYING_OUTPUT_REGISTER 0
#define LED_CAPTURE 0
#define LED_DATA_WIDTH 10
#define LED_DO_TEST_BENCH_WIRING 0
#define LED_DRIVEN_SIM_VALUE 0
#define LED_EDGE_TYPE "NONE"
#define LED_FREQ 120000000
#define LED_HAS_IN 0
#define LED_HAS_OUT 1
#define LED_HAS_TRI 0
#define LED_IRQ -1
#define LED_IRQ_INTERRUPT_CONTROLLER_ID -1
#define LED_IRQ_TYPE "NONE"
#define LED_NAME "/dev/led"
#define LED_RESET_VALUE 0
#define LED_SPAN 16
#define LED_TYPE "altera_avalon_pio"


/*
 * sdram configuration
 *
 */

#define ALT_MODULE_CLASS_sdram altera_avalon_new_sdram_controller
#define SDRAM_BASE 0x800000
#define SDRAM_CAS_LATENCY 3
#define SDRAM_CONTENTS_INFO
#define SDRAM_INIT_NOP_DELAY 0.0
#define SDRAM_INIT_REFRESH_COMMANDS 2
#define SDRAM_IRQ -1
#define SDRAM_IRQ_INTERRUPT_CONTROLLER_ID -1
#define SDRAM_IS_INITIALIZED 1
#define SDRAM_NAME "/dev/sdram"
#define SDRAM_POWERUP_DELAY 100.0
#define SDRAM_REFRESH_PERIOD 15.625
#define SDRAM_REGISTER_DATA_IN 1
#define SDRAM_SDRAM_ADDR_WIDTH 0x16
#define SDRAM_SDRAM_BANK_WIDTH 2
#define SDRAM_SDRAM_COL_WIDTH 8
#define SDRAM_SDRAM_DATA_WIDTH 16
#define SDRAM_SDRAM_NUM_BANKS 4
#define SDRAM_SDRAM_NUM_CHIPSELECTS 1
#define SDRAM_SDRAM_ROW_WIDTH 12
#define SDRAM_SHARED_DATA 0
#define SDRAM_SIM_MODEL_BASE 0
#define SDRAM_SPAN 8388608
#define SDRAM_STARVATION_INDICATOR 0
#define SDRAM_TRISTATE_BRIDGE_SLAVE ""
#define SDRAM_TYPE "altera_avalon_new_sdram_controller"
#define SDRAM_T_AC 5.5
#define SDRAM_T_MRD 3
#define SDRAM_T_RCD 20.0
#define SDRAM_T_RFC 70.0
#define SDRAM_T_RP 20.0
#define SDRAM_T_WR 14.0


/*
 * switch configuration
 *
 */

#define ALT_MODULE_CLASS_switch altera_avalon_pio
#define SWITCH_BASE 0x10011e0
#define SWITCH_BIT_CLEARING_EDGE_REGISTER 0
#define SWITCH_BIT_MODIFYING_OUTPUT_REGISTER 0
#define SWITCH_CAPTURE 0
#define SWITCH_DATA_WIDTH 10
#define SWITCH_DO_TEST_BENCH_WIRING 0
#define SWITCH_DRIVEN_SIM_VALUE 0
#define SWITCH_EDGE_TYPE "NONE"
#define SWITCH_FREQ 120000000
#define SWITCH_HAS_IN 1
#define SWITCH_HAS_OUT 0
#define SWITCH_HAS_TRI 0
#define SWITCH_IRQ -1
#define SWITCH_IRQ_INTERRUPT_CONTROLLER_ID -1
#define SWITCH_IRQ_TYPE "NONE"
#define SWITCH_NAME "/dev/switch"
#define SWITCH_RESET_VALUE 0
#define SWITCH_SPAN 16
#define SWITCH_TYPE "altera_avalon_pio"


/*
 * sysid configuration
 *
 */

#define ALT_MODULE_CLASS_sysid altera_avalon_sysid_qsys
#define SYSID_BASE 0x1001270
#define SYSID_ID 0
#define SYSID_IRQ -1
#define SYSID_IRQ_INTERRUPT_CONTROLLER_ID -1
#define SYSID_NAME "/dev/sysid"
#define SYSID_SPAN 8
#define SYSID_TIMESTAMP 1647714880
#define SYSID_TYPE "altera_avalon_sysid_qsys"


/*
 * timer configuration
 *
 */

#define ALT_MODULE_CLASS_timer altera_avalon_timer
#define TIMER_ALWAYS_RUN 0
#define TIMER_BASE 0x1001120
#define TIMER_COUNTER_SIZE 32
#define TIMER_FIXED_PERIOD 0
#define TIMER_FREQ 120000000
#define TIMER_IRQ 5
#define TIMER_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMER_LOAD_VALUE 119999
#define TIMER_MULT 0.001
#define TIMER_NAME "/dev/timer"
#define TIMER_PERIOD 1
#define TIMER_PERIOD_UNITS "ms"
#define TIMER_RESET_OUTPUT 0
#define TIMER_SNAPSHOT 1
#define TIMER_SPAN 32
#define TIMER_TICKS_PER_SEC 1000
#define TIMER_TIMEOUT_PULSE_OUTPUT 0
#define TIMER_TYPE "altera_avalon_timer"


/*
 * timer0 configuration
 *
 */

#define ALT_MODULE_CLASS_timer0 altera_avalon_timer
#define TIMER0_ALWAYS_RUN 0
#define TIMER0_BASE 0x1001100
#define TIMER0_COUNTER_SIZE 32
#define TIMER0_FIXED_PERIOD 0
#define TIMER0_FREQ 120000000
#define TIMER0_IRQ 7
#define TIMER0_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMER0_LOAD_VALUE 119999
#define TIMER0_MULT 0.001
#define TIMER0_NAME "/dev/timer0"
#define TIMER0_PERIOD 1
#define TIMER0_PERIOD_UNITS "ms"
#define TIMER0_RESET_OUTPUT 0
#define TIMER0_SNAPSHOT 1
#define TIMER0_SPAN 32
#define TIMER0_TICKS_PER_SEC 1000
#define TIMER0_TIMEOUT_PULSE_OUTPUT 0
#define TIMER0_TYPE "altera_avalon_timer"


/*
 * timer1 configuration
 *
 */

#define ALT_MODULE_CLASS_timer1 altera_avalon_timer
#define TIMER1_ALWAYS_RUN 0
#define TIMER1_BASE 0x1001140
#define TIMER1_COUNTER_SIZE 32
#define TIMER1_FIXED_PERIOD 0
#define TIMER1_FREQ 120000000
#define TIMER1_IRQ 4
#define TIMER1_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMER1_LOAD_VALUE 119999
#define TIMER1_MULT 0.001
#define TIMER1_NAME "/dev/timer1"
#define TIMER1_PERIOD 1
#define TIMER1_PERIOD_UNITS "ms"
#define TIMER1_RESET_OUTPUT 0
#define TIMER1_SNAPSHOT 1
#define TIMER1_SPAN 32
#define TIMER1_TICKS_PER_SEC 1000
#define TIMER1_TIMEOUT_PULSE_OUTPUT 0
#define TIMER1_TYPE "altera_avalon_timer"


/*
 * timer3 configuration
 *
 */

#define ALT_MODULE_CLASS_timer3 altera_avalon_timer
#define TIMER3_ALWAYS_RUN 0
#define TIMER3_BASE 0x1001040
#define TIMER3_COUNTER_SIZE 64
#define TIMER3_FIXED_PERIOD 0
#define TIMER3_FREQ 120000000
#define TIMER3_IRQ 3
#define TIMER3_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMER3_LOAD_VALUE 119999
#define TIMER3_MULT 0.001
#define TIMER3_NAME "/dev/timer3"
#define TIMER3_PERIOD 1
#define TIMER3_PERIOD_UNITS "ms"
#define TIMER3_RESET_OUTPUT 0
#define TIMER3_SNAPSHOT 1
#define TIMER3_SPAN 64
#define TIMER3_TICKS_PER_SEC 1000
#define TIMER3_TIMEOUT_PULSE_OUTPUT 0
#define TIMER3_TYPE "altera_avalon_timer"


/*
 * timer4 configuration
 *
 */

#define ALT_MODULE_CLASS_timer4 altera_avalon_timer
#define TIMER4_ALWAYS_RUN 0
#define TIMER4_BASE 0x1001080
#define TIMER4_COUNTER_SIZE 64
#define TIMER4_FIXED_PERIOD 0
#define TIMER4_FREQ 120000000
#define TIMER4_IRQ 2
#define TIMER4_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMER4_LOAD_VALUE 119999
#define TIMER4_MULT 0.001
#define TIMER4_NAME "/dev/timer4"
#define TIMER4_PERIOD 1
#define TIMER4_PERIOD_UNITS "ms"
#define TIMER4_RESET_OUTPUT 0
#define TIMER4_SNAPSHOT 1
#define TIMER4_SPAN 64
#define TIMER4_TICKS_PER_SEC 1000
#define TIMER4_TIMEOUT_PULSE_OUTPUT 0
#define TIMER4_TYPE "altera_avalon_timer"


/*
 * timestamp_timer configuration
 *
 */

#define ALT_MODULE_CLASS_timestamp_timer altera_avalon_timer
#define TIMESTAMP_TIMER_ALWAYS_RUN 0
#define TIMESTAMP_TIMER_BASE 0x1001000
#define TIMESTAMP_TIMER_COUNTER_SIZE 64
#define TIMESTAMP_TIMER_FIXED_PERIOD 0
#define TIMESTAMP_TIMER_FREQ 120000000
#define TIMESTAMP_TIMER_IRQ 6
#define TIMESTAMP_TIMER_IRQ_INTERRUPT_CONTROLLER_ID 0
#define TIMESTAMP_TIMER_LOAD_VALUE 119999
#define TIMESTAMP_TIMER_MULT 0.001
#define TIMESTAMP_TIMER_NAME "/dev/timestamp_timer"
#define TIMESTAMP_TIMER_PERIOD 1
#define TIMESTAMP_TIMER_PERIOD_UNITS "ms"
#define TIMESTAMP_TIMER_RESET_OUTPUT 0
#define TIMESTAMP_TIMER_SNAPSHOT 1
#define TIMESTAMP_TIMER_SPAN 64
#define TIMESTAMP_TIMER_TICKS_PER_SEC 1000
#define TIMESTAMP_TIMER_TIMEOUT_PULSE_OUTPUT 0
#define TIMESTAMP_TIMER_TYPE "altera_avalon_timer"

#endif /* __SYSTEM_H_ */
