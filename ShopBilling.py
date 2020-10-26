from datetime import date
import time
import sys
import pandas as pd
import numpy as np
import inflect
import os

global code_list,qty_list,num_list,name_list,price_list,q,p,cus,sn_list, id_list,id,us,user_list
code_list=[]
qty_list=[]
num_list = []
name_list = []
price_list =[ ]
id_list = []
user_list =[]
date = date.today()

def words(num):
	p = inflect.engine()
	print(f"In words : {p.number_to_words(num)}")

def center(text, align):
	string = text
	new_string = string.center(align)
	print(new_string)
	
def clear():
    import os
    os.system( 'clear' )

def store():
	if type == "n" or type == "" :
			os.mkdir("/storage/emulated/0/Program/shop/Users/{}".format(user_id))
			
			userinfo = open("/storage/emulated/0/Program/shop/Users/{}/user_info.txt".format(user_id,),"+a")
			userinfo.write("{}\n{}\n{}\n{}\n".format(user_id,cus,add,con))
			
			userdat = open("/storage/emulated/0/Program/shop/Users/{}/user_data.txt".format(user_id),"a")
			userdat.write("Date,Bill. No,Code,Product,Qty,TP\n")
			userdat.close()

	for elc,elq,eln,elp in zip(code_list,qty_list,name_list,price_list):
		data = open("data.txt","+a")
		data.write("{},{},{},{},{},{},{}\n".format(date,user_id,cus,elc,eln,elq,elp,))
		
		if type == "n" or type == "" :
			
			user = open("/storage/emulated/0/Program/shop/Users/{}/user_data.txt".format(user_id),"+a")
			user.write("{},{},{},{},{},{}\n".format(date,sn,elc,eln,elq,elp))

		else:
			user = open("/storage/emulated/0/Program/shop/Users/{}/user_data.txt".format(user_id),"+a")
			user.write("{},{},{},{},{},{}\n".format(date,sn,elc,eln,elq,elp))		
store()



def customer_data():
	global defaults,sn,user_id,cus,add,con
	if type == "o":
		user = open("/storage/emulated/0/Program/shop/Users/{}/user_info.txt".format(user_id),"+r")
		dat = user.readlines()
		cus = dat[1].strip()
		add = dat[2].strip()
		con = dat[3].strip()
	else:		
		defaults = {"customer":".......",
		"address":"......",
		"contact":"......."}
		data = open("data.txt","r")
		sn = len(data.readlines())
		data.close()	
		user_id = str(date.month)+str(date.day)+str(sn)
		user_list.append(user_id)		
customer_data()


def print_res():
	global dis
	dis = int(input("Discount > "))
	clear()
	q = np.array(qty_list)
	p = np.array(price_list)
	center(f"SN : {sn}\t\t NEW PURSE HOUSE", 0)
	center("Sadar Market,09",49)
	center(" Delhi, India", 49)
	center(f"User ID : {user_id}",0)
	center(f"Customer : {cus} \tDate : {date} ",0)
	center(f"Add. : {add} ",0)
	center(f"Contact : {con}\n",0)
	df = pd.DataFrame({
	"P.Code":code_list,
	"P.Name":name_list,
	"Qty":qty_list,
	"Rate":price_list,
	"Amount": p*q })
	
	#adding last row for total
	sum = df["Amount"].sum()
	sum_qty = df["Qty"].sum()
	net = sum-(dis/100*sum)
	df = df.append({
	"P.Code":"",
	"P.Name":"", 
	"Qty":"",
	"Rate":"",
	"Amount":"" }, ignore_index=True)
	
	df = df.append({
	"P.Code":"Total",
	"P.Name":"", 
	"Qty":sum_qty,
	"Rate":"",
	"Amount":sum }, ignore_index=True)
	
	center(df.to_string(index=False),10)
	print(f"\nDiscout : {dis}%")
	print(f"Net Amount : {net}")
	words(net)
	print("\n\t**Thanks For Visiting**")
	store()
	
	exit()


def get_data():
	b_name = open("Name.txt","+r")
	b_price= open("Price.txt","+r")
	name = b_name.readlines()
	price = b_price.readlines()
	
	for el_num in num_list:
		name_list.append(name[el_num+1].strip())
		price_list.append(int(price[el_num+1].strip()))
	print_res()


def get_index():
	b_code = open("Code.txt","+r")
	item_list = b_code.read().split()
	for el_code in code_list:
		if el_code in item_list:
			num = item_list.index(el_code)
			num_list.append(int(num))
		else:
			continue
	get_data()


def items():
	active=True
	while active:
		clear()
		c = input("code > ")
		if c == "p":
			active=False
		else:
			b_code = open("Code.txt","+r")
			item_list = b_code.read().split()
			if c in item_list:
				code_list.append(c)
				while True:
					q = input("quantity > ")
					if q.isdigit():
						qty_list.append(int(q))
						break
					else:
						print("Input a number ! \n")
						continue
					
				
	get_index()


def start():
	global name,cus,add,con,type,user_id
	type = input("New or Old > ")
	if type.lower() == "o":
		user_id = input("User ID > ")
		customer_data()
		items()
		
	elif type.lower() == "n" or type == "":		
		cus = input("Customer name > ")
		add = input("Address > ")
		con = input("Contact > ")
		
		if cus == "":
			cus = defaults.get("customer")
		if add == "":
			add = defaults.get("address")
		if con == "":
			con = defaults.get("contact")
		items()
	
		
#	c = "a3"
#	q = 2
#	cus = "..."
#	add = "..."
#	con = "..."
#	code_list.append(c)
#	qty_list.append(q)		
#	get_index()
	
	
start()
