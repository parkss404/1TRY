#include <iostream>
#include <initializer_list>
using std::cout; using std::cin;
using std::string;
using namespace std;

string Food000[] = { "¥���","����" };
string Food001[] = { "����","���","�ø�","����","����","������ġ","�ұ���","�Ľ�Ÿ","�ܹ���" };
string Food010[] = { "����","�����","����","����","ġŲ","ȸ" };
string Food100[] = { "�ʶ�","�δ��","«��" };
string Food110[] = { "�߹�","�ߺ�����","���","�ſ�ġŲ","������","�Ʊ���","���" };
string Food101[] = { "������","�̸�","����ø�" };
string Food011[] = { "������","����","�Ұ��" };
string Food111[] = { "���庺��","�߰���","�޲ٹ�" };


int main() {

	char a;
	char b;
	char c;
	char last;
	int len;
	int st = 0;
	int nd = 0;
	int rd = 0;

	que1:												//üũ����Ʈ ����
	cout << "ȥ�� �޴��� ã���ó���?(O,X)" << endl;
	cin >> a;
	if (a == 'O') {
		st + 1;
		cout << "�ſ� ������ �� ��ó���?(O,X)" << endl;
	}
	else if (a == 'X') {
		cout << "��� �ſ� ������ �� ��ó���?(O,X)" << endl;
	}
	else { goto que1; };								//üũ����Ʈ�� ���ư���
	cin >> b;
	if (b == 'O') {
		nd + 1;
		cout << "�ſ� ���޴��� �԰�ͳ���?(O,X)" << endl;
	}
	else if (b == 'X') {
		cout << "�ȸſ� ���޴��� �԰�ͳ���?(O,X)" << endl;
	}
	cin >> c;
	if (c == 'O') {
		rd + 1;
	}
	if (st == 0 && nd == 0 && rd == 0) {
		len = sizeof(Food000) / sizeof(string);
		cout << "����� ��õ�޴���" << Food000[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 0 && nd == 0 && rd == 1) {
		len = sizeof(Food001) / sizeof(string);
		cout << "����� ��õ�޴���" << Food001[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 0 && nd == 1 && rd == 0) {
		len = sizeof(Food010) / sizeof(string);
		cout << "����� ��õ�޴���" << Food010[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 1 && nd == 0 && rd == 0) {
		len = sizeof(Food100) / sizeof(string);
		cout << "����� ��õ�޴���" << Food100[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 0 && nd == 1 && rd == 1) {
		len = sizeof(Food011) / sizeof(string);
		cout << "����� ��õ�޴���" << Food011[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 1 && nd == 0 && rd == 1) {
		len = sizeof(Food101) / sizeof(string);
		cout << "����� ��õ�޴���" << Food101[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 1 && nd == 1 && rd == 0) {
		len = sizeof(Food110) / sizeof(string);
		cout << "����� ��õ�޴���" << Food110[rand() % len] << "�Դϴ�." << endl;
	}
	else if (st == 1 && nd == 1 && rd == 1) {
		len = sizeof(Food111) / sizeof(string);
		cout << "����� ��õ�޴���" << Food111[rand() % len] << "�Դϴ�." << endl;
	}
}