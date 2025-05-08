import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    dut.a.value = 0
    dut.b.value = 0
    await Timer(1, units='ns')
    assert dut.y.value == 0

    dut.a.value = 0
    dut.b.value = 1
    await Timer(1, units='ns')
    assert dut.y.value == 1

    dut.a.value = 1
    dut.b.value = 0
    await Timer(1, units='ns')
    assert dut.y.value == 1

    dut.a.value = 1
    dut.b.value = 1
    await Timer(1, units='ns')
    assert dut.y.value == 0
