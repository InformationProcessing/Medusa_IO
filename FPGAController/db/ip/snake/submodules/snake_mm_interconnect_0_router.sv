// (C) 2001-2018 Intel Corporation. All rights reserved.
// Your use of Intel Corporation's design tools, logic functions and other 
// software and tools, and its AMPP partner logic functions, and any output 
// files from any of the foregoing (including device programming or simulation 
// files), and any associated documentation or information are expressly subject 
// to the terms and conditions of the Intel Program License Subscription 
// Agreement, Intel FPGA IP License Agreement, or other applicable 
// license agreement, including, without limitation, that your use is for the 
// sole purpose of programming logic devices manufactured by Intel and sold by 
// Intel or its authorized distributors.  Please refer to the applicable 
// agreement for further details.



// Your use of Altera Corporation's design tools, logic functions and other 
// software and tools, and its AMPP partner logic functions, and any output 
// files any of the foregoing (including device programming or simulation 
// files), and any associated documentation or information are expressly subject 
// to the terms and conditions of the Altera Program License Subscription 
// Agreement, Altera MegaCore Function License Agreement, or other applicable 
// license agreement, including, without limitation, that your use is for the 
// sole purpose of programming logic devices manufactured by Altera and sold by 
// Altera or its authorized distributors.  Please refer to the applicable 
// agreement for further details.


// $Id: //acds/rel/18.1std/ip/merlin/altera_merlin_router/altera_merlin_router.sv.terp#1 $
// $Revision: #1 $
// $Date: 2018/07/18 $
// $Author: psgswbuild $

// -------------------------------------------------------
// Merlin Router
//
// Asserts the appropriate one-hot encoded channel based on 
// either (a) the address or (b) the dest id. The DECODER_TYPE
// parameter controls this behaviour. 0 means address decoder,
// 1 means dest id decoder.
//
// In the case of (a), it also sets the destination id.
// -------------------------------------------------------

