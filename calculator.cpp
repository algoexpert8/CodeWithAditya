#include <iostream>
using namespace std;

int main(){
    double num1, num2;
    char operation;
    cout<<"CALCULATOR:\n";
    cout<<"Enter the 1st number below:\n";
    cin>>num1;
    cout<<"Enter the 2nd number below:\n";
    cin>>num2;
    cout<<"Instructions for selecting the operation:\n Addition : + \n Subtraction : - \n Multiplication : * \n Division : /:\n";
    cout<<"Enter any 1 out of the operations given above:\n";
    cin>>operation;

    switch (operation){
        case '+':
        cout<<"The sum is: "<<num1+num2<<endl;
        break;
        case '-':
        cout<<"The difference is: "<<num1-num2<<endl;
        break;
        case '*':
        cout<<"The product is: "<<num1*num2<<endl;
        break;
        case '/':
        cout<<"The quotient is: "<<num1/num2<<endl;
        break;
        default:
        cout<<"That's an invalid input!";
        
    }
}