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

logic [31:0] sample0, sample1, sample2, sample3;
logic [31:0] coeff0, coeff1, coeff2, coeff3;
logic [31:0] layer11, layer12, layer13, layer14, layer21, layer22, layer31, scalecoeff, unscaledout;


always @(posedge clk_coeff) begin
    if (reset) begin
		coefficients[0] <= 0;
		coefficients[1] <= 0;
		coefficients[2] <= 0;
		coefficients[3] <= 0;
		coefficients[4] <= 0;
		coefficients[5] <= 0;
		coefficients[6] <= 0;
		coefficients[7] <= 0;
		coefficients[8] <= 0;
		coefficients[9] <= 0;
		coefficients[10] <= 0;
		coefficients[11] <= 0;
		coefficients[12] <= 0;
		coefficients[13] <= 0;
		coefficients[14] <= 0;
		coefficients[15] <= 0;
		coefficients[16] <= 0;
		coefficients[17] <= 0;
		coefficients[18] <= 0;
		coefficients[19] <= 0;
		coefficients[20] <= 0;
		coefficients[21] <= 0;
		coefficients[22] <= 0;
		coefficients[23] <= 0;
		coefficients[24] <= 0;
		coefficients[25] <= 0;
		coefficients[26] <= 0;
		coefficients[27] <= 0;
		coefficients[28] <= 0;
		coefficients[29] <= 0;
		coefficients[30] <= 0;
		coefficients[31] <= 0;
		coefficients[32] <= 0;
		coefficients[33] <= 0;
		coefficients[34] <= 0;
		coefficients[35] <= 0;
		coefficients[36] <= 0;
		coefficients[37] <= 0;
		coefficients[38] <= 0;
		coefficients[39] <= 0;
		coefficients[40] <= 0;
		coefficients[41] <= 0;
		coefficients[42] <= 0;
		coefficients[43] <= 0;
		coefficients[44] <= 0;
		coefficients[45] <= 0;
		coefficients[46] <= 0;
		coefficients[47] <= 0;
		coefficients[48] <= 0;
		coefficients[49] <= 0;
		coefficients[50] <= 0;
		coefficients[51] <= 0;
		coefficients[52] <= 0;
		coefficients[53] <= 0;
		coefficients[54] <= 0;
		coefficients[55] <= 0;
		coefficients[56] <= 0;
		coefficients[57] <= 0;
		coefficients[58] <= 0;
		coefficients[59] <= 0;
		coefficients[60] <= 0;
		coefficients[61] <= 0;
		coefficients[62] <= 0;
		coefficients[63] <= 0;
		coefficients[64] <= 0;
end else begin
    	coefficients[64] <= in;
		coefficients[0] <= coefficients[1];
		coefficients[1] <= coefficients[2];
		coefficients[2] <= coefficients[3];
		coefficients[3] <= coefficients[4];
		coefficients[4] <= coefficients[5];
		coefficients[5] <= coefficients[6];
		coefficients[6] <= coefficients[7];
		coefficients[7] <= coefficients[8];
		coefficients[8] <= coefficients[9];
		coefficients[9] <= coefficients[10];
		coefficients[10] <= coefficients[11];
		coefficients[11] <= coefficients[12];
		coefficients[12] <= coefficients[13];
		coefficients[13] <= coefficients[14];
		coefficients[14] <= coefficients[15];
		coefficients[15] <= coefficients[16];
		coefficients[16] <= coefficients[17];
		coefficients[17] <= coefficients[18];
		coefficients[18] <= coefficients[19];
		coefficients[19] <= coefficients[20];
		coefficients[20] <= coefficients[21];
		coefficients[21] <= coefficients[22];
		coefficients[22] <= coefficients[23];
		coefficients[23] <= coefficients[24];
		coefficients[24] <= coefficients[25];
		coefficients[25] <= coefficients[26];
		coefficients[26] <= coefficients[27];
		coefficients[27] <= coefficients[28];
		coefficients[28] <= coefficients[29];
		coefficients[29] <= coefficients[30];
		coefficients[30] <= coefficients[31];
		coefficients[31] <= coefficients[32];
		coefficients[32] <= coefficients[33];
		coefficients[33] <= coefficients[34];
		coefficients[34] <= coefficients[35];
		coefficients[35] <= coefficients[36];
		coefficients[36] <= coefficients[37];
		coefficients[37] <= coefficients[38];
		coefficients[38] <= coefficients[39];
		coefficients[39] <= coefficients[40];
		coefficients[40] <= coefficients[41];
		coefficients[41] <= coefficients[42];
		coefficients[42] <= coefficients[43];
		coefficients[43] <= coefficients[44];
		coefficients[44] <= coefficients[45];
		coefficients[45] <= coefficients[46];
		coefficients[46] <= coefficients[47];
		coefficients[47] <= coefficients[48];
		coefficients[48] <= coefficients[49];
		coefficients[49] <= coefficients[50];
		coefficients[50] <= coefficients[51];
		coefficients[51] <= coefficients[52];
		coefficients[52] <= coefficients[53];
		coefficients[53] <= coefficients[54];
		coefficients[54] <= coefficients[55];
		coefficients[55] <= coefficients[56];
		coefficients[56] <= coefficients[57];
		coefficients[57] <= coefficients[58];
		coefficients[58] <= coefficients[59];
		coefficients[59] <= coefficients[60];
		coefficients[60] <= coefficients[61];
		coefficients[61] <= coefficients[62];
		coefficients[62] <= coefficients[63];
		coefficients[63] <= coefficients[64];
