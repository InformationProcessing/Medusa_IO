/*
 * timers
 *
 *  Created on: Mar 10, 2022
 *      Author: michal
 */
// Timer code
//---------------------------------------------------------------

#include "system.h"
#include "timers.h"


void acc_timer_init(void * isr) {
	//Calculate necessary cycles for 1 ms period
	alt_32 freq = 1000;
	alt_32 period = alt_timestamp_freq()/freq;

    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER1_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER1_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(TIMER1_BASE, 0xfbd0);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(TIMER1_BASE, 0x0001);
    alt_irq_register(TIMER1_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER1_BASE, 0x0007);

}

void acc_timer_isr() {
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER1_BASE, 0);


    alt_32 x,y,z;

    alt_up_accelerometer_spi_read_x_axis(acc_dev, & x);
	alt_up_accelerometer_spi_read_y_axis(acc_dev, & y);
	alt_up_accelerometer_spi_read_z_axis(acc_dev, & z);

	ring_buf_push(x_buf, x);
	ring_buf_push(y_buf, y);
	ring_buf_push(z_buf, z);

	//iNTERRUPT FREQUENCY MONITORING
	static int count;
	static alt_64 lasttime;

    if(debug && ((count & 4095) == 0) ){
    	printf("Avg sampling period (us): %i\n", (alt_timestamp()-lasttime)/4096 /(alt_timestamp_freq()/1000000) );
		count = 1;
		lasttime = alt_timestamp();
    }
    count++;
}

void hex_timer_init(void * isr) {
	//Calculate necessary cycles for 1 ms period
	alt_32 freq = 5;
	alt_32 period = alt_timestamp_freq()/freq;


    IOWR_ALTERA_AVALON_TIMER_CONTROL(HEX_TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER1_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(TIMER1_BASE, 0xfbd0);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(TIMER1_BASE, 0x0001);
    alt_irq_register(TIMER1_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER1_BASE, 0x0007);

}

void hex_timer_isr() {
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER1_BASE, 0);


    alt_32 x,y,z;

    alt_up_accelerometer_spi_read_x_axis(acc_dev, & x);
	alt_up_accelerometer_spi_read_y_axis(acc_dev, & y);
	alt_up_accelerometer_spi_read_z_axis(acc_dev, & z);

	ring_buf_push(x_buf, x);
	ring_buf_push(y_buf, y);
	ring_buf_push(z_buf, z);

	//iNTERRUPT FREQUENCY MONITORING
	static int count;
	static alt_64 lasttime;

    if(debug && ((count & 4095) == 0) ){
    	printf("Avg sampling period (us): %i\n", (alt_timestamp()-lasttime)/4096 /(alt_timestamp_freq()/1000000) );
		count = 1;
		lasttime = alt_timestamp();
    }
    count++;
}

