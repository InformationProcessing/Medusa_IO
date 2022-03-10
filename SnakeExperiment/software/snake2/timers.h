/*
 * timers.h
 *
 *  Created on: Mar 10, 2022
 *      Author: micha
 */

#ifndef TIMERS_H_
#define TIMERS_H_

void acc_timer_init(void * isr);
void acc_timer_isr();
void hex_timer_init(void * isr);
void hex_timer_isr();

extern int debug;


#endif /* TIMERS_H_ */
