import datetime
import hashlib
import pyDes
import time
import random
import string
from pymsgbox import *

plaintext='ibrahim'

cont = "y"
while cont.lower() == "y":
    print("Select operation\n1.Block Number\n")

    choice = input("Enter choice(1):")

    

    if choice == '1':

        # printing the start time  
        print("The time of code execution begin is : ", end ="") 
        print(time.ctime()) 

        password = input("Enter Password:")
        
        if plaintext == password:
             alert(text='Its hacked', title='BlockChain Secutrity', button='OK')
             
             print("Start of Hacking Time : ", end ="") 
             for remaining in range(300, 0, -1):
                 sys.stdout.write("\r")
                 sys.stdout.write("{:2d}.".format(remaining))
                 sys.stdout.flush()
                 time.sleep(1)
             print("End of Hacking Time: ", end ="") 
             print(time.ctime())
        else:
            alert(text='Its not hacked', title='BlockChain Secutrity', button='OK')
            

            
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
                return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(en_d)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(dec)+"\nDecript Delay: "+str(dec_time)+"\n--------------"
       
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

        for n in range(11):
            blockchain.mine(Block("Block " + str(n+1)))
 

       

    elif choice == '2':

       print("ibrahim")



    elif choice == '3':
       print("khalil")

    else:
       print("Invalid input")
    cont = input("Continue?y/n:")
    if cont == "n":
        break
