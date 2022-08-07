#!/usr/bin/env python3


# Integer To String Converter Tool
# Learning Resources: https://www.pythonindo.com/fungsi-chr/
# Created On Sunday, August 7, 2022, 09:27 AM.
# Message: Keep Spirit and Don't Give Up


import os
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("cls")
	os.system("pip install tk")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("pip install tk")
	os.system("clear")
import tkinter
from tkinter import *


def Integer_To_String_Converter_Tool(Code_By="Ruben Leonardo Sigalingging"):
	Fungsi_Utama_Integer_To_String_Converter_Tool=tkinter.Tk()
	Fungsi_Utama_Integer_To_String_Converter_Tool.title("Integer To String Converter Tool")
	Fungsi_Utama_Integer_To_String_Converter_Tool.geometry("800x500")
	Fungsi_Utama_Integer_To_String_Converter_Tool.resizable(width=True,height=True)
	Fungsi_Utama_Integer_To_String_Converter_Tool.configure(bg="#000000",cursor="arrow")


	Label_Judul_Integer_To_String_Converter_Tool=tkinter.Label(Fungsi_Utama_Integer_To_String_Converter_Tool,anchor=tkinter.CENTER,bg="#008000",bd=2,cursor="pirate",font=("Ubuntu Condensed",33),fg="#ffffff",height=2,justify=tkinter.CENTER,text="Integer To String Converter Tool")
	Label_Judul_Integer_To_String_Converter_Tool.pack(expand=False,fill=tkinter.X,side=tkinter.TOP,padx=0,pady=0)


	Instruction=tkinter.Label(Fungsi_Utama_Integer_To_String_Converter_Tool,anchor=tkinter.CENTER,bg="#ffffff",bd=12,cursor="pirate",font=("Ubuntu Condensed",15),fg="#008b8b",justify=tkinter.CENTER,text="Input Integer Below!",width=18)
	Instruction.pack(expand=False,side=tkinter.TOP,padx=25,pady=25)


	Entry_Button=tkinter.Entry(Fungsi_Utama_Integer_To_String_Converter_Tool,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#008b8b",highlightcolor="#008000",justify=tkinter.CENTER,selectbackground="#008b8b",selectforeground="#ffffff",width=18)
	Entry_Button.pack(expand=False,side=tkinter.TOP,padx=25,pady=25)


	def Processor_Function(Code_By="Ruben Leonardo Sigalingging"):
		Get_Variable=Entry_Button.get()
		Get_Variable=int(Get_Variable)
		chr_function=chr(Get_Variable)
		Convert_Result_Label=tkinter.Label(Fungsi_Utama_Integer_To_String_Converter_Tool,anchor=tkinter.CENTER,bg="#008000",bd=12,cursor="pirate",font=("Ubuntu Condensed",15),fg="#ffffff",justify=tkinter.CENTER,width=18)
		Convert_Result_Label.configure(text="Result Of Conversion:\n"+str(chr_function))
		Convert_Result_Label.pack(expand=False,side=tkinter.TOP,padx=5,pady=5)


		print(f"\033[91mThe Result Of Converting Numbers \033[94m{Get_Variable} \033[91mIs: \033[92m{chr_function}\n")


	Click_Button=tkinter.Button(Fungsi_Utama_Integer_To_String_Converter_Tool,activebackground="#008b8b",activeforeground="#ffffff",bd=3,bg="#008000",fg="#ffffff",font=("Times New Roman",15),highlightcolor="#a9a9a9",justify=tkinter.CENTER,width=15,height=1,text="Click Here!",command=Processor_Function)
	Click_Button.pack(expand=False,side=tkinter.TOP,padx=15,pady=15)

	Fungsi_Utama_Integer_To_String_Converter_Tool.mainloop()
Integer_To_String_Converter_Tool()