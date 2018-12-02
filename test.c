/*this is a comment*/
#define harrison 56
int j = 10;

int main(){
    //hello
    port a = 0x0001;
    int k = 10;
    int i = 5 + 1;
    j = i + 2;
    enable interrupt;
    if(i == 6){
        j = i & 2;
        k = k ^ 4;
    }
    // Here's another
    else{
        j = 1;
        k = 2;
    }
    while(j < 12){
        i = i | 2;
        i = i + 2;
    }
    for(int z = 0; z < 10; z++){
        k = k + 1;
    }
    disable interrupt;
    
}
Interrupt_Handler(){
    j = 50;
    output(j, a);
    input(j, a);
}