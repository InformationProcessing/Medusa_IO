
#include "system.h"
#include "altera_up_avalon_accelerometer_spi.h"
#include "altera_avalon_timer_regs.h"
#include "altera_avalon_timer.h"
#include "altera_avalon_pio_regs.h"
#include "sys/alt_stdio.h"
#include "sys/alt_irq.h"
#include "sys/alt_timestamp.h"

#include <stdlib.h>
#include <string.h>
#include <stdio.h>


//UART input parsing
#define TOKEN_SIZE 8
#define BUFFER_SIZE 64

//UART output parsing
#define HEX_BUF_SIZE 8

//UART input buffer
char* cmdbuffer;

//Hex buffer declaration
char* hexbuffers[3];

//Hex display buffer
#define DISP_BUF_SIZE 100
char* disp_buf;
int disp_offset = 0;
int disp_length = 0;

//Led flash
#define LED_BUF_SIZE 100
char* led_buf;
int led_offset = -1;
int led_val = 0;

//Global accelerometer declaration
alt_up_accelerometer_spi_dev * acc_dev;

//Buffer typing & coeffs
#define RING_SIZE 59
double h[] = {0.0046, 0.0074, -0.0024, -0.0071, 0.0033, 0.0001, -0.0094, 0.0040, 0.0044, -0.0133, 0.0030, 0.0114, -0.0179,
		-0.0011, 0.0223, -0.0225, -0.0109, 0.0396, -0.0263, -0.0338, 0.0752, -0.0289, -0.1204, 0.2879, 0.6369, 0.2879, -0.1204,
		-0.0289, 0.0752, -0.0338, -0.0263, 0.0396, -0.0109, -0.0225, 0.0223, -0.0011, -0.0179, 0.0114, 0.0030, -0.0133, 0.0044,
		0.0040, -0.0094, 0.0001, 0.0033, -0.0071, -0.0024, 0.0074, 0.0046};

//Latency timer
int debug = 0;
alt_64 latency;

//Fixed point related declarations
#define FIXED alt_32
#define POINT 11
alt_32 quality = 50;
alt_32 norm_const;

//Forward declarations
void throw_code(char* regname, int code);
void read_request();
void to_hex(alt_32 val, int length, char* buf );
void parse_request(char* request);

void hw_push_value(alt_32 xvalue, alt_32 yvalue);
void hw_push_coefficients(alt_32 xvalue, alt_32 yvalue);
alt_32 hw_x_read();
alt_32 hw_y_read();


//Ring buffer
//---------------------------------------------------------------

void coeffs_to_fixed(){

	hw_reset();

	double sum = 0;
	int real_index = 0;
	alt_32 temp;

	//Multiply to shift for fixed point
	int scalefactor = 1 << POINT;

	//Re-indexing
	int lower_bound = RING_SIZE/2 - quality/2;
	int upper_bound = RING_SIZE/2 + quality/2;

	//Indexing system for taking values from center of impulse response array

	for(int i = lower_bound; i< upper_bound; i++){

		temp = (FIXED)(h[i]*scalefactor);
		hw_push_coefficients(temp, temp);
		sum += h[i];

		//Index calculation for hselect
		real_index++;
	}

	//Floating point scaling factor
	 sum = 1/sum;

	 //Fixed point conversion of normalization constant
	 norm_const = (FIXED)((int)(sum*scalefactor));
	 hw_push_coefficients(norm_const, norm_const);
}

int second_letter_to_hex(char in){
	switch(in){
		case 'M':
			return 0b10101011;
	};
	return 0b11111111;
}


int letter_to_hex(char in, int* second){

	switch(in){
		case '0':
			return 0b11000000;
		case '1':
			return 0b11111001;
		case '2':
			return 0b10100100;
		case '3':
			return 0b10110000;
		case '4':
			return 0b10011001;
		case '5':
			return 0b10010010;
		case '6':
			return 0b10000010;
		case '7':
			return 0b11111000;
		case '8':
			return 0b10000000;
		case '9':
			return 0b10010000;
		case 'A':
			return 0b10001000;
		case 'B'://Lowercase
			return 0b10000011;
		case 'C':
			return 0b11000110;
		case 'D'://Lowercase
			return 0b10100001;
		case 'E':
			return 0b10000110;
		case 'F':
			return 0b10001110;
		case 'G':
			return 0b10010000;
		case 'H':
			return 0b10001001;
		case 'I':
			return 0b11111001;
		case 'J':
			return 0b11110001;
		case 'K':
			return 0b10001010;
		case 'L':
			return 0b11000111;
		case 'M':
			*second = 1;
			return 0b10101011;
		case 'N':
			return 0b10101011;
		case 'O':
			return 0b11000000;
		case 'P':
			return 0b10001100;
		case 'Q':
			return 0b10011000;
		case 'R'://Lowercase
			return 0b10101111;
		case 'S':
			return 0b10010010;
		case 'T':
			return 0b10000111;
		case 'U':
			return 0b11000001;
		case 'V':
			return 0b11100011;
		case 'X':
			return 0b10011011;
		case 'Y':
			return 0b10010001;
		case 'Z':
			return 0b10100100;
		case '.':
			return 0b00000000;
		default:
			return 0b11111111;
	};

	return 0;
}

