// It is a part of brainfuck processor. Only address change and output logic.

module data_memory
  ( input  wire       clk

  , input  wire       signal_latch_data_address
  , input  wire       signal_data_address_sel
  , input  wire       signal_latch_acc

  , output wire  [7:0] acc
  );

reg [3:0] data_address;
reg [7:0] mem[15:0];
wire [7:0] mem_out;
reg [7:0] acc_internal;

// not a part of hardware
integer i;
initial begin
  data_address = 0;
  for (i = 0; i < 8; i = i+1)
    mem[i] = i[7:0];
end

// logic
always @(posedge clk)
  if ( signal_latch_data_address )
    data_address <= signal_data_address_sel
                    ? data_address + 1
                    : data_address - 1;

assign mem_out = mem[data_address];

always @(posedge clk)
  if ( signal_latch_acc )
    acc_internal <= mem_out;

assign acc = acc_internal;

endmodule
