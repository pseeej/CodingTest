#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    string tempstr = "";
    
    for(int i=0;i<new_id.length();i++){
        char temp = tolower(new_id[i]);
        if((temp>='a' && temp<='z') || (temp>='0' && temp<='9') ||
           (temp == '-') || (temp == '_') || (temp == '.'))
            tempstr+=(temp);
        if(temp == '.'){
            int j=0;
            while(tempstr[tempstr.length()-j-1]=='.'){
                j++;
            }
            string tempstr2 = "";
            for(int k=0;k<tempstr.length()-j;k++){
                tempstr2 += tempstr[k];
            }
            tempstr2+='.';
            tempstr = tempstr2;
        }
        if(tempstr[0] == '.')
            tempstr = "";
    }
    
    if(tempstr[tempstr.length()-1]=='.'){
        string tempstr2="";
        for(int i=0;i<tempstr.length()-1;i++){
            tempstr2+=tempstr[i];
        }
        tempstr = tempstr2;
    }
    
    if(tempstr.length()==0)
        tempstr = "a";

    if(tempstr.length()>=16){
        for(int i=0;i<=13;i++){
            answer += tempstr[i];
        }
        if(tempstr[14] != '.')
            answer += tempstr[14] ;
    }
    else if(tempstr.length()<=2){
        for(int i=tempstr.length()-1;i<2;i++){
            tempstr += tempstr[i];
        }
        answer = tempstr;
    }
    else
        answer = tempstr;
   
    
    return answer;
}