end
end

always @(posedge clk_sample) begin

    if (reset) begin
		samples[0] <= 0;
		samples[1] <= 0;
		samples[2] <= 0;
		samples[3] <= 0;
		samples[4] <= 0;
		samples[5] <= 0;
		samples[6] <= 0;
		samples[7] <= 0;
		samples[8] <= 0;
		samples[9] <= 0;
		samples[10] <= 0;
		samples[11] <= 0;
		samples[12] <= 0;
		samples[13] <= 0;
		samples[14] <= 0;
		samples[15] <= 0;
		samples[16] <= 0;
		samples[17] <= 0;
		samples[18] <= 0;
		samples[19] <= 0;
		samples[20] <= 0;
		samples[21] <= 0;
		samples[22] <= 0;
		samples[23] <= 0;
		samples[24] <= 0;
		samples[25] <= 0;
		samples[26] <= 0;
		samples[27] <= 0;
		samples[28] <= 0;
		samples[29] <= 0;
		samples[30] <= 0;
		samples[31] <= 0;
		samples[32] <= 0;
		samples[33] <= 0;
		samples[34] <= 0;
		samples[35] <= 0;
		samples[36] <= 0;
		samples[37] <= 0;
		samples[38] <= 0;
		samples[39] <= 0;
		samples[40] <= 0;
		samples[41] <= 0;
		samples[42] <= 0;
		samples[43] <= 0;
		samples[44] <= 0;
		samples[45] <= 0;
		samples[46] <= 0;
		samples[47] <= 0;
		samples[48] <= 0;
		samples[49] <= 0;
		samples[50] <= 0;
		samples[51] <= 0;
		samples[52] <= 0;
		samples[53] <= 0;
		samples[54] <= 0;
		samples[55] <= 0;
		samples[56] <= 0;
		samples[57] <= 0;
		samples[58] <= 0;
		samples[59] <= 0;
		samples[60] <= 0;
		samples[61] <= 0;
		samples[62] <= 0;
		samples[63] <= 0;
end else begin
    samples[63] <= in<<<11;
	samples[0] <= samples[1];
	samples[1] <= samples[2];
	samples[2] <= samples[3];
	samples[3] <= samples[4];
	samples[4] <= samples[5];
	samples[5] <= samples[6];
	samples[6] <= samples[7];
	samples[7] <= samples[8];
	samples[8] <= samples[9];
	samples[9] <= samples[10];
	samples[10] <= samples[11];
	samples[11] <= samples[12];
	samples[12] <= samples[13];
	samples[13] <= samples[14];
	samples[14] <= samples[15];
	samples[15] <= samples[16];
	samples[16] <= samples[17];
	samples[17] <= samples[18];
	samples[18] <= samples[19];
	samples[19] <= samples[20];
	samples[20] <= samples[21];
	samples[21] <= samples[22];
	samples[22] <= samples[23];
	samples[23] <= samples[24];
	samples[24] <= samples[25];
	samples[25] <= samples[26];
	samples[26] <= samples[27];
	samples[27] <= samples[28];
	samples[28] <= samples[29];
	samples[29] <= samples[30];
	samples[30] <= samples[31];
	samples[31] <= samples[32];
	samples[32] <= samples[33];
	samples[33] <= samples[34];
	samples[34] <= samples[35];
	samples[35] <= samples[36];
	samples[36] <= samples[37];
	samples[37] <= samples[38];
	samples[38] <= samples[39];
	samples[39] <= samples[40];
	samples[40] <= samples[41];
	samples[41] <= samples[42];
	samples[42] <= samples[43];
	samples[43] <= samples[44];
	samples[44] <= samples[45];
	samples[45] <= samples[46];
	samples[46] <= samples[47];
	samples[47] <= samples[48];
	samples[48] <= samples[49];
	samples[49] <= samples[50];
	samples[50] <= samples[51];
	samples[51] <= samples[52];
	samples[52] <= samples[53];
	samples[53] <= samples[54];
	samples[54] <= samples[55];
	samples[55] <= samples[56];
	samples[56] <= samples[57];
	samples[57] <= samples[58];
	samples[58] <= samples[59];
	samples[59] <= samples[60];
	samples[60] <= samples[61];
	samples[61] <= samples[62];
	samples[62] <= samples[63];

	 end
 end

