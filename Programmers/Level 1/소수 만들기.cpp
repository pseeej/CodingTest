#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
    int answer = 0;
    
    vector<int> temp;

    for(int i=0;i<nums.size()-2;i++){
        for(int j=i+1;j<nums.size()-1;j++){
            for(int k=j+1;k<nums.size();k++){
                int num = nums[i]+nums[j]+nums[k];
                // int check = 1;
                // for(int l=0;l<temp.size();l++){
                //     if(num==temp[l]){
                //         check=0;
                //         break;
                //     }
                // }
                // if(check==1)
                    temp.push_back(num);
            }
        }
    }

    for(int i=0;i<temp.size();i++){
        int checkif=1;
        for(int j=2;j<temp[i];j++){
            if(temp[i]%j==0){
                checkif = 0;
                break;
            }
        }
        if(checkif == 1)
            answer++;
    }
    
    return answer;
}
