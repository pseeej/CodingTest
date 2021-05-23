#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    int arr2[8] = { 2, 1, 2, 3, 2, 4, 2, 5 };
    int arr3[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

    vector<int> cnt(3);

    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == (i % 5) + 1)
            cnt[0]++;
        if (answers[i] == arr2[i % 8])
            cnt[1]++;
        if (answers[i] == arr3[i % 10])
            cnt[2]++;
    }

    int max = 0;
    for (int i = 0; i < cnt.size(); i++) {
        if (cnt[i] > max)
            max = cnt[i];
    }

    for (int i = 0; i < cnt.size(); i++) {
        if (cnt[i] == max)
            answer.push_back(i + 1);
    }


    return answer;
}