always @(*) begin

	layer1[0] = (coefficients[0] * samples[0])>>>11;
	layer1[1] = (coefficients[1] * samples[1])>>>11;
	layer1[2] = (coefficients[2] * samples[2])>>>11;
	layer1[3] = (coefficients[3] * samples[3])>>>11;
	layer1[4] = (coefficients[4] * samples[4])>>>11;
	layer1[5] = (coefficients[5] * samples[5])>>>11;
	layer1[6] = (coefficients[6] * samples[6])>>>11;
	layer1[7] = (coefficients[7] * samples[7])>>>11;
	layer1[8] = (coefficients[8] * samples[8])>>>11;
	layer1[9] = (coefficients[9] * samples[9])>>>11;
	layer1[10] = (coefficients[10] * samples[10])>>>11;
	layer1[11] = (coefficients[11] * samples[11])>>>11;
	layer1[12] = (coefficients[12] * samples[12])>>>11;
	layer1[13] = (coefficients[13] * samples[13])>>>11;
	layer1[14] = (coefficients[14] * samples[14])>>>11;
	layer1[15] = (coefficients[15] * samples[15])>>>11;
	layer1[16] = (coefficients[16] * samples[16])>>>11;
	layer1[17] = (coefficients[17] * samples[17])>>>11;
	layer1[18] = (coefficients[18] * samples[18])>>>11;
	layer1[19] = (coefficients[19] * samples[19])>>>11;
	layer1[20] = (coefficients[20] * samples[20])>>>11;
	layer1[21] = (coefficients[21] * samples[21])>>>11;
	layer1[22] = (coefficients[22] * samples[22])>>>11;
	layer1[23] = (coefficients[23] * samples[23])>>>11;
	layer1[24] = (coefficients[24] * samples[24])>>>11;
	layer1[25] = (coefficients[25] * samples[25])>>>11;
	layer1[26] = (coefficients[26] * samples[26])>>>11;
	layer1[27] = (coefficients[27] * samples[27])>>>11;
	layer1[28] = (coefficients[28] * samples[28])>>>11;
	layer1[29] = (coefficients[29] * samples[29])>>>11;
	layer1[30] = (coefficients[30] * samples[30])>>>11;
	layer1[31] = (coefficients[31] * samples[31])>>>11;
	layer1[32] = (coefficients[32] * samples[32])>>>11;
	layer1[33] = (coefficients[33] * samples[33])>>>11;
	layer1[34] = (coefficients[34] * samples[34])>>>11;
	layer1[35] = (coefficients[35] * samples[35])>>>11;
	layer1[36] = (coefficients[36] * samples[36])>>>11;
	layer1[37] = (coefficients[37] * samples[37])>>>11;
	layer1[38] = (coefficients[38] * samples[38])>>>11;
	layer1[39] = (coefficients[39] * samples[39])>>>11;
	layer1[40] = (coefficients[40] * samples[40])>>>11;
	layer1[41] = (coefficients[41] * samples[41])>>>11;
	layer1[42] = (coefficients[42] * samples[42])>>>11;
	layer1[43] = (coefficients[43] * samples[43])>>>11;
	layer1[44] = (coefficients[44] * samples[44])>>>11;
	layer1[45] = (coefficients[45] * samples[45])>>>11;
	layer1[46] = (coefficients[46] * samples[46])>>>11;
	layer1[47] = (coefficients[47] * samples[47])>>>11;
	layer1[48] = (coefficients[48] * samples[48])>>>11;
	layer1[49] = (coefficients[49] * samples[49])>>>11;
	layer1[50] = (coefficients[50] * samples[50])>>>11;
	layer1[51] = (coefficients[51] * samples[51])>>>11;
	layer1[52] = (coefficients[52] * samples[52])>>>11;
	layer1[53] = (coefficients[53] * samples[53])>>>11;
	layer1[54] = (coefficients[54] * samples[54])>>>11;
	layer1[55] = (coefficients[55] * samples[55])>>>11;
	layer1[56] = (coefficients[56] * samples[56])>>>11;
	layer1[57] = (coefficients[57] * samples[57])>>>11;
	layer1[58] = (coefficients[58] * samples[58])>>>11;
	layer1[59] = (coefficients[59] * samples[59])>>>11;
	layer1[60] = (coefficients[60] * samples[60])>>>11;
	layer1[61] = (coefficients[61] * samples[61])>>>11;
	layer1[62] = (coefficients[62] * samples[62])>>>11;
	layer1[63] = (coefficients[63] * samples[63])>>>11;

	layer14 = layer1[63]>>11;
	layer13 = layer1[62]>>11;
	layer12 = layer1[61]>>11;
	layer11 = layer1[60]>>11;




	layer2[0] = layer1[0] + layer1[1];
	layer2[1] = layer1[2] + layer1[3];
	layer2[2] = layer1[4] + layer1[5];
	layer2[3] = layer1[6] + layer1[7];
	layer2[4] = layer1[8] + layer1[9];
	layer2[5] = layer1[10] + layer1[11];
	layer2[6] = layer1[12] + layer1[13];
	layer2[7] = layer1[14] + layer1[15];
	layer2[8] = layer1[16] + layer1[17];
	layer2[9] = layer1[18] + layer1[19];
	layer2[10] = layer1[20] + layer1[21];
	layer2[11] = layer1[22] + layer1[23];
	layer2[12] = layer1[24] + layer1[25];
	layer2[13] = layer1[26] + layer1[27];
	layer2[14] = layer1[28] + layer1[29];
	layer2[15] = layer1[30] + layer1[31];
	layer2[16] = layer1[32] + layer1[33];
	layer2[17] = layer1[34] + layer1[35];
	layer2[18] = layer1[36] + layer1[37];
	layer2[19] = layer1[38] + layer1[39];
	layer2[20] = layer1[40] + layer1[41];
	layer2[21] = layer1[42] + layer1[43];
	layer2[22] = layer1[44] + layer1[45];
	layer2[23] = layer1[46] + layer1[47];
	layer2[24] = layer1[48] + layer1[49];
	layer2[25] = layer1[50] + layer1[51];
	layer2[26] = layer1[52] + layer1[53];
	layer2[27] = layer1[54] + layer1[55];
	layer2[28] = layer1[56] + layer1[57];
	layer2[29] = layer1[58] + layer1[59];
	layer2[30] = layer1[60] + layer1[61];
	layer2[31] = layer1[62] + layer1[63];

    layer22 = layer2[31]>>11;
    layer21 = layer2[30]>>11;


	layer3[0] = layer2[0] + layer2[1];
	layer3[1] = layer2[2] + layer2[3];
	layer3[2] = layer2[4] + layer2[5];
	layer3[3] = layer2[6] + layer2[7];
	layer3[4] = layer2[8] + layer2[9];
	layer3[5] = layer2[10] + layer2[11];
	layer3[6] = layer2[12] + layer2[13];
	layer3[7] = layer2[14] + layer2[15];
	layer3[8] = layer2[16] + layer2[17];
	layer3[9] = layer2[18] + layer2[19];
	layer3[10] = layer2[20] + layer2[21];
	layer3[11] = layer2[22] + layer2[23];
	layer3[12] = layer2[24] + layer2[25];
	layer3[13] = layer2[26] + layer2[27];
	layer3[14] = layer2[28] + layer2[29];
	layer3[15] = layer2[30] + layer2[31];

	layer31 = layer3[15]>>11;

	layer4[0] = layer3[0] + layer3[1];
	layer4[1] = layer3[2] + layer3[3];
	layer4[2] = layer3[4] + layer3[5];
	layer4[3] = layer3[6] + layer3[7];
	layer4[4] = layer3[8] + layer3[9];
	layer4[5] = layer3[10] + layer3[11];
	layer4[6] = layer3[12] + layer3[13];
	layer4[7] = layer3[14] + layer3[15];

	layer5[0] = layer4[0] + layer4[1];
	layer5[1] = layer4[2] + layer4[3];
	layer5[2] = layer4[4] + layer4[5];
	layer5[3] = layer4[6] + layer4[7];

	layer6[0] = layer5[0] + layer5[1];
	layer6[1] = layer5[2] + layer5[3];

    scalecoeff = coefficients[64];

    layer7 = layer6[0] + layer6[1];
    unscaledout = layer7>>>11;
    out = (layer7*coefficients[64]) >>> 22;

    coeff0 = coefficients[60];
    coeff1 = coefficients[61];
    coeff2 = coefficients[62];
    coeff3 = coefficients[63];

    sample0 = samples[60];
    sample1 = samples[61];
    sample2 = samples[62];
    sample3 = samples[63];


end


endmodule