void write_char(alt_32 code, int index){
	if (index == 5){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX5_BASE, code);
	} else if (index == 4){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX4_BASE, code);
	}else if (index == 3){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX3_BASE, code);
	}else if (index == 2){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX2_BASE, code);
	}else if (index == 1){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX1_BASE, code);
	}else if (index == 0){
		IOWR_ALTERA_AVALON_PIO_DATA(HEX0_BASE, code);
	}
}
//Display processing
void write_to_disp(char* str, int offset){
	int second = 0;
	int code;
	int char_offset = 0;
	int flag;

	for(int i = 5; i>=0; i--){
		if (second){
			code = second_letter_to_hex(str[offset+char_offset]);
			write_char(code, i);
			second = 0;
			char_offset++;
			 flag = 0;
		}else{
			second = 0;
			flag = 0;
			code = letter_to_hex(str[offset+char_offset], &second);
			write_char(code, i);

			if(second == 0){char_offset++;}
		}
	}
}


void clr_disp(){
	IOWR_ALTERA_AVALON_PIO_DATA(HEX0_BASE, 255);
	IOWR_ALTERA_AVALON_PIO_DATA(HEX1_BASE, 255);
	IOWR_ALTERA_AVALON_PIO_DATA(HEX2_BASE, 255);
	IOWR_ALTERA_AVALON_PIO_DATA(HEX3_BASE, 255);
	IOWR_ALTERA_AVALON_PIO_DATA(HEX4_BASE, 255);
	IOWR_ALTERA_AVALON_PIO_DATA(HEX5_BASE, 255);
}


//Input tokenization and parsing
//---------------------------------------------------------------
void read_request(char* outbuf){
	char c;
	int idx = 0;

	//Clear previous request from buffer
	memset(outbuf, 0, BUFFER_SIZE);

	//Get first character
	c = alt_getchar();

	//Start timer after first char received
	latency = alt_timestamp();

	while(c != '\n'){
		outbuf[idx] = c;
		c = alt_getchar();
		idx++;
	}
	outbuf[idx] = ' ';

}

