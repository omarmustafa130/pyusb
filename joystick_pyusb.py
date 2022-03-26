import usb.core
import time

device = usb.core.find(idVendor = 0x0810, idProduct = 0x0001)

endpoint = device[0].interfaces()[0].endpoints()[0]
interface = device[0].interfaces()[0].bInterfaceNumber

device.reset()

if device.is_kernel_driver_active(interface):
    device.detach_kernel_driver(interface)

device.set_configuration()
endpaddr = endpoint.bEndpointAddress

list_len = 8 # after testing, all buttons and axes of the two joysticks together were put in the first 7 places of the list
while True: 
    ########################  I had two joysticks connected through 1 usb ###########################
    joy_data_1_from_usb = []
    joy_data_2_from_usb = []

    #joy1_axes[]=[R-axis up/down, R-axis left/right, L-axis up/down, L-axis left/right]
    #joy1_buttons[up/down,right/left, triangle, circle, x, rectangle, R1, R2, R3 , L1, L2, L3,select, start]
    joy1_axes = [0,0,0,0]
    joy1_buttons = [0,0,0,0,0,0,0,0,0,0,0,0]
    joy2_axes = [0,0,0,0]
    joy2_buttons = [0,0,0,0,0,0,0,0,0,0,0,0]


    read = device.read(endpaddr, 16)
   

    for i in range (list_len):
        joy_data_1_from_usb.append(read[i])
        joy_data_2_from_usb.append(read[i+8])
    joy_data_1_from_usb=joy_data_1_from_usb[1:7]
    joy_data_2_from_usb=joy_data_2_from_usb[1:7]

################################################# JOY 1 ####################################################


######################################### AXES ############################################

######################### LEFT AXES ################################
    if joy_data_1_from_usb[3] < 128:           #UP
        joy1_axes[2]= (joy_data_1_from_usb[1] * (-1) +128) / 128
    elif joy_data_1_from_usb[3] > 128:         #Down
        joy1_axes[2]= (joy_data_1_from_usb[1] * (-1) +127) / 128
    elif joy_data_1_from_usb[2] < 128:         #Left
        joy1_axes[3]= (joy_data_1_from_usb[2]  +128) / 128
    elif joy_data_1_from_usb[2] > 128:         #Right
        joy1_axes[3]= (joy_data_1_from_usb[2]  *(-1) +126) / 126


######################## RIGHT AXES ################################
    if joy_data_1_from_usb[1] < 128:           #UP
        joy1_axes[0]= (joy_data_1_from_usb[1] * (-1) +128) / 128
    elif joy_data_1_from_usb[1] > 128:         #Down
        joy1_axes[0]= (joy_data_1_from_usb[1] * (-1) +126) / 126
    elif joy_data_1_from_usb[0] < 128:         #Left
        joy1_axes[1]= (joy_data_1_from_usb[0]  +128) / 128
    elif joy_data_1_from_usb[0] > 128:         #Right
        joy1_axes[1]= (joy_data_1_from_usb[0]  *(-1) +126) / 126


   


############################ BUTTONS ###############################
    if joy_data_1_from_usb[4] == 0:         #UP
        joy1_buttons[0]= 1
    elif joy_data_1_from_usb[4] == 4:       #DOWN
        joy1_buttons[0]= -1.
    elif joy_data_1_from_usb[4] == 2:       #RIGHT
        joy1_buttons[1]= 1
    elif joy_data_1_from_usb[4] == 6:       #LEFT
        joy1_buttons[1]= -1
    elif joy_data_1_from_usb[4] == 31:      #Triangle
        joy1_buttons[2]= 1
    elif joy_data_1_from_usb[4] == 47:      #Circle
        joy1_buttons[3]= 1
    elif joy_data_1_from_usb[4] == 79:      #X
        joy1_buttons[4]= 1
    elif joy_data_1_from_usb[4] == 143:     #Rectangle
        joy1_buttons[5]= 1
    if joy_data_1_from_usb[5] == 1:         #L1
        joy1_buttons[9]= 1
    elif joy_data_1_from_usb[5] == 4:       #L2
        joy1_buttons[10]= 1
    elif joy_data_1_from_usb[5] == 2:       #R1
        joy1_buttons[6]= 1
    elif joy_data_1_from_usb[5] == 8:       #R2
        joy1_buttons[7]= 1
    elif joy_data_1_from_usb[5] == 64:      #L3
        joy1_buttons[8]= 1
    elif joy_data_1_from_usb[5] == 128:     #R3
        joy1_buttons[11]= 1
    elif joy_data_1_from_usb[5] == 16:      #Select
        joy1_buttons[12]= 1
    elif joy_data_1_from_usb[5] == 32:      #Start
        joy1_buttons[13]= 1



