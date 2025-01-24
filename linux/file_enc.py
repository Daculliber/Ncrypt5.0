from cryptography.fernet import Fernet
from func import lst_about
from file_explore import explore
import os,time

def clear():
    os.system ('clear')

def gen_key():
	key = Fernet.generate_key()
	return key
def enc(inp,key):
	# using the generated key
	fernet = Fernet(key)
	# opening the original file to encrypt
	with open(inp, 'rb') as file:
		original = file.read()
		file.close
		
	# encrypting the file
	encrypted = fernet.encrypt(original)

	# opening the file in write mode and 
	# writing the encrypted data
	with open(inp, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)
		file.close
def dec(inp,key):
	# using the key
	fernet = Fernet(key)

	# opening the encrypted file
	with open(inp, 'rb') as enc_file:
		encrypted = enc_file.read()

	# decrypting the file
	decrypted = fernet.decrypt(encrypted)

	# opening the file in write mode and
	# writing the decrypted data
	with open(inp, 'wb') as dec_file:
		dec_file.write(decrypted)
def pin_enc(inp,key,pin):
	for i in range (pin):
		enc(inp,key)
def pin_dec(inp,key,pin):
	try: 
		for i in range(pin):
			dec(inp,key)
	except:
		print("Incorrect PIN")
		print("The file will be destroyed for safety.")
		print("You should know your PIN, and you should make backups.")
		a=open(inp,'w')
		a.write("The file was destroyed for safety reasons. But don't worry, you have a backup. Don't you?")
		a.close()
		time.sleep(1)
def keymanage(key):
	
	cmd=""
	while cmd!="back":
		clear()
		print('''===========================
	KEY MANAGER
===========================
Generate -------------(new)
Select ------------(select)
===========================
<--[back]
===========================''')
		cmd=lst_about(input(">> "),['new',"select","back"])
		if cmd==('new'):
			clear()
			key1=gen_key()
			filekey=open("newfilekey.nKey",'wb')
			filekey.write(key1)
			filekey.close()
			print("The key was created. Do you want to set it as default?")
			print("WARNING: This action will overwrite the default key.")
			a=input("Y/N")
			if a=='Y':
				filekey=open("default.nKey",'wb')
				filekey.write(key1)
				filekey.close()
				print("The key was set as default.")
			else: 
				print("The key was saved but will only be set as default for this session.")
				time.sleep(0.5)
			key=key1
		elif cmd=="select":
			file=explore(note="Select Key")
			filekey=open(file,'rb')
			key1=filekey.read()
			print("The key was set for this session. Do you want to set it as default?")
			print("WARNING: This action will overwrite the default key.")
			a=input("Y/N ")
			time.sleep(0.5)
			if a=='Y':
				filekey=open("default.nKey",'wb')
				filekey.write(key1)
				filekey.close()

				print("The key was set as default.")
				time.sleep(0.5)
			else: 
				print("The key will only be set as default for this session.")
				time.sleep(0.5)
			key=key1
		elif cmd=="back":
			pass
		else:
			print("Invalid command")
			time.sleep(0.5)
	return key






