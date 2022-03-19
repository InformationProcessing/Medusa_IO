Debug = True

print("""module hard(
    input logic reset,
    input logic clk_coeff,
    input logic clk_sample,

    input logic signed [31:0] in,
    output logic signed  [31:0] out
);

logic signed [31:0] coefficients [63:0];
logic signed [31:0] samples [63:0];

//Addition layers
logic signed [31:0] layer1 [63:0];
logic signed [31:0] layer2 [31:0];
logic signed[31:0] layer3 [15:0];
logic signed [31:0] layer4 [7:0];
logic signed [31:0] layer5 [3:0];
logic signed [31:0] layer6 [1:0];


always @(posedge clk_coeff) begin
    if (reset) begin""")

for i in range(64):
    print(f"\t\tcoefficients[{i}] <= 0;")

print( """end else begin
    \tcoefficients[63] <= in;""")

for i in range(63):
    print(f"\t\tcoefficients[{i}] <= coefficients[{i+1}];")

print("""end
end

always @(posedge clk_sample) begin \n
    if (reset) begin""")

for i in range(64):
    print(f"\t\tsamples[{i}] <= 0;")

print( """end else begin 
samples[63] <= in<<<11;""")

for i in range(63):
    print(f"\tsamples[{i}] <= samples[{i+1}];")
print("")
print("""\t end \n end

always @(*) begin""")
print("")
for i in range(64):
    print(f"\tlayer1[{i}] = (coefficients[{i}] * samples[{i}])>>>11;")
print("")
for i in range(32):
    print(f"\tlayer2[{i}] = layer1[{2*i}] + layer1[{2*i+1}];")
print("")
for i in range(16):
    print(f"\tlayer3[{i}] = layer2[{2*i}] + layer2[{2*i+1}];")
print("")
for i in range(8):
    print(f"\tlayer4[{i}] = layer3[{2*i}] + layer3[{2*i+1}];")
print("")
for i in range(4):
    print(f"\tlayer5[{i}] = layer4[{2*i}] + layer4[{2*i+1}];")
print("")
for i in range(2):
    print(f"\tlayer6[{i}] = layer5[{2*i}] + layer5[{2*i+1}];")
print("")

print("""
    out = (layer6[0] + layer6[1]) >>> 11;
end


endmodule""")



