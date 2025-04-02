import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    a_in=[0,0,1,1]
    b_in=[0,1,0,1]
    y_out=[0,1,1,0]
    for i in range(4):
        dut.a.value =a_in[i]
        dut.b.value=b_in[i]
        await Timer(1,"ns")
        assert dut.y.value == y_out[i]

