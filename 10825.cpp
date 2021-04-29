#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct student {
	string name;
	int kor, eng, math;
};

bool cmp(student a, student b) {
	if (a.kor == b.kor && a.eng == b.eng && a.math == b.math)
		return a.name < b.name;
	if (a.kor == b.kor && a.eng == b.eng)
		return a.math > b.math;
	if (a.kor == b.kor)
		return a.eng < b.eng;
	return a.kor > b.kor;

}

int main() {

	int N;
	cin >> N;

	vector<student> stu(N);
	for (int i = 0; i < N; i++) {
		cin >> stu[i].name >> stu[i].kor >> stu[i].eng >> stu[i].math;
	}

	sort(stu.begin(), stu.end(), cmp);
	for (int i = 0; i < N; i++)
		cout << stu[i].name <<  "\n";



	return 0;
}