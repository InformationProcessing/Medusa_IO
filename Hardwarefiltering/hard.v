module hard(
    input logic reset,
    input logic clk_coeff,
    input logic clk_sample,

    input logic signed [31:0] in,
    output logic signed  [31:0] out
);

logic signed [31:0] coefficients [64:0];
logic signed [31:0] samples [63:0];

//Addition layers
logic signed [31:0] layer1 [63:0];
logic signed [31:0] layer2 [31:0];
logic signed[31:0] layer3 [15:0];
logic signed [31:0] layer4 [7:0];
logic signed [31:0] layer5 [3:0];
logic signed [31:0] layer6 [1:0];
logic signed [31:0] layer7 ;
logic signed [31:0] scaled;

logic [31:0] scalecoeff, unscaledout;

logic[31:0] i;

always @(posedge clk_coeff) begin
    if (reset) begin
        for (i = 0; i <65; i = i + 1) begin
            coefficients[i] <= 0;
        end

end else begin
    	coefficients[64] <= in;
		for (i = 0; i <64; i = i + 1) begin
            coefficients[i] <= coefficients[i+1];
        end
end
end

always @(posedge clk_sample) begin

    if (reset) begin
		for (i = 0; i <64; i = i + 1) begin
            samples[i] <= 0;
        end
end else begin
    samples[63] <= in<<<11;
	for (i = 0; i <63; i = i + 1) begin
        samples[i] <= samples[i+1];
    end

	 end
 end

always @(*) begin

    for (i = 0; i <64; i = i + 1) begin
        layer1[i] = (coefficients[i] * samples[i])>>>11;
    end


    for (i = 0; i <32; i = i + 1) begin
        layer2[i] = layer1[2*i] + layer1[2*i+1];
    end

    for (i = 0; i <16; i = i + 1) begin
        layer3[i] = layer2[2*i] + layer2[2*i +1];
    end

	for (i = 0; i <8; i = i + 1) begin
        layer4[i] = layer3[2*i] + layer3[2*i +1];
    end

    for (i = 0; i <4; i = i + 1) begin
        layer5[i] = layer4[2*i] + layer4[2*i +1];
    end

	layer6[0] = layer5[0] + layer5[1];
	layer6[1] = layer5[2] + layer5[3];

    layer7 = layer6[0] + layer6[1];

    out = (layer7*coefficients[64]) >>> 22;
end


endmodule