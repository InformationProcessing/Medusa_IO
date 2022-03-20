#!/bin/bash

iverilog -o out.o hard.v hard_tb.v -g 2012 &&
./out.o

gtkwave waves.vcd