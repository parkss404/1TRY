#include <iostream>
using std::cout; using std::cin;
using std::string;
using namespace std;

string Food000[] = { "짜장면","피자" };
string Food001[] = { "국밥","김밥","냉면","덮밥","만두","샌드위치","쌀국수","파스타","햄버거" };
string Food010[] = { "스시","내장류","보쌈","족발","치킨","회" };
string Food100[] = { "맵떡","부대찌개","짬뽕" };
string Food110[] = { "닭발","닭볶음탕","등갈비","매운치킨","불족발","아구찜","찜닭" };
string Food101[] = { "마라탕","쫄면","비빔냉면" };
string Food011[] = { "돈가스","삼겹살","불고기" };
string Food111[] = { "내장볶음","닭강정","쭈꾸미" };


int main() {
	char a;
	char b;
	char c;
	int st = 0;
	int nd = 0;
	int rd = 0;
	cout << "혼밥 메뉴를 찾으시나요?(O,X)" << endl;
	cin >> a;
	if (a == 'O') {
		st + 1;
		cout << "매운 음식을 잘 드시나요?(O,X)" << endl;
	}
	else if (a == 'X') {
		cout << "모두 매운 음식을 잘 드시나요?(O,X)" << endl;
	}
	cin >> b;
	if (b == 'O') {
		nd + 1;
		cout << "매운 고기메뉴가 먹고싶나요?(O,X)" << endl;
	}
	else if (b == 'X') {
		cout << "안매운 고기메뉴가 먹고싶나요?(O,X)" << endl;
	}
	cin >> c;
	if (c == 'O') {
		rd + 1;
	}
}