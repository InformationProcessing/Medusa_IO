
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
#define RING_T alt_32
#define RING_SIZE 29
double h[] = {0.0030, 0.0114, -0.0179, -0.0011, 0.0223, -0.0225, -0.0109, 0.0396, -0.0263,\
		-0.0338, 0.0752, -0.0289, -0.1204, 0.2879, 0.6369, 0.2879, -0.1204, -0.0289, 0.0752, \
		-0.0338, -0.0263, 0.0396, -0.0109, -0.0225, 0.0223, -0.0011, -0.0179, 0.0114, 0.0030};

//X,Y,Z accelerometer buffers
struct ring_buffer *x_buf;
struct ring_buffer *y_buf;
struct ring_buffer *z_buf;

//Latency timer
int debug = 0;
alt_64 latency;



//Forward declarations

void timer_init(void * isr);
void throw_code(char* regname, int code);
alt_32 get_input(char x);
void read_request();
void to_hex(alt_32 val, int length, char* buf );
void parse_request(char* request);
//int write_to_disp(char* str, int offset);


//Ring buffer
//---------------------------------------------------------------
struct ring_buffer {
	int size;
	int next_free;
	RING_T* values;
};

//Buffer functions
void ring_buf_push(struct ring_buffer* buf, RING_T in){
	if (buf->next_free < 0){
		buf->next_free = buf ->size-1;
	}
	(buf->values)[buf->next_free] = in;
	(buf->next_free)--;
}

RING_T ring_buf_read(struct ring_buffer* buf, RING_T idx){
	int mapped_idx;
	if (buf->next_free+1+idx >= buf->size){
		mapped_idx = buf->next_free+1+idx - buf->size;
	}
	else {
		mapped_idx = buf->next_free+1+idx;
	}

	return buf->values[mapped_idx];
}

alt_32 convolve_float(struct ring_buffer* buf, double coefficients[]  ){

	//Disabling interrupts prevents accelerometer buffers being overwritten while value is calculated
	//alt_irq_context state = alt_irq_disable_all ();
	alt_irq_disable(TIMER_IRQ);

	double sum = 0;
	for(int i = 0; i < buf->size; i ++){
		sum += ring_buf_read(buf, i)* coefficients[i];
	}

	//Re-enable interrupts from state
	//alt_irq_enable_all(state);
	alt_irq_enable(TIMER_IRQ);
	return (alt_32)sum;

}


int letter_to_hex(char in){

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
			return 0b10011001;
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

//Display processing
void write_to_disp(char* str, int offset){

	IOWR_ALTERA_AVALON_PIO_DATA(HEX5_BASE, letter_to_hex(str[offset]));
	IOWR_ALTERA_AVALON_PIO_DATA(HEX4_BASE, letter_to_hex(str[offset+1]));
	IOWR_ALTERA_AVALON_PIO_DATA(HEX3_BASE, letter_to_hex(str[offset+2]));
	IOWR_ALTERA_AVALON_PIO_DATA(HEX2_BASE, letter_to_hex(str[offset+3]));
	IOWR_ALTERA_AVALON_PIO_DATA(HEX1_BASE, letter_to_hex(str[offset+4]));
	IOWR_ALTERA_AVALON_PIO_DATA(HEX0_BASE, letter_to_hex(str[offset+5]));
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
			x = convolve_float(x_buf, h);
			y = convolve_float(y_buf, h);
			z = convolve_float(z_buf, h);

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
	if (strcmp(tokens[1], &"LEDFLASH") == 0){

		//alt_printf("Tried to write LEDFLASH");
		memset(led_buf, 0,(LED_BUF_SIZE) * sizeof(char));
		strncpy(led_buf, tokens[2], LED_BUF_SIZE);
		led_offset = 0;
		throw_code(&"LEDWRITE", 0);
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
	//Calculate necessary cycles for 1 ms period
//	alt_32 freq = 1000;
//	alt_32 period = alt_timestamp_freq()/freq;

    IOWR_ALTERA_AVALON_TIMER_CONTROL(ACC_TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(ACC_TIMER_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(ACC_TIMER_BASE, 0xfbd0);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(ACC_TIMER_BASE, 0x0001);
    alt_irq_register(ACC_TIMER_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(ACC_TIMER_BASE, 0x0007);

}

void acc_timer_isr() {
    IOWR_ALTERA_AVALON_TIMER_STATUS(ACC_TIMER_BASE, 0);


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

void disp_timer_init(void * isr) {
	//Calculate necessary cycles for 1 ms period
//	alt_32 freq = 5;
//	alt_32 period = alt_timestamp_freq()/freq;


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
	//Calculate necessary cycles for 1 ms period
//	alt_32 freq = 5;
//	alt_32 period = alt_timestamp_freq()/freq;


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


alt_32 get_input(char x){

	alt_32 thresh = 150;

	//Temp gating code
	if(x == 'x'){
		alt_32 x = convolve_float(x_buf, h);
		if(x<-thresh)x = 15;
		else if(x>thresh) x = 1;
		else x = 0;

		return x;

	}
	else if(x == 'y'){
		alt_32 y = alt_up_accelerometer_spi_read_y_axis(acc_dev, & y);
		if(y<-thresh)y = 15;
		else if(y>thresh) y = 1;
		else y = 0;

		return y;

	}
	else if(x == 'z'){
		alt_32 z = alt_up_accelerometer_spi_read_z_axis(acc_dev, & z);
		if(z<-thresh)z = 15;
		else if(z>thresh) z = 1;
		else z = 0;

		return z;

	}
	else{
		//throw_code(3);
		return 16;
	}
}


void throw_code(char* regname, int code){
	printf("K %s %x\n", regname, code);
}

//HEX write
//---------------------------------------------------------------


int main() {

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

	//Initialize accelerometer buffers
	struct ring_buffer x,y,z;

	x = (struct ring_buffer){.size = RING_SIZE, .next_free = 0, .values = 0};
	y = (struct ring_buffer){.size = RING_SIZE, .next_free = 0, .values = 0};
	z = (struct ring_buffer){.size = RING_SIZE, .next_free = 0, .values = 0};
	x_buf = &x;
	y_buf = &y;
	z_buf = &z;

	x_buf->values = malloc((RING_SIZE) * sizeof(RING_T));
	memset(x_buf->values, 0,(RING_SIZE) * sizeof(RING_T));
	y_buf->values = malloc((RING_SIZE) * sizeof(RING_T));
	memset(y_buf->values, 0,(RING_SIZE) * sizeof(RING_T));
	z_buf->values = malloc((RING_SIZE) * sizeof(RING_T));
	memset(x_buf->values, 0,(RING_SIZE) * sizeof(RING_T));

	//Display buffer
	disp_buf  = malloc((DISP_BUF_SIZE) * sizeof(char));
	memset(disp_buf, 0,(DISP_BUF_SIZE) * sizeof(char));

	//Accelerometer initialization
	acc_dev = alt_up_accelerometer_spi_open_dev("/dev/accelerometer_spi");


	//to_hex(16,3,hexbuffers[0]);


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

