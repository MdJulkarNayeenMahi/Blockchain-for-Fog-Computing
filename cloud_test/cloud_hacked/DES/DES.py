import datetime
import hashlib
import pyDes
import time
import random
import string
from pymsgbox import *
import fog
import re




file1 = open("Edge_hacked_block.txt","w")
file2 = open("Edge_hacked_encrypt.txt","w")
file12 = open("Edge_hacked_decrypt.txt","w")
file4 = open("Edge_Not_hacked_block.txt","w")
file5 = open("Edge_Not_hacked_encrypt.txt","w")
file6 = open("Edge_Not_hacked_decrypt.txt","w")

#plaintext='ibrahim'
print("Enter Your Alpha numeric password ....\n")

plaintext= input("Input your password: ")
x = True

while x:  
    if (len(plaintext)<6 or len(plaintext)>12):
        break
    elif not re.search("[a-z]",plaintext):
        break
    elif not re.search("[0-9]",plaintext):
        break
    elif not re.search("[A-Z]",plaintext):
        break
    elif not re.search("[!@$%^&*()_]",plaintext):
        break
    elif re.search("\s",plaintext):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
print("The password is : ",plaintext)


cont = "y"
while cont.lower() == "y":
    print("Select operation\nBlock Number\n")

    choice = int(input("Enter choice(1 to 10):"))

    

    if 0 < choice and choice <= 10:

        # printing the start time  
        print("The time of code execution begin is : ", end ="") 
        print(time.ctime()) 

        password = input("Enter Password:")
        
        if plaintext == password:
             alert(text='Its hacked', title='BlockChain Secutrity', button='OK')
             
             print("Start of Hacking Time : ")
             for remaining in range(300, 0, -1):
                 sys.stdout.write("\r")
                 sys.stdout.write("{:2d}.".format(remaining))
                 sys.stdout.flush()
                 time.sleep(1)
             print("End of Hacking Time: ")  
             print(time.ctime())
             print("##########################################Start#########################################")
             fog.hello_printer(plaintext,choice)
             
             print("######################################End#############################################")


             # using sleep() to hault the code execution 
             time.sleep(10)
            
      
             # printing the end time  
             print("The time of code execution end is : ", end ="") 
             print(time.ctime()) 
            
             class Block:
                 blockNo = 0
                 data = None
                 next = None
                 hash = None
                 nonce = 0
                 previous_hash = 0x0
                 timestamp = datetime.datetime.now()

                 def __init__(self, data):
                     self.data = data

                 def hash(self):
                     h = hashlib.sha256()
            
                     h.update(
                     str(self.nonce).encode('utf-8') +
                     str(self.data).encode('utf-8') +
                     str(self.previous_hash).encode('utf-8') +
                     str(self.timestamp).encode('utf-8') +
                     str(self.blockNo).encode('utf-8')
                     )
                     return h.hexdigest()
                 def __str__(self):
                    
                     data = ''.join([random.choice(plaintext+string.ascii_letters + string.digits+'!@#$%^*&( )_+}{'  ) for n in range(20)])
                     print(data)
                    
                     if len(data)>0:
                         en = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
                         en_d = en.encrypt(data)
                         en_time=time.perf_counter()
                     if len(data)>0:
                         dec = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
                         dec_d = dec.encrypt(data)
                         dec = dec.decrypt(dec_d)
                         dec_time=time.perf_counter()
                        
                         info = "Meet me tomorrow at 2pm with a bag of taka 2 lac near at BRAC BANK, Mtijheel Brance."
                         file1.write( "Data Info: " + str(info))
                         file1.write( "\nBlock Hash: " + str(self.hash()))
                         file1.write( "\nBlockNo: " + str(self.blockNo))
                         file1.write( "\nBlock Data: " + str(self.data))
                         file1.write( "\nHashes: " + str(self.nonce))
                         file1.write( "\nEncrypted: "+ str(en_d))
                         file1.write( "\nEncrypet Delay time: "+str(en_time))
                         file1.write( "\nDecript: "+str(dec_d))
                         file1.write( "\nDecript Delay: "+str(dec_time))
                         file1.write( "\n--------------")

                         
                         file2.write(str(en_time)+"\n")
                        
                         file12.write(str(dec_time)+"\n")
                         
                        
                        
                     return "Data Info: " + str(info) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(en_d)+"\nEncrypet Delay time: "+" Start Time: "+str(en_time)+"\nDecript: "+str(dec_d)+"\nDecript Delay: "+str(dec_time)+"\n--------------"
                       
             class Blockchain:
                 diff = 20
                 maxNonce = 2**32
                 target = 2 ** (256-diff)
                 block = Block("Genesis")
                 dummy = head = block

                 def add(self, block):
                     block.previous_hash = self.block.hash()
                     block.blockNo = self.block.blockNo + 1

                     self.block.next = block
                     self.block = self.block.next

                 def mine(self, block):
                     for n in range(self.maxNonce):
                         if int(block.hash(), 16) <= self.target:
                             self.add(block)
                             print(block)
                             break
                         else:
                             block.nonce += choice

             blockchain = Blockchain()
             if choice ==1:
                 for n in range(choice):
                     blockchain.mine(Block("Block " + str(n+1)))
                 for n in range(10-1):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice ==2:
                 for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                 for n in range(10-2):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice ==3:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-3):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 4:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-4):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 5:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-5):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 6:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-6):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 7:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-7):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 8:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-8):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 9:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-9):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             elif choice == 10:
                  for n in range(choice-1):
                     blockchain.mine(Block("Block " + str(n+1)))
                  for n in range(10-10):
                     blockchain.mine(Block("Block " + str(n+choice+1)))
             
             file1.close()
             file2.close()
             file12.close()
             print("####################################\n")
             nun = input("If want to See Hacked Block yes/no: ")

             if nun == "yes":
                 print("##########################################Start#########################################\n")
                 hacking_time=time.perf_counter()
                 print("\nhacking execution Time: ")
                 print(hacking_time)
                
                 file11 = open("Hacked_block.txt","r") 
                 
                 print (file11.read())
                 
                 file11.close()
               
                 print("####################################\n")
                 fog.hello_printerr(plaintext,choice)
                 print("######################################End##############################################\n")
             elif nun == "no":
                 break
             else:
                 print("Invalid Input")

        else:
            alert(text='Its not hacked', title='BlockChain Secutrity', button='OK')
            class Block:
                blockNo = 0
                data = None
                next = None
                hash = None
                nonce = 0
                previous_hash = 0x0
                timestamp = datetime.datetime.now()

                def __init__(self, data):
                    self.data = data

                def hash(self):
                    h = hashlib.sha512()
                    
                    h.update(
                    str(self.nonce).encode('utf-8') +
                    str(self.data).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8') +
                    str(self.timestamp).encode('utf-8') +
                    str(self.blockNo).encode('utf-8')
                    )
                    return h.hexdigest()
                def __str__(self):
                    data = ''.join([random.choice(plaintext+string.ascii_letters + string.digits+'!@#$%^*&( )_+}{'  ) for n in range(20)])
                    print(data)
                            
                    if len(data)>0:
                        en = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
                        en_d = en.encrypt(data)
                        en_time=time.perf_counter()
                    if len(data)>0:
                        dec = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
                        dec_d = dec.encrypt(data)
                        dec = dec.decrypt(dec_d)
                        dec_time=time.perf_counter()
                        
                        file4.write( "\nBlock Hash: " + str(self.hash()))
                        file4.write( "\nBlockNo: " + str(self.blockNo))
                        file4.write( "\nBlock Data: " + str(self.data))
                        file4.write( "\nHashes: " + str(self.nonce))
                        file4.write( "\nEncrypted: "+ str(en_d))
                        file4.write( " Finish Time: "+str(en_time))
                        file4.write( "\nDecript: "+str(dec_d))
                        file4.write( "\nDecript Delay: "+str(dec_time))
                        file4.write( "\n--------------")

                        file5.write(str(en_time)+ "\n")
                
                        file6.write(str(dec_time)+"\n")
                            
                        info = "Meet me tomorrow at 2pm with a bag of taka 2 lac near at BRAC BANK, Mtijheel Brance."
                        
                    return "Data Info: " + str(info) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(en_d)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(dec_d)+"\nDecript Delay: "+str(dec_time)+"\n--------------"
            class Blockchain:
                diff = 20
                maxNonce = 2**512
                target = 2 ** (512-diff)
                block = Block("Genesis")
                dummy = head = block

                def add(self, block):
                    block.previous_hash = self.block.hash()
                    block.blockNo = self.block.blockNo + 1

                    self.block.next = block
                    self.block = self.block.next

                def mine(self, block):
                    for n in range(self.maxNonce):
                        if int(block.hash(), 16) <= self.target:
                            self.add(block)
                            print(block)
                            break
                        else:
                            block.nonce += 1

            blockchain = Blockchain()
            for n in range(10):
                blockchain.mine(Block("Block " + str(n+1)))

            
            file4.close()
            file5.close()
            file6.close()
           
           

    elif choice == '2':

       print("ibrahim")



    elif choice == '3':
       print("khalil")

    else:
       print("Invalid input")
    cont = input("Continue?y/n:")
    if cont == "n":
        break
