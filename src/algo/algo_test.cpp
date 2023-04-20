# include "algo_test.h"
# include <iostream>

using namespace std;
int algoTest()
{
    cout<<"_algo"<<"_test"<<endl;
    return 0;
}

int algoFib(int n)
{
    int a=0,b=1;
    for (int i=0;i<(n+1)/2;i++){
        a+=b;
        b+=a;
    }
    if ((n)%2==1){
        return a;
    }
    else {
        return b;
    }
}