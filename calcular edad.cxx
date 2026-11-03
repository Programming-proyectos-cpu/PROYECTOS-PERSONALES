#include <iostream>
using namespace std;
int main (){
	
	int edad;
	cout << "Ingrese edad: " << endl;
	cin >> edad;
    
    if (edad >= 18 ){
    	cout << "Eres mayor de edad" << endl;
    }
    else if (edad >=13 && edad <= 16){
    	cout << "Eres un Adolecente" << endl;
    }
    else{
    	cout << "Eres menor de edad" << endl;
    }
	return 0;
}