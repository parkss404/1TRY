#include <iostream>
using std::cout; using std::cin;
using std::string;
using namespace std;

string Food000[] = { "¥���","����" };
string Food001[] = { "����","���","�ø�","����","����","������ġ","�ұ���","�Ľ�Ÿ","�ܹ���" };
string Food010[] = { "����","�����","����","����","ġŲ","ȸ" };
string Food100[] = { "�ʶ�","�δ��","«��" };
string Food110[] = { "�߹�","�ߺ�����","���","�ſ�ġŲ","������","�Ʊ���","���" };
string Food101[] = { "������","�̸�","����ø�" };
string Food011[] = { "������","����","�Ұ���" };
string Food111[] = { "���庺��","�߰���","�޲ٹ�" };


int main() {
	char a;
	char b;
	char c;
	int st = 0;
	int nd = 0;
	int rd = 0;
	que1:												
	cout << "ȥ�� �޴��� ã���ó���?(O,X)" << endl;
	cin >> a;
	if (a == 'O') {
		st + 1;
		que2:
		cout << "�ſ� ������ �� ��ó���?(O,X)" << endl;
	}
	else if (a == 'X') {
		cout << "��� �ſ� ������ �� ��ó���?(O,X)" << endl;
	}
	else { goto que1; };
	cin >> b;
	if (b == 'O') {
		nd + 1;
		que3:
		cout << "�ſ� ����޴��� �԰��ͳ���?(O,X)" << endl;
	}
	else if (b == 'X') {
		cout << "�ȸſ� ����޴��� �԰��ͳ���?(O,X)" << endl;
	}
	else { goto que2; };
	cin >> c;
	if (c == 'O') {
		rd + 1;
	}
	else if (c == 'X') {
		goto next;
	}
	else { goto que3; };
}