# include "src_test.h"
# include "algo/algo_test.h"
# include <iostream>


int srcTest()
{
    std::cout<<"_src"<<"_test"<<std::endl;
    return 0;
}


int SrcClass::Fib(int n)
{
    return algoFib(n);
}

int main()
{
    int alg = algoTest();
    int src = srcTest();
    std::cout<<"class_test"<<std::endl;
    SrcClass test ;
    for (int i=0;i<10;i++)
    {
        std::cout<<"class fib "<<test.Fib(i)<<std::endl;
    }

}