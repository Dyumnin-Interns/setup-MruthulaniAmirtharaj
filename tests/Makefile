SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/tests/wrappers/xor_gate.v
TOPLEVEL = xor_test
MODULE = dut_test
include $(shell cocotb-config --makefiles)/Makefile.sim6