################################################# JOY 2 ####################################################


######################################### AXES ############################################

######################### LEFT AXES ################################
    if joy_data_2_from_usb[3] < 128:           #UP
        joy2_axes[2]= (joy_data_2_from_usb[3] * (-1) +128) / 128
    elif joy_data_2_from_usb[3] > 128:         #Down
        joy2_axes[2]= (joy_data_2_from_usb[3] * (-1) +127) / 128
    elif joy_data_2_from_usb[2] < 128:         #Left
        joy2_axes[3]= (joy_data_2_from_usb[2]  +128) / 128
    elif joy_data_2_from_usb[2] > 128:         #Right
        joy2_axes[3]= (joy_data_2_from_usb[2] * (-1) +127) / 128

######################## RIGHT AXES ################################
    if joy_data_2_from_usb[1] < 128:           #UP
        joy2_axes[0]= (joy_data_2_from_usb[1] * (-1) +128) / 128
    elif joy_data_2_from_usb[1] > 128:         #Down
        joy2_axes[0]= (joy_data_2_from_usb[1] * (-1) +127) / 128
    elif joy_data_2_from_usb[0] < 128:         #Left
        joy2_axes[1]= (joy_data_2_from_usb[0]  +128) / 128
    elif joy_data_2_from_usb[0] > 128:         #Right
        joy2_axes[1]= (joy_data_2_from_usb[0] * (-1) +127) / 128


############################ BUTTONS ###############################
    if joy_data_2_from_usb[4] == 0:         #UP
        joy2_buttons[0]= 1
    elif joy_data_2_from_usb[4] == 4:       #DOWN
        joy2_buttons[0]= -1.
    elif joy_data_2_from_usb[4] == 2:       #RIGHT
        joy2_buttons[1]= 1
    elif joy_data_2_from_usb[4] == 6:       #LEFT
        joy2_buttons[1]= -1
    elif joy_data_2_from_usb[4] == 31:      #Triangle
        joy2_buttons[2]= 1
    elif joy_data_2_from_usb[4] == 47:      #Circle
        joy2_buttons[3]= 1
    elif joy_data_2_from_usb[4] == 79:      #X
        joy2_buttons[4]= 1
    elif joy_data_2_from_usb[4] == 143:     #Rectangle
        joy2_buttons[5]= 1
    if joy_data_2_from_usb[5] == 1:         #L1
        joy2_buttons[9]= 1
    elif joy_data_2_from_usb[5] == 4:       #L2
        joy2_buttons[10]= 1
    elif joy_data_2_from_usb[5] == 2:       #R1
        joy2_buttons[6]= 1
    elif joy_data_2_from_usb[5] == 8:       #R2
        joy2_buttons[7]= 1
    elif joy_data_2_from_usb[5] == 64:      #L3
        joy2_buttons[8]= 1
    elif joy_data_2_from_usb[5] == 128:     #R3
        joy2_buttons[11]= 1
    elif joy_data_2_from_usb[5] == 16:      #Select
        joy2_buttons[12]= 1
    elif joy_data_2_from_usb[5] == 32:      #Start
        joy2_buttons[13]= 1


    print("Joy 1: ", joy1_axes, "                    ", joy1_buttons)
    print("Joy 2: ", joy2_axes, "                    ", joy2_buttons)
