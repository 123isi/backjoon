#include <iostream>
#include <string>
using namespace std;
int main(){
    string a;
    long long n;
    cin >> n;
    cin.ignore();
    int check = 0;
    for (long long i = 0 ; i < n ; i++){
        getline(cin,a);
        if (a == "Never gonna give you up" || a == "Never gonna let you down"||  a == "Never gonna run around and desert you" || a== "Never gonna make you cry" || a== "Never gonna say goodbye" || a== "Never gonna tell a lie and hurt you" || a== "Never gonna stop"){
            check = 1;
        }else{
            check = 0;
            break;
        }
    }
    if (check == 0){
        cout << "Yes";
    }else{
        cout << "No";
    }
}