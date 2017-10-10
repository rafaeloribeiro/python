#!/usr/bin/env python
# ----------------------------------------------------------------------
# TCP Throughput Calculator
# Creation date: 2017-10-09
# Creator: Rafael de Oliveira Ribeiro <rafael.ribeiro@ieee.org>
# Last updated: 2017-10-09
# Last updated by: Rafael de Oliveira Ribeiro <rafael.ribeiro@ieee.org>
# ----------------------------------------------------------------------
# Script created for calculating TCP throughput, based on Mathis'
# Equation, as described in "Macroscopic Behavior of the TCP Congestion 
# Avoidance Algorithm" paper, Sigcomm 1997
# (URL: http://ccr.sigcomm.org/archive/1997/jul97/ccr-9707-mathis.pdf)
#

import math        # needed for most calculations
import matplotlib.pyplot as plt
import sys         # for I/O and exiting out of the program

def input_data(*args, **kwargs):  # Will be defined later, for normalising data from input.
    pass

def tcp_thro_calc(rtt, mss, packet_loss):
    '''
    This functions calculates the estimated upper bound bandwidth
    for a particular connection, based on the measured values of:
        - RTT latency, in ms;
        - MSS, in bytes; and,
        - Packet loss, in percentage

    As per the works of Mathis et. al, the returned bandwitdh is:
        
        BW < (MSS/RTT)*(1/sqrt(Packet loss)) 
    '''
    try: 
        bw = ((mss)/(rtt*pow(packet_loss,1/2)))/8 # returning in bits/s
    except ZeroDivisionError:
        return False
    return bw

if __name__ == '__main__':

    RTT_test = [10.0,15.0,20.0,25.0,30.0,35.5,40.0,45.0,50.0]    # Just test data, remember: ms!
    MSS_test = 1440                          # Just test data, remember: bytes!
    packet_loss =[1.0,0.5,0.1,0.05,0.01,0.005,0.001,0.0005,0.0001] # Just test data, remember: percent!

    bw_test_1 = {}
    x1 = []
    y1 = []

    for valor in RTT_test:
        round_trip = valor/1000
        bandwidth = tcp_thro_calc(round_trip,MSS_test,packet_loss[0])
        bw_test_1[valor] = bandwidth
        x1.append(valor)      # for the graph
        y1.append(bandwidth)  # for the graph

    plt.subplot(2,1,1)
    plt.plot(x1,y1, 'o-')
    plt.title('RTT and packet loss variation')
    plt.xlabel('Round trip time (ms)')
    plt.ylabel('Max_BW (b/s)')

    bw_test_2 = {}
    x2 = []
    y2 = []

    for valor in packet_loss:
        round_trip = RTT_test[0]/1000
        p_loss = valor/100
        bandwidth = tcp_thro_calc(round_trip,MSS_test,p_loss)
        bw_test_2[valor] = bandwidth
        x2.append(p_loss) # for the graph
        y2.append(bandwidth)  # for the graph

    plt.subplot(2,1,2)
    plt.plot(x2,y2, 'o-')
    plt.xlabel('Packet loss')
    plt.ylabel('Max_BW (b/s)')

    plt.show()

