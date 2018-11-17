
int main(){
    port a = 1;
    int k = 10;
    int i = 5 + 1;
    int j = i + 2;
    enable interrupt;
    if(i == 6){
        j = i + 2;
        k = k + 4;
    }
    else{
        j = 1;
        k = 2;
    }
    while(j < 12){
        i = i + 1;
        i = i + 2;
    }
    for(int z = 0; z < 10; z++){
        k = k + 1;
    }
    disable interrupt;
    
}

Interrupt_Handler(){
    j = 50;
    output(i, a);
    input(i, a);
}