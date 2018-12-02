port I2C_ADDR_PORT = 1;
port I2C_DATA_PORT = 2;
port I2C_CMD_PORT = 3;
port I2C_STATUS_PORT = 4;
port SW_ADDR_PORT = 5;
port SW_DATA_PORT = 6;

int ready_flag = 1;

int main() {
    enable interrupt;
    while(1);
    
   
}
Interrupt_Handler(){
    int temp = 0;
    int address = 0;
    int data = 0;
    int cmd = 1;
    input(temp, I2C_STATUS_PORT);
    if(temp == 1){
        input(address, SW_ADDR_PORT );
        input(data, SW_DATA_PORT);
        
        output(address, I2C_ADDR_PORT);
        output(data, I2C_DATA_PORT);
        output(cmd, I2C_CMD_PORT);
    }
}