void parse_request(char* request){
	int token_number = 0;
	char* tokens[8] = {};
	char* token;


	token = strtok(cmdbuffer, " ");


	while(token != NULL){
		tokens[token_number]= token;
		token_number++;
		token = strtok(NULL, " ");
	}

	if(token_number == 0 || strcmp(tokens[0], &"R" ) != 0){
		throw_code(&"ERR", 1);
		return;
	}

	//Read request parsing
	int is_all = (strcmp(tokens[1], &"ALL") == 0); //Strcmp is weird and equal is denoted by 0
	int matched = 0;

	if(is_all || (strcmp(tokens[1], &"ACCPROC") == 0)){
		//alt_printf("Tried to read accproc");
		matched = 1;

		alt_32 x,y,z;
			x = hw_x_read();
			y = hw_y_read();
			alt_up_accelerometer_spi_read_z_axis(acc_dev, & z);

			to_hex(x, 3, hexbuffers[0]);
			to_hex(y, 3, hexbuffers[1]);
			to_hex(z, 3, hexbuffers[2]);

			if (is_all){
				alt_printf("K ACCPROC X%sY%sZ%s ", hexbuffers[0], hexbuffers[1], hexbuffers[2]);
			}
			else{
				alt_printf("K ACCPROC X%sY%sZ%s 0\n", hexbuffers[0], hexbuffers[1], hexbuffers[2]);
			}

	}
	if (is_all || strcmp(tokens[1], &"ACCRAW") == 0){
		matched = 1;

		//Direct accelerometer read
		alt_32 x,y,z;
		alt_up_accelerometer_spi_read_x_axis(acc_dev, & x);
		alt_up_accelerometer_spi_read_y_axis(acc_dev, & y);
		alt_up_accelerometer_spi_read_z_axis(acc_dev, & z);

		to_hex(x, 3, hexbuffers[0]);
		to_hex(y, 3, hexbuffers[1]);
		to_hex(z, 3, hexbuffers[2]);

		if (is_all){
			printf("ACCRAW X%sY%sZ%s ", hexbuffers[0], hexbuffers[1], hexbuffers[2]);
		}
		else{
			printf("K ACCRAW X%sY%sZ%s 0\n", hexbuffers[0], hexbuffers[1], hexbuffers[2]);
		}

	}
	if (is_all || strcmp(tokens[1], &"BUTTON") == 0){

		matched = 1;
		alt_32 button = ~IORD_ALTERA_AVALON_PIO_DATA(BUTTON_BASE);

		//Button response processing
		//Bitmask
		alt_32 mask = 0x3;
		button = button & mask;

		if (is_all){
			alt_printf("BUTTON %x ", button);
		}
		else{
			alt_printf("K BUTTON %x 0\n", button);
		}

	}
	if (is_all || strcmp(tokens[1], &"SWITCH") == 0){
		//alt_printf("Tried to read switch");
		matched = 1;

		alt_32 switches = ~IORD_ALTERA_AVALON_PIO_DATA(SWITCH_BASE);
		switches &= 0x3ff;
		to_hex(switches, 3, hexbuffers[0]);

		if (is_all){
			alt_printf("SWITCH %x ", switches);
		}
		else{
			alt_printf("K SWITCH %x 0\n", switches);
		}

	}

	//Saves unnecessary comparisons
	if (is_all){
		alt_printf(" 0\n");
		return;
	}


	//Write request parsing

	if (strcmp(tokens[1], &"HEXTEXT") == 0){

		//alt_printf("Tried to write HEXTEXT");
		matched = 1;
		memset(disp_buf, 0,(DISP_BUF_SIZE) * sizeof(char));
		strncpy(disp_buf, tokens[2], DISP_BUF_SIZE);
		disp_length = strlen(disp_buf);
		if(strlen(disp_buf)>6){

			memmove((disp_buf+5),disp_buf,disp_length);
			disp_buf[0] = '_';
			disp_buf[1] = '_';
			disp_buf[2] = '_';
			disp_buf[3] = '_';
			disp_buf[4] = '_';
			strcat(disp_buf, &"_____");
		}
		disp_offset = 0;
		disp_length = strlen(disp_buf);

		throw_code(&"HEXTEXT", 0);
	}

	if (strcmp(tokens[1], &"LEDWRITE") == 0){

		//alt_printf("Tried to write LEDWRITE");
		led_val = (int) strtol(tokens[2], 0, 16);
		IOWR(LED_BASE, 0, led_val);
		throw_code(&"LEDWRITE", 0);
		matched = 1;

	}
	if (strcmp(tokens[1], &"ACCQUAL") == 0){

			//alt_printf("Tried to write LEDWRITE");
			quality = (int) strtol(tokens[2], 0, 10);

			if (quality<0) {
				quality = 0;
				throw_code(&"ACCQUAL", 1);
			}
			else if (quality > RING_SIZE){
				quality = RING_SIZE;
				throw_code(&"ACCQUAL", 1);
			}
			else {
				throw_code(&"ACCQUAL", 0);
			}

			coeffs_to_fixed();

			matched = 1;

		}
	if (strcmp(tokens[1], &"LEDFLASH") == 0){

		//alt_printf("Tried to write LEDFLASH");
		memset(led_buf, 0,(LED_BUF_SIZE) * sizeof(char));
		strncpy(led_buf, tokens[2], LED_BUF_SIZE);
		led_offset = 0;
		throw_code(&"LEDFLASH", 0);
		matched = 1;

		}
	if (strcmp(tokens[1], &"DEBUG") == 0){

			debug = (int) strtol(tokens[2], 0, 16);
			throw_code(&"DEBUG", 0);
			matched = 1;
		}

	if (!matched){
		throw_code(&"ERR", 2);
		matched = 1;
	}

}


// Timer code
//---------------------------------------------------------------


