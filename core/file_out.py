#!/usr/bin/env python
'''
OWASP ZSC | ZCR Shellcoder
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/Ali-Razmjoo/OWASP-ZSC
http://api.z3r0d4y.com/
https://groups.google.com/d/forum/owasp-zsc [ owasp-zsc[at]googlegroups[dot]com ]
'''
from core.alert import *

def file_output(target, func, data, os, encode, shellcode, shellcode_op):
	args="1"
	for value in data:
		if args=="":
			args=value
		else:
			args+="', '"+value			
	fileout=open(target, 'w')
	file_output='''#include <stdio.h>
#include <string.h>
/*
This shellcode generated by OWASP ZSC
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
http://zsc.z3r0d4y.com/
owasp-zsc[at]googlegroups[dot]com

Title: %s('%s')
OS: %s
Encode: %s
Length: %s
Assembly code:\n
%s



compile example: gcc -ggdb -static -m32 -fno-stack-protector -z execstack -mpreferred-stack-boundary=2 -o shellcode_compiled %s
followed by(to run): ./shellcode_compiled
*/
\n\n
char *shellcode = "%s";
int main(void)
{
	(*(void(*)()) shellcode)();
	return 0;
}
'''%(func, args, os, encode, str(len(shellcode_op) / 4), shellcode, target, shellcode_op)
	fileout.write(file_output)
	fileout.close()
	info('File saved as %s .\n'%target)

def downloaded_file_output(target, data):
	fileout=open(target, 'w')
	fileout.write(data)
	fileout.close()
	info('File saved as %s . \n'%target)

						
