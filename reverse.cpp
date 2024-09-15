#include<iostream>
using namespace std;
class solution{
public:
int reverse(int x){
    bool check=false;
    if(x<0){
        check=true;
        x=-x;
    }

    int val = 0;

    while(x!=0){
    int digit=x%10;
    x=x/10;
    val=val*10+digit;
}
if (-2^32-1<=val<=2^32-1)
    {
        return 0;
    }
if (check)
{
    val=-val;
}
return val;


}
  
};
int main(){

    solution sol;
    cout<<sol.reverse(-987)<<endl;
    return 0;
}