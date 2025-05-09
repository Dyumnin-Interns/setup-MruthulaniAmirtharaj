module dut(
    input wire a,
    input wire b,
    output wire y
);

assign y = a^b;
initial begin
    $dumpfile("xor.vcd"); 
    $dumpvars(0, xor); 
endmodule
