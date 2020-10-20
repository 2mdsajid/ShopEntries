import datetime
import time
import sys
import pandas as pd
import numpy as np


global code_list,qty_list,num_list,name_list,price_list,q,p,cus,sn_list,name,cus,add
code_list=[]
qty_list=[]
num_list = []
name_list = []
price_list =[ ]
#sn_list=[]
#for sn in range(len(price_list)):
#	sn_list.append(sn)
date = datetime.datetime.now().date()


def center(text, align):
	string = text
	new_string = string.center(align)
	print(new_string)
	

def clear():
    import os
    os.system( 'clear' )



def print_res():
	clear()
	#cus = "sajid"
#	add = "Nepal"
	q = np.array(qty_list)
	p = np.array(price_list)
	center("NEW PURSE HOUSE", 50)
	center("Sadar Market,09",49)
	center(" Delhi, India", 49)
	center("SN : .........",0)
	center(f"Customer : {cus} \t\tDate : {date} ",0)
	center(f"Add. : {add} ",0)
	center(f"Contact : ........ \n",0)
	df = pd.DataFrame({
	"P. Code":code_list,
	"Product ":name_list,
	"Quantity":qty_list,
	"Rate":price_list,
	"Amount": p*q })
	center(df.to_string(index=False),10)
	sum = df["Amount"].sum()
	center(f"\n\t\t\tTotal :      {sum}",10)
	exit()



def get_data():
	b_name = open("Name.txt","+r")
	b_price= open("Price.txt","+r")
	name = b_name.readlines()
	price = b_price.readlines()
	
	for el_num in num_list:
		name_list.append(name[el_num+1].strip())
		price_list.append(int(price[el_num+1].strip()))
	#print(name_list)
	
	print_res()



def get_index():
	b_code = open("Code.txt","+r")
	item_list = b_code.read().split()
	for el_code in code_list:
		num = item_list.index(el_code)
		num_list.append(int(num))
	#print(num_list)
	get_data()
		
		
		
def start():
	global name,cus,add
	cus = input("Customer name > ")
	add = input("Address > ")
	active=True
	while active:
		clear()
		c = input("code > ")
		if c == "e":
			active=False
		else:
			code_list.append(c)
			q = int(input("quantity > "))
			qty_list.append(q)
	#c = "a2"
#	q = 2
#	cus = "Sajid"
#	code_list.append(c)
#	qty_list.append(q)		
	get_index()
	
	
start()
