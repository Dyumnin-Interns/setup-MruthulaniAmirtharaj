import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def and_test(dut):
    # Test all input combinations
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for a_val, b_val in inputs:
        dut.a.value = a_val
        dut.b.value = b_val
        await Timer(1, units="ns")
        expected = a_val & b_val
        assert dut.y.value == expected, f"Failed for a={a_val}, b={b_val}"
