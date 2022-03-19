	component snake is
		port (
			accelerometer_spi_external_interface_I2C_SDAT      : inout std_logic                     := 'X';             -- I2C_SDAT
			accelerometer_spi_external_interface_I2C_SCLK      : out   std_logic;                                        -- I2C_SCLK
			accelerometer_spi_external_interface_G_SENSOR_CS_N : out   std_logic;                                        -- G_SENSOR_CS_N
			accelerometer_spi_external_interface_G_SENSOR_INT  : in    std_logic                     := 'X';             -- G_SENSOR_INT
			altpll_areset_conduit_export                       : in    std_logic                     := 'X';             -- export
			altpll_locked_conduit_export                       : out   std_logic;                                        -- export
			button_external_connection_export                  : in    std_logic_vector(1 downto 0)  := (others => 'X'); -- export
			clk_clk                                            : in    std_logic                     := 'X';             -- clk
			clk_sdram_clk                                      : out   std_logic;                                        -- clk
			hex0_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			hex1_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			hex2_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			hex3_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			hex4_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			hex5_external_connection_export                    : out   std_logic_vector(7 downto 0);                     -- export
			led_external_connection_export                     : out   std_logic_vector(9 downto 0);                     -- export
			reset_reset_n                                      : in    std_logic                     := 'X';             -- reset_n
			sdram_wire_addr                                    : out   std_logic_vector(11 downto 0);                    -- addr
			sdram_wire_ba                                      : out   std_logic_vector(1 downto 0);                     -- ba
			sdram_wire_cas_n                                   : out   std_logic;                                        -- cas_n
			sdram_wire_cke                                     : out   std_logic;                                        -- cke
			sdram_wire_cs_n                                    : out   std_logic;                                        -- cs_n
			sdram_wire_dq                                      : inout std_logic_vector(15 downto 0) := (others => 'X'); -- dq
			sdram_wire_dqm                                     : out   std_logic_vector(1 downto 0);                     -- dqm
			sdram_wire_ras_n                                   : out   std_logic;                                        -- ras_n
			sdram_wire_we_n                                    : out   std_logic;                                        -- we_n
			switch_external_connection_export                  : in    std_logic_vector(9 downto 0)  := (others => 'X')  -- export
		);
	end component snake;

	u0 : component snake
		port map (
			accelerometer_spi_external_interface_I2C_SDAT      => CONNECTED_TO_accelerometer_spi_external_interface_I2C_SDAT,      -- accelerometer_spi_external_interface.I2C_SDAT
			accelerometer_spi_external_interface_I2C_SCLK      => CONNECTED_TO_accelerometer_spi_external_interface_I2C_SCLK,      --                                     .I2C_SCLK
			accelerometer_spi_external_interface_G_SENSOR_CS_N => CONNECTED_TO_accelerometer_spi_external_interface_G_SENSOR_CS_N, --                                     .G_SENSOR_CS_N
			accelerometer_spi_external_interface_G_SENSOR_INT  => CONNECTED_TO_accelerometer_spi_external_interface_G_SENSOR_INT,  --                                     .G_SENSOR_INT
			altpll_areset_conduit_export                       => CONNECTED_TO_altpll_areset_conduit_export,                       --                altpll_areset_conduit.export
			altpll_locked_conduit_export                       => CONNECTED_TO_altpll_locked_conduit_export,                       --                altpll_locked_conduit.export
			button_external_connection_export                  => CONNECTED_TO_button_external_connection_export,                  --           button_external_connection.export
			clk_clk                                            => CONNECTED_TO_clk_clk,                                            --                                  clk.clk
			clk_sdram_clk                                      => CONNECTED_TO_clk_sdram_clk,                                      --                            clk_sdram.clk
			hex0_external_connection_export                    => CONNECTED_TO_hex0_external_connection_export,                    --             hex0_external_connection.export
			hex1_external_connection_export                    => CONNECTED_TO_hex1_external_connection_export,                    --             hex1_external_connection.export
			hex2_external_connection_export                    => CONNECTED_TO_hex2_external_connection_export,                    --             hex2_external_connection.export
			hex3_external_connection_export                    => CONNECTED_TO_hex3_external_connection_export,                    --             hex3_external_connection.export
			hex4_external_connection_export                    => CONNECTED_TO_hex4_external_connection_export,                    --             hex4_external_connection.export
			hex5_external_connection_export                    => CONNECTED_TO_hex5_external_connection_export,                    --             hex5_external_connection.export
			led_external_connection_export                     => CONNECTED_TO_led_external_connection_export,                     --              led_external_connection.export
			reset_reset_n                                      => CONNECTED_TO_reset_reset_n,                                      --                                reset.reset_n
			sdram_wire_addr                                    => CONNECTED_TO_sdram_wire_addr,                                    --                           sdram_wire.addr
			sdram_wire_ba                                      => CONNECTED_TO_sdram_wire_ba,                                      --                                     .ba
			sdram_wire_cas_n                                   => CONNECTED_TO_sdram_wire_cas_n,                                   --                                     .cas_n
			sdram_wire_cke                                     => CONNECTED_TO_sdram_wire_cke,                                     --                                     .cke
			sdram_wire_cs_n                                    => CONNECTED_TO_sdram_wire_cs_n,                                    --                                     .cs_n
			sdram_wire_dq                                      => CONNECTED_TO_sdram_wire_dq,                                      --                                     .dq
			sdram_wire_dqm                                     => CONNECTED_TO_sdram_wire_dqm,                                     --                                     .dqm
			sdram_wire_ras_n                                   => CONNECTED_TO_sdram_wire_ras_n,                                   --                                     .ras_n
			sdram_wire_we_n                                    => CONNECTED_TO_sdram_wire_we_n,                                    --                                     .we_n
			switch_external_connection_export                  => CONNECTED_TO_switch_external_connection_export                   --           switch_external_connection.export
		);

