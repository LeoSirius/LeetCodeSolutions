#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int main(){
    string input("Input test 123 4.7 A");
    istringstream input_string_stream(input);
    string str1, str2;
    int i;
    double d;
    char c;
    input_string_stream >> str1 >> str2 >> i >> d >> c;

    cout << str1 << endl << str2 << endl;
    cout << i << endl << d << endl << c << endl;
    long L;
    if(input_string_stream >> L) cout <<  "L = " << L << endl;
    else cout << "empty" << endl;

    return 0; 
}