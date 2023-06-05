/*
Swap Details Entered
An web application was designed by a company to calculate the income tax of its employees as per the latest budget. 
A form was designed to enter the details of the employees and do income tax calculation. 
Since the basic excemption limit, percentage of deductions etc differ based on gender, separate forms are designed in the web application for male and female. 
Number of fields to be entered and width of the fields to be entered are same. By mistake both the genders have entered details in the form for the other gender. 
Internally the details entered by each employee is stored as a string with a delimiter in between. For males ‘:’ is used as the delimiter and for females ‘#’ is used as delimiter.

Given the strings of details of a male and a female employee, write a C++ code to swap the corressponding fields and make it ready for further processing.

For example, if the strings given are 50891:12378949:10000:ACZPJ9823B and 78191#45376107#10200#BFZPJ0453B 
then the output should be 78191:45376107:10200:BFZPJ0453B and 50891#12378949#10000#ACZPJ9823B

*/

#include <iostream>
#include <string>
using namespace std;
int main(){
    string female, male;
    cin>>female>>male;
   
    
    string delimiter1 =":";
    string delimiter2 ="#";
    int l1 = female.find(delimiter1,0);
    int l2 = male.find(delimiter2,0);
    for(int i = 0; i < 3; i++){
        l1 = female.find(delimiter1,0);
        l2 = male.find(delimiter2,0);
        
        female.replace(l1,1,delimiter2);
        male.replace(l2,1,delimiter1);
        
    }
    cout<<male<<endl<<female<<endl;
}
