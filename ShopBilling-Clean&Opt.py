from datetime import date
import os

class TheData:
	
	def __init__(self, ID, items):
		self.items = items
		self.userID = ID
	
	def userData(self):
		user = open("/storage/emulated/0/Program/shop/Users/{}/user_info.txt".format(self.userID),"+r").read().split()
		name = user[1]
		add = user[2]
		cont = user[3]
		return name, add, cont
	
	def tableData(self):
		list = []
		totalAmt = 0
		totalItem = 0
		n = open("Name.txt","+r").read().split()
		p = open("Price.txt","+r").read().split()
		for tuples in self.items:
			name = n[tuples[0]]
			price = p[tuples[0]]
			totalAmt += int(price)*int(tuples[2])
			totalItem += tuples[2]
			list +=  [(tuples[1], name, tuples[2], price, int(price)*int(tuples[2]))]
		return list, totalAmt, totalItem
		
	def printData(self):
		os.system("clear")
		a = TheData.userData(self)
		b = TheData.tableData(self)
		print(f"SN : {serialNumber()}\tNEW PURSE HOUSE")
		print("Sadar Market,09".rjust(31))
		print("Delhi, India".rjust(29))
		print(f"\nUser ID : {self.userID}")
		print(f"Customer : {a[0].title()} \t\tDate : {date.today()} ")
		print(f"Add. : {a[1].title()} ")
		print(f"Contact : {a[2]}\n")
		print("P.code\t","P.name\t","Quantity\t","Price\t","Amount\t")
		for d in b[0]:
			print(str(d[0])+"\t", str(d[1])+"\t",str(d[2])+"\t\t",str(d[3])+"\t",str(d[4])+"\t")
		print("Total"+"\t","\t",str(b[2])+"\t\t\t",str(b[1]))
		print(f"\nNet Amount : {b[1]}")
		print("\n\t**Thanks For Visiting**")
		
		TheData.storeData(self, d, a)

	def storeData(self, d, a):
		user = open("/storage/emulated/0/Program/shop/Users/{}/user_data.txt".format(self.userID),"+a")
		user.write("{},{},{},{},{},{}\n".format(date.today(), serialNumber(), d[0], d[1], d[2], d[3]))
		
		data = open("data.txt","+a")
		data.write("{},{},{},{},{},{},{}\n".format(date.today(), self.userID, a[0], d[0], d[1], d[2], d[3] ))


def serialNumber():
	data = open("data.txt","r")
	return len(data.readlines())
	data.close()

def newUser():
	print("old(o) / new(n) > ")
	if input("").lower() == "o":
		return False
	return True

def getUserID():
	if newUser():
		os.system("clear")
		name = input("Name > ") or "."*8
		add = input("Address > ") or "."*8
		contact = input("Contact > ") or "."*8
		userID = str(date.today().month)+str(date.today().day)+str(serialNumber())
		
		os.mkdir("/storage/emulated/0/Program/shop/Users/{}".format(userID))
		
		userinfo = open("/storage/emulated/0/Program/shop/Users/{}/user_info.txt".format(userID,),"+a")
		userinfo.write("{}\n{}\n{}\n{}\n".format(userID, name, add, contact))
			
		userdat = open("/storage/emulated/0/Program/shop/Users/{}/user_data.txt".format(userID),"a")
		userdat.write("Date,Bill. No,Code,Product,Qty,TP\n")
		userdat.close()
		
		return userID
	return input("User Id > ")

def getProduct():
	items = []
	cd = open("Code.txt","+r").read().split()
	while True:
		os.system("clear")
		code = input("Code > ") or "rb09"
		if code in cd:
			index = cd.index(code)
			qty = int(input("Quantity > ")) 
			items += [(index, code, qty)]
		elif code == "p":
			break
		else:
			print("sorry ! ")
	return items
		
user = TheData(getUserID(),getProduct())
user.printData()