module data_memory_tb();

reg clk;
reg latch_data_address, data_address_sel;
reg latch_acc;

wire [7:0] acc;

data_memory u
  ( .clk( clk )

  , .signal_latch_data_address( latch_data_address )
  , .signal_data_address_sel( data_address_sel )
  , .signal_latch_acc( latch_acc )

  , .acc( acc )
  );

// dump wave diagram into VCD file
initial begin
  $dumpfile("data_memory_tb.vcd");
  $dumpvars(0, data_memory_tb);
  // execute clock signal
  clk <= 1;
  forever #1 clk <= !clk;
end

initial
  begin
    // signal will estabilish after each clock signal
    latch_data_address <= 0; data_address_sel <= 0; latch_acc <= 0; @(posedge clk);
    repeat(2) @(posedge clk);

    // addr to 3
    latch_data_address <= 1; data_address_sel <= 1; latch_acc <= 0; @(posedge clk);
    latch_data_address <= 1; data_address_sel <= 1; latch_acc <= 0; @(posedge clk);
    latch_data_address <= 1; data_address_sel <= 1; latch_acc <= 0; @(posedge clk);

    // latch acc
    latch_data_address <= 0; data_address_sel <= 0; latch_acc <= 1; @(posedge clk);

    // addr to 2
    latch_data_address <= 1; data_address_sel <= 0; latch_acc <= 0; @(posedge clk);

    // addr to 1 and latch acc at same time
    latch_data_address <= 1; data_address_sel <= 0; latch_acc <= 1; @(posedge clk);

    latch_data_address <= 0; data_address_sel <= 0; latch_acc <= 0; @(posedge clk);
    repeat(2) @(posedge clk);

    $finish;
  end

endmodule
