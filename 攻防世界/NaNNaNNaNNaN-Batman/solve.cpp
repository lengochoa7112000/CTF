#include <iostream>
#include <string>
using namespace std;

int main()
{
	string a[4][4] = {"fl","s_a","i","e}","a","_h0l","n","","g{","e","_0","","it'","_","n",""};
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++)
			cout << a[j][i];
	}
	return 0;
}
