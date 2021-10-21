// currency converter to convert american dollars to pounds, euro and indian rupee.

#include <iostream>
#include <string>
using namespace std;

int main(){
    double dollar;
    string currency;

    cout<<"CURRENCY CONVERTER\n";
    cout<<"Enter the American Dollars you want to convert:\n";
    cin>>dollar;
    double pound = dollar*0.73;
    double euro = dollar*0.86;
    double rupee = dollar*75.13;

    cout<<"Enter INR for converting USD to INR, GBP for USD to GBP, or EUR for USD to EUR:\n";
    cin>>currency;

    if (currency == "INR"){
        cout<<dollar<< " Dollars In Rupees = "<<rupee;
    }

    else if(currency == "EUR"){
        cout<<dollar<<" Dollars In Euro = "<<euro;

    }

    else if (currency == "GBP"){
        cout<<dollar<<" Dollars in Pounds = "<<pound;
    }
    else{
        cout<<"That's An Invalid Input! Please Try Again.";
    }
}