void acc_timer_init(void * isr) {

    IOWR_ALTERA_AVALON_TIMER_CONTROL(ACC_TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(ACC_TIMER_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(ACC_TIMER_BASE, 0xfbd0);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(ACC_TIMER_BASE, 0x0001);
    alt_irq_register(ACC_TIMER_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(ACC_TIMER_BASE, 0x0007);

}

void acc_timer_isr() {
    IOWR_ALTERA_AVALON_TIMER_STATUS(ACC_TIMER_BASE, 0);


    alt_32 x,y;

    alt_up_accelerometer_spi_read_x_axis(acc_dev, & x);
	alt_up_accelerometer_spi_read_y_axis(acc_dev, & y);

	hw_push_value(x,y);


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

void disp_timer_init(void * isr) {
    IOWR_ALTERA_AVALON_TIMER_CONTROL(HEX_TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(HEX_TIMER_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(HEX_TIMER_BASE, 0x5a00);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(HEX_TIMER_BASE, 0x0262);
    alt_irq_register(HEX_TIMER_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(HEX_TIMER_BASE, 0x0007);

}

void disp_timer_isr() {
	IOWR_ALTERA_AVALON_TIMER_STATUS(HEX_TIMER_BASE, 0);

    if(disp_buf[disp_offset+5] == '\0'){
    	disp_offset = 0;
    }
    else{
    	disp_offset++;
    }
    write_to_disp(disp_buf,disp_offset);



}

void led_timer_init(void * isr) {
    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(TIMER_BASE, 0x5d40);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(TIMER_BASE, 0x00c6);
    alt_irq_register(TIMER_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER_BASE, 0x0007);

}

void led_timer_isr() {
	IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER_BASE, 0);

	if (led_offset != -1){


		if (led_buf[led_offset] == '\0'){
			led_offset = -1;
			IOWR(LED_BASE, 0, led_val);

		}
		else if (led_buf[led_offset] == '1'){
			led_offset++;
			IOWR(LED_BASE, 0, 1023);
		}
		else{
			led_offset++;
			IOWR(LED_BASE, 0, 0);
		}
	}


}


//Input processing
//---------------------------------------------------------------
//Function takes integer and writes to character buffer the hex representation in
//such a way that it is padded or cut down to length

void to_hex(alt_32 val, int length, char* buf ){
	//Clear previous data from buffer and write new
	memset(buf, 0, HEX_BUF_SIZE);
	sprintf(buf, "%x", val);
	int hexlen = strlen(buf);

	//Left shift if string is longer than desired length to take least significant
	if (hexlen > length){
		for(int i = 0; i < length; i++){
			buf[i] = buf[(i + hexlen - length)];
		}
	}
	//Right shift to align if desired hex is shorter than desired
	else if (hexlen < length){
		for(int i = 0; i < length; i++){
			if(i < hexlen){
				buf[(length - 1 - i)] = buf[(length - 1 - i) - (length-hexlen)];
			}
			else{
				buf[(length - 1 - i)] = '0';
			}

		}
	}
	//Add termination
	buf[length] = '\0';

}


void throw_code(char* regname, int code){
	printf("K %s %x\n", regname, code);
}

//Hardware helper functions
void hw_reset(){
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 4);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 7);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);
};

void hw_push_value(alt_32 xvalue, alt_32 yvalue){
	IOWR(HARDWARE_OUT_X_BASE,0, xvalue);
	IOWR(HARDWARE_OUT_Y_BASE,0, yvalue);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 1);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);

}
void hw_push_coefficients(alt_32 xvalue, alt_32 yvalue){
	IOWR(HARDWARE_OUT_X_BASE,0, xvalue);
	IOWR(HARDWARE_OUT_Y_BASE,0, yvalue);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 2);
	IOWR(HARDWARE_CLOCKS_BASE, 0, 0);
}
alt_32 hw_x_read(){
	return IORD_ALTERA_AVALON_PIO_DATA(HARDWARE_IN_X_BASE);
}

alt_32 hw_y_read(){
	return IORD_ALTERA_AVALON_PIO_DATA(HARDWARE_IN_Y_BASE);
}

//Main function
int main() {


	//Initialize fixed point coefficients
	coeffs_to_fixed();

	//Clear display from flash message and add
	disp_buf = malloc(DISP_BUF_SIZE * sizeof(char));
	strcpy(disp_buf, "______");
	clr_disp();
	disp_timer_init(disp_timer_isr);
	disp_length = 6;

	//Ledflash initialization
	led_buf = malloc(LED_BUF_SIZE * sizeof(char));
	led_timer_init(led_timer_isr);
	led_offset = -1;
	IOWR(LED_BASE, 0, 0);


	//UART buffer instantiation
	cmdbuffer = malloc( BUFFER_SIZE * sizeof(char));

	//Initialize hex output buffers
	hexbuffers[0] = malloc( HEX_BUF_SIZE * sizeof(char));
	hexbuffers[1] = malloc( HEX_BUF_SIZE * sizeof(char));
	hexbuffers[2] = malloc( HEX_BUF_SIZE * sizeof(char));


	//Display buffer
	disp_buf  = malloc((DISP_BUF_SIZE) * sizeof(char));
	memset(disp_buf, 0,(DISP_BUF_SIZE) * sizeof(char));

	//Accelerometer initialization
	acc_dev = alt_up_accelerometer_spi_open_dev("/dev/accelerometer_spi");


	//1kHz timer routine initialization
	acc_timer_init(acc_timer_isr);
	alt_timestamp_start();

	//Command response loop
	while(1){
		read_request(cmdbuffer);
		parse_request(cmdbuffer);

		//Request response timing: first char received to last char sent
		if (debug){
			printf("Response time (us) : %i \n",(alt_timestamp()-latency)/(alt_timestamp_freq()/1000000));
		}
	}

    return 0;
}

