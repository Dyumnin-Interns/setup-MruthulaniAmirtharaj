SIM ?= icarus
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/and_gate.v
TOPLEVEL = and_gate
MODULE = test_and_gate

# Enables waveform dump
WAVES = 1
ifeq ($(WAVES), 1)
    SIM_ARGS += -D DUMP_VCD
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
