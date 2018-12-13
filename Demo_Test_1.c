// This is a simple test of the CECS 490 Compiler

/*  The target architecture is the tramelblaze
    this particular example sends ascii characters
    to the LCD. */
#define a 0x61
#define b 0x62
#define c 0x63
#define d 0x64
#define e 0x65
#define f 0x66
#define g 0x67
#define h 0x68
#define i 0x69
#define j 0x6A
#define k 0x6B
#define l 0x6C
#define m 0x6D
#define n 0x6E
#define o 0x6F
#define p 0x70
#define q 0x71
#define r 0x72
#define s 0x73
#define t 0x74
#define u 0x75
#define v 0x76
#define w 0x77
#define x 0x78
#define y 0x79
#define z 0x7A


port I2C_ADDR_PORT = 1;
port I2C_DATA_PORT = 2;
port I2C_CMD_PORT = 3;
port I2C_STATUS_PORT = 4;
port SW_ADDR_PORT = 5;
port SW_DATA_PORT = 6;

int ready_flag = 1;
int temp = 0;
int address = 0;
int data = a;
int cmd = 0;

int main() {
    enable interrupt;
    while(1);
    
   
}
Interrupt_Handler(){
    temp = 0;
    address = 0;
    data = 0;
    cmd = 1;
    input(temp, I2C_STATUS_PORT);
    if(temp == 1){
        input(address, SW_ADDR_PORT );
        
        output(address, I2C_ADDR_PORT);
        output(data, I2C_DATA_PORT);
        output(cmd, I2C_CMD_PORT);
    }
    data = data + 1;
    if(data == z)
        data = a;
}

