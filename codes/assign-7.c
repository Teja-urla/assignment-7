#include<stdio.h>
int main(){
    double a = 4/5.00;               // probability for getting 1st good orange
    double b = 11/14.00;               // probability for  picking a good orange being 1 good orange
    double c = 10/13.00;               //  probability for  picking a good orange being 2 good oranges
  printf("probability of getting all the oranges good is %.2f",a*b*c);
}   
