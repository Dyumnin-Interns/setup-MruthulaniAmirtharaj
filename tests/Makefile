SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/xor_gate.v
VERILOG_SOURCES += $(PWD)/tests/wrappers/xor_gate.v
TOPLEVEL = xor_test
MODULE = xor_test
include $(shell cocotb-config --makefiles)/Makefile.sim6
