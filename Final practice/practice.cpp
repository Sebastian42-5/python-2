# include <vector>
# include <iostream>

using namespace std;

int main(){

    vector<string> cars = {"Mazda", "Mitsubishi"};
    
    for (string car : cars){
        cout << car << "\n";
    }

    return 0;
}