`timescale 1 ns / 1 ns

module snake_mm_interconnect_0_router_default_decode
  #(
     parameter DEFAULT_CHANNEL = 5,
               DEFAULT_WR_CHANNEL = -1,
               DEFAULT_RD_CHANNEL = -1,
               DEFAULT_DESTID = 21 
   )
  (output [91 - 87 : 0] default_destination_id,
   output [30-1 : 0] default_wr_channel,
   output [30-1 : 0] default_rd_channel,
   output [30-1 : 0] default_src_channel
  );

  assign default_destination_id = 
    DEFAULT_DESTID[91 - 87 : 0];

  generate
    if (DEFAULT_CHANNEL == -1) begin : no_default_channel_assignment
      assign default_src_channel = '0;
    end
    else begin : default_channel_assignment
      assign default_src_channel = 30'b1 << DEFAULT_CHANNEL;
    end
  endgenerate

  generate
    if (DEFAULT_RD_CHANNEL == -1) begin : no_default_rw_channel_assignment
      assign default_wr_channel = '0;
      assign default_rd_channel = '0;
    end
    else begin : default_rw_channel_assignment
      assign default_wr_channel = 30'b1 << DEFAULT_WR_CHANNEL;
      assign default_rd_channel = 30'b1 << DEFAULT_RD_CHANNEL;
    end
  endgenerate

endmodule


module snake_mm_interconnect_0_router
(
    // -------------------
    // Clock & Reset
    // -------------------
    input clk,
    input reset,

    // -------------------
    // Command Sink (Input)
    // -------------------
    input                       sink_valid,
    input  [105-1 : 0]    sink_data,
    input                       sink_startofpacket,
    input                       sink_endofpacket,
    output                      sink_ready,

    // -------------------
    // Command Source (Output)
    // -------------------
    output                          src_valid,
    output reg [105-1    : 0] src_data,
    output reg [30-1 : 0] src_channel,
    output                          src_startofpacket,
    output                          src_endofpacket,
    input                           src_ready
);

    // -------------------------------------------------------
    // Local parameters and variables
    // -------------------------------------------------------
    localparam PKT_ADDR_H = 60;
    localparam PKT_ADDR_L = 36;
    localparam PKT_DEST_ID_H = 91;
    localparam PKT_DEST_ID_L = 87;
    localparam PKT_PROTECTION_H = 95;
    localparam PKT_PROTECTION_L = 93;
    localparam ST_DATA_W = 105;
    localparam ST_CHANNEL_W = 30;
    localparam DECODER_TYPE = 0;

    localparam PKT_TRANS_WRITE = 63;
    localparam PKT_TRANS_READ  = 64;

    localparam PKT_ADDR_W = PKT_ADDR_H-PKT_ADDR_L + 1;
    localparam PKT_DEST_ID_W = PKT_DEST_ID_H-PKT_DEST_ID_L + 1;



    // -------------------------------------------------------
    // Figure out the number of bits to mask off for each slave span
    // during address decoding
    // -------------------------------------------------------
    localparam PAD0 = log2ceil(64'h1000000 - 64'h800000); 
    localparam PAD1 = log2ceil(64'h1001000 - 64'h1000800); 
    localparam PAD2 = log2ceil(64'h1001040 - 64'h1001000); 
    localparam PAD3 = log2ceil(64'h1001080 - 64'h1001040); 
    localparam PAD4 = log2ceil(64'h10010c0 - 64'h1001080); 
    localparam PAD5 = log2ceil(64'h10010e0 - 64'h10010c0); 
    localparam PAD6 = log2ceil(64'h1001100 - 64'h10010e0); 
    localparam PAD7 = log2ceil(64'h1001120 - 64'h1001100); 
    localparam PAD8 = log2ceil(64'h1001140 - 64'h1001120); 
    localparam PAD9 = log2ceil(64'h1001160 - 64'h1001140); 
    localparam PAD10 = log2ceil(64'h1001170 - 64'h1001160); 
    localparam PAD11 = log2ceil(64'h1001180 - 64'h1001170); 
    localparam PAD12 = log2ceil(64'h1001190 - 64'h1001180); 
    localparam PAD13 = log2ceil(64'h10011a0 - 64'h1001190); 
    localparam PAD14 = log2ceil(64'h10011b0 - 64'h10011a0); 
    localparam PAD15 = log2ceil(64'h10011c0 - 64'h10011b0); 
    localparam PAD16 = log2ceil(64'h10011d0 - 64'h10011c0); 
    localparam PAD17 = log2ceil(64'h10011e0 - 64'h10011d0); 
    localparam PAD18 = log2ceil(64'h10011f0 - 64'h10011e0); 
    localparam PAD19 = log2ceil(64'h1001200 - 64'h10011f0); 
    localparam PAD20 = log2ceil(64'h1001210 - 64'h1001200); 
    localparam PAD21 = log2ceil(64'h1001220 - 64'h1001210); 
    localparam PAD22 = log2ceil(64'h1001230 - 64'h1001220); 
    localparam PAD23 = log2ceil(64'h1001240 - 64'h1001230); 
    localparam PAD24 = log2ceil(64'h1001250 - 64'h1001240); 
    localparam PAD25 = log2ceil(64'h1001260 - 64'h1001250); 
    localparam PAD26 = log2ceil(64'h1001270 - 64'h1001260); 
    localparam PAD27 = log2ceil(64'h1001278 - 64'h1001270); 
    localparam PAD28 = log2ceil(64'h1001280 - 64'h1001278); 
    localparam PAD29 = log2ceil(64'h1001282 - 64'h1001280); 
    // -------------------------------------------------------
    // Work out which address bits are significant based on the
    // address range of the slaves. If the required width is too
    // large or too small, we use the address field width instead.
    // -------------------------------------------------------
    localparam ADDR_RANGE = 64'h1001282;
    localparam RANGE_ADDR_WIDTH = log2ceil(ADDR_RANGE);
    localparam OPTIMIZED_ADDR_H = (RANGE_ADDR_WIDTH > PKT_ADDR_W) ||
                                  (RANGE_ADDR_WIDTH == 0) ?
                                        PKT_ADDR_H :
                                        PKT_ADDR_L + RANGE_ADDR_WIDTH - 1;

    localparam RG = RANGE_ADDR_WIDTH-1;
    localparam REAL_ADDRESS_RANGE = OPTIMIZED_ADDR_H - PKT_ADDR_L;

      reg [PKT_ADDR_W-1 : 0] address;
      always @* begin
        address = {PKT_ADDR_W{1'b0}};
        address [REAL_ADDRESS_RANGE:0] = sink_data[OPTIMIZED_ADDR_H : PKT_ADDR_L];
      end   

    // -------------------------------------------------------
    // Pass almost everything through, untouched
    // -------------------------------------------------------
    assign sink_ready        = src_ready;
    assign src_valid         = sink_valid;
    assign src_startofpacket = sink_startofpacket;
    assign src_endofpacket   = sink_endofpacket;
    wire [PKT_DEST_ID_W-1:0] default_destid;
    wire [30-1 : 0] default_src_channel;




    // -------------------------------------------------------
    // Write and read transaction signals
    // -------------------------------------------------------
    wire read_transaction;
    assign read_transaction  = sink_data[PKT_TRANS_READ];


    snake_mm_interconnect_0_router_default_decode the_default_decode(
      .default_destination_id (default_destid),
      .default_wr_channel   (),
      .default_rd_channel   (),
      .default_src_channel  (default_src_channel)
    );

    always @* begin
        src_data    = sink_data;
        src_channel = default_src_channel;
        src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = default_destid;

        // --------------------------------------------------
        // Address Decoder
        // Sets the channel and destination ID based on the address
        // --------------------------------------------------

    // ( 0x800000 .. 0x1000000 )
    if ( {address[RG:PAD0],{PAD0{1'b0}}} == 25'h800000   ) begin
            src_channel = 30'b000000000000000000000000100000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 21;
    end

    // ( 0x1000800 .. 0x1001000 )
    if ( {address[RG:PAD1],{PAD1{1'b0}}} == 25'h1000800   ) begin
            src_channel = 30'b000000000000000000000000001000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 4;
    end

    // ( 0x1001000 .. 0x1001040 )
    if ( {address[RG:PAD2],{PAD2{1'b0}}} == 25'h1001000   ) begin
            src_channel = 30'b000000000010000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 29;
    end

    // ( 0x1001040 .. 0x1001080 )
    if ( {address[RG:PAD3],{PAD3{1'b0}}} == 25'h1001040   ) begin
            src_channel = 30'b000000000000010000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 26;
    end

    // ( 0x1001080 .. 0x10010c0 )
    if ( {address[RG:PAD4],{PAD4{1'b0}}} == 25'h1001080   ) begin
            src_channel = 30'b000000000000001000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 27;
    end

    // ( 0x10010c0 .. 0x10010e0 )
    if ( {address[RG:PAD5],{PAD5{1'b0}}} == 25'h10010c0   ) begin
            src_channel = 30'b000000010000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 0;
    end

    // ( 0x10010e0 .. 0x1001100 )
    if ( {address[RG:PAD6],{PAD6{1'b0}}} == 25'h10010e0   ) begin
            src_channel = 30'b000000001000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 18;
    end

    // ( 0x1001100 .. 0x1001120 )
    if ( {address[RG:PAD7],{PAD7{1'b0}}} == 25'h1001100   ) begin
            src_channel = 30'b000000000100000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 24;
    end

    // ( 0x1001120 .. 0x1001140 )
    if ( {address[RG:PAD8],{PAD8{1'b0}}} == 25'h1001120   ) begin
            src_channel = 30'b000000000001000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 28;
    end

    // ( 0x1001140 .. 0x1001160 )
    if ( {address[RG:PAD9],{PAD9{1'b0}}} == 25'h1001140   ) begin
            src_channel = 30'b000000000000100000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 25;
    end

    // ( 0x1001160 .. 0x1001170 )
    if ( {address[RG:PAD10],{PAD10{1'b0}}} == 25'h1001160  && read_transaction  ) begin
            src_channel = 30'b100000000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 8;
    end

    // ( 0x1001170 .. 0x1001180 )
    if ( {address[RG:PAD11],{PAD11{1'b0}}} == 25'h1001170   ) begin
            src_channel = 30'b010000000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 11;
    end

    // ( 0x1001180 .. 0x1001190 )
    if ( {address[RG:PAD12],{PAD12{1'b0}}} == 25'h1001180   ) begin
            src_channel = 30'b001000000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 10;
    end

    // ( 0x1001190 .. 0x10011a0 )
    if ( {address[RG:PAD13],{PAD13{1'b0}}} == 25'h1001190  && read_transaction  ) begin
            src_channel = 30'b000100000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 7;
    end

    // ( 0x10011a0 .. 0x10011b0 )
    if ( {address[RG:PAD14],{PAD14{1'b0}}} == 25'h10011a0   ) begin
            src_channel = 30'b000010000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 5;
    end

    // ( 0x10011b0 .. 0x10011c0 )
    if ( {address[RG:PAD15],{PAD15{1'b0}}} == 25'h10011b0  && read_transaction  ) begin
            src_channel = 30'b000001000000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 6;
    end

    // ( 0x10011c0 .. 0x10011d0 )
    if ( {address[RG:PAD16],{PAD16{1'b0}}} == 25'h10011c0   ) begin
            src_channel = 30'b000000100000000000000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 9;
    end

    // ( 0x10011d0 .. 0x10011e0 )
    if ( {address[RG:PAD17],{PAD17{1'b0}}} == 25'h10011d0  && read_transaction  ) begin
            src_channel = 30'b000000000000000100000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 3;
    end

    // ( 0x10011e0 .. 0x10011f0 )
    if ( {address[RG:PAD18],{PAD18{1'b0}}} == 25'h10011e0  && read_transaction  ) begin
            src_channel = 30'b000000000000000010000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 22;
    end

    // ( 0x10011f0 .. 0x1001200 )
    if ( {address[RG:PAD19],{PAD19{1'b0}}} == 25'h10011f0   ) begin
            src_channel = 30'b000000000000000001000000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 12;
    end

    // ( 0x1001200 .. 0x1001210 )
    if ( {address[RG:PAD20],{PAD20{1'b0}}} == 25'h1001200   ) begin
            src_channel = 30'b000000000000000000100000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 13;
    end

    // ( 0x1001210 .. 0x1001220 )
    if ( {address[RG:PAD21],{PAD21{1'b0}}} == 25'h1001210   ) begin
            src_channel = 30'b000000000000000000010000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 14;
    end

    // ( 0x1001220 .. 0x1001230 )
    if ( {address[RG:PAD22],{PAD22{1'b0}}} == 25'h1001220   ) begin
            src_channel = 30'b000000000000000000001000000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 15;
    end

    // ( 0x1001230 .. 0x1001240 )
    if ( {address[RG:PAD23],{PAD23{1'b0}}} == 25'h1001230   ) begin
            src_channel = 30'b000000000000000000000100000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 16;
    end

    // ( 0x1001240 .. 0x1001250 )
    if ( {address[RG:PAD24],{PAD24{1'b0}}} == 25'h1001240   ) begin
            src_channel = 30'b000000000000000000000010000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 17;
    end

    // ( 0x1001250 .. 0x1001260 )
    if ( {address[RG:PAD25],{PAD25{1'b0}}} == 25'h1001250   ) begin
            src_channel = 30'b000000000000000000000001000000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 20;
    end

    // ( 0x1001260 .. 0x1001270 )
    if ( {address[RG:PAD26],{PAD26{1'b0}}} == 25'h1001260   ) begin
            src_channel = 30'b000000000000000000000000010000;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 2;
    end

    // ( 0x1001270 .. 0x1001278 )
    if ( {address[RG:PAD27],{PAD27{1'b0}}} == 25'h1001270  && read_transaction  ) begin
            src_channel = 30'b000000000000000000000000000100;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 23;
    end

    // ( 0x1001278 .. 0x1001280 )
    if ( {address[RG:PAD28],{PAD28{1'b0}}} == 25'h1001278   ) begin
            src_channel = 30'b000000000000000000000000000010;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 19;
    end

    // ( 0x1001280 .. 0x1001282 )
    if ( {address[RG:PAD29],{PAD29{1'b0}}} == 25'h1001280   ) begin
            src_channel = 30'b000000000000000000000000000001;
            src_data[PKT_DEST_ID_H:PKT_DEST_ID_L] = 1;
    end

end


    // --------------------------------------------------
    // Ceil(log2()) function
    // --------------------------------------------------
    function integer log2ceil;
        input reg[65:0] val;
        reg [65:0] i;

        begin
            i = 1;
            log2ceil = 0;

            while (i < val) begin
                log2ceil = log2ceil + 1;
                i = i << 1;
            end
        end
    endfunction

endmodule


