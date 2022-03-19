module hard_tb();

logic reset;
logic clk_coeff;
logic clk_sample;

logic [31:0] in;
logic [31:0] out;


//declarations
real coeffs [63:0];
int samples [63:0];
int length = 64;
real reference;


initial begin
    $display("Got here");
    $dumpfile("waves.vcd");
    $dumpvars(0, hard_tb);
end

initial begin
    $display("Got here");

    for (int i = 0; i< 100; i = i + 1) begin
    //Reset sequence
    clk_coeff = 0;
    clk_sample = 0;
    #1;
    reset = 1;
    #1;
    clk_coeff = 1;
    clk_sample = 1;
    #1;
    reset = 0;
    clk_coeff = 0;
    clk_sample = 0;

    //Load coefficients
    for (int i = 0; i< length; i = i + 1) begin
        clk_coeff = 0;
        //Random coefficient
        coeffs[i] = real'($random%511)/255;
        //coeffs[i] = i;
        in = int'(coeffs[i] *(1<<11));
        #1;
        clk_coeff = 1;
        #1;
        $display("coefifcients[%d] = %d / %7.5f", i, int'(in), coeffs[i]);
    end
    clk_coeff = 0;

    //Populate random data array
    for (int i = 0; i< length; i = i + 1) begin
        samples[i] = $random%255;
         //samples[i] = 1;
    end

    //Generate reference value
    reference = 0;
    for(int i = 0; i< length; i = i + 1) begin
        reference = reference + samples[i]*coeffs[i];
    end

    //Load samples
    for (int i = 0; i< length; i = i + 1) begin
        clk_sample = 0;
        in = samples[i];
         $display("data[%d] = %d", i, samples[i]);
        #1;
        clk_sample = 1;
        #1;
    end
    clk_sample = 0;


    $display("actual = %d, reference %d", int'(out), int'(reference));
    $display("%d", (int'(out) < 0 ));
    assert ((int'(out) <= int'(reference + 2)) && (int'(out) >= int'(reference - 2))) begin
            $display("Correct answer");
        end else begin
            $fatal;
        end

    end
    $display("passed all tests");
    $finish;
end

hard dut(.reset(reset), .clk_coeff(clk_coeff), .clk_sample(clk_sample), .in(in), .out(out));
endmodule