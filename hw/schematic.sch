EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Q_NMOS_GDS Q1
U 1 1 5AEB1E72
P 8700 5200
F 0 "Q1" H 8900 5250 50  0000 L CNN
F 1 "FQP50N06" H 8900 5150 50  0000 L CNN
F 2 "" H 8900 5300 50  0001 C CNN
F 3 "" H 8700 5200 50  0001 C CNN
	1    8700 5200
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR?
U 1 1 5AEB1ECC
P 8800 4550
F 0 "#PWR?" H 8800 4400 50  0001 C CNN
F 1 "+12V" H 8800 4690 50  0000 C CNN
F 2 "" H 8800 4550 50  0001 C CNN
F 3 "" H 8800 4550 50  0001 C CNN
	1    8800 4550
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 5AEB1F4C
P 8150 5200
F 0 "R1" V 8230 5200 50  0000 C CNN
F 1 "82" V 8150 5200 50  0000 C CNN
F 2 "" V 8080 5200 50  0001 C CNN
F 3 "" H 8150 5200 50  0001 C CNN
	1    8150 5200
	0    1    1    0   
$EndComp
Wire Wire Line
	7650 5200 8000 5200
Text Label 7650 5200 0    60   ~ 0
GPIO
Wire Wire Line
	8300 5200 8500 5200
$Comp
L GND #PWR?
U 1 1 5AEB208F
P 8800 5650
F 0 "#PWR?" H 8800 5400 50  0001 C CNN
F 1 "GND" H 8800 5500 50  0000 C CNN
F 2 "" H 8800 5650 50  0001 C CNN
F 3 "" H 8800 5650 50  0001 C CNN
	1    8800 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	8800 5400 8800 5650
$Comp
L R R2
U 1 1 5AEB20C5
P 8400 5400
F 0 "R2" V 8480 5400 50  0000 C CNN
F 1 "10k" V 8400 5400 50  0000 C CNN
F 2 "" V 8330 5400 50  0001 C CNN
F 3 "" H 8400 5400 50  0001 C CNN
	1    8400 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	8400 5250 8400 5200
Connection ~ 8400 5200
Wire Wire Line
	8400 5550 8800 5550
Connection ~ 8800 5550
Wire Wire Line
	8800 5000 8800 4950
Wire Wire Line
	8600 4950 9350 4950
Wire Wire Line
	9350 4850 8800 4850
Wire Wire Line
	8800 4850 8800 4550
Text Label 9350 4850 0    60   ~ 0
Valve+
Text Label 9350 4950 0    60   ~ 0
Valve-
$Comp
L D D1
U 1 1 5AEB2314
P 8600 4800
F 0 "D1" H 8600 4900 50  0000 C CNN
F 1 "D?" H 8600 4700 50  0000 C CNN
F 2 "" H 8600 4800 50  0001 C CNN
F 3 "" H 8600 4800 50  0001 C CNN
	1    8600 4800
	0    1    1    0   
$EndComp
Connection ~ 8800 4950
Wire Wire Line
	8600 4650 8800 4650
Connection ~ 8800 4650
$EndSCHEMATC
