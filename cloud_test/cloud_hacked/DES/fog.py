import datetime
import hashlib
import pyDes
import time
import random
import string
from pymsgbox import *

file2 = open("Fog_block.txt","w")
file1 = open("Hacked_block.txt","w")
file7 = open("Fog_encrypt.txt","w")
file8 = open("Fog_decrypt.txt","w")
def hello_printer(plaintext,choice):
    #plaintext='ibrahim'
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
                    file1.write( "\nData Info: " + str(info))
                    file1.write( "\nBlock Hash: " + str(self.hash()))
                    file1.write( "\nBlockNo: " + str(self.blockNo))
                    file1.write( "\nBlock Data: " + str(self.data))
                    file1.write( "\nHashes: " + str(self.nonce))
                    file1.write( "\nEncrypted: "+ str(en_d))
                    file1.write( "\nEncrypet Delay time: "+str(en_time)) 
                    file1.write( "\nDecript: "+str(dec_d))
                    file1.write( "\nDecript Delay: "+str(dec_time))
                    file1.write( "\n--------------")
                    file2.write( "\n-------Hacked Block Start-------")
                    file2.write( "\nData Info: " + str(info))
                    file2.write( "\nBlock Hash: " + str(self.hash()))
                    file2.write( "\nBlockNo: " + str(self.blockNo))
                    file2.write( "\nBlock Data: " + str(self.data))
                    file2.write( "\nHashes: " + str(self.nonce))
                    file2.write( "\nEncrypted: "+ str(en_d))
                    file2.write( "\nEncrypet Delay time: "+str(en_time)) 
                    file2.write( "\nDecript: "+str(dec_d))
                    file2.write( "\nDecript Delay: "+str(dec_time))
                    file2.write( "\n-------Hacked Block End-------")
                    
                return "Data Info: " + str(info) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(en_d)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(dec_d)+"\nDecript Delay: "+str(dec_time)+"\n--------------"       
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
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice ==2:
        for n in range(choice-1):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 3:
        for n in range(choice-2):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 4:
        for n in range(choice-3):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 5:
        for n in range(choice-4):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 6:
        for n in range(choice-5):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 7:
        for n in range(choice-6):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 8:
        for n in range(choice-7):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 9:
        for n in range(choice-8):
            blockchain.mine(Block("Block " + str(n+choice)))
    elif choice == 10:
        for n in range(choice-9):
            blockchain.mine(Block("Block " + str(n+choice)))
    else:
        for n in range(0):
            blockchain.mine(Block("Block " + str(n+0)))
    file1.close()
 
    
def hello_printerr(plaintext,choice):

    #plaintext = "Ibrahim"
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
                    
                info = "Meet me tomorrow at 2pm with a bag of taka 2 lac near at BRAC BANK, Mtijheel Brance."
                file2.write( "\nData Info: " + str(info))
                file2.write( "\nBlock Hash: " + str(self.hash()))
                file2.write( "\nBlockNo: " + str(self.blockNo))
                file2.write( "\nBlock Data: " + str(self.data))
                file2.write( "\nHashes: " + str(self.nonce))
                file2.write( "\nEncrypted: "+ str(en_d))
                file2.write( " Finish Time: "+str(en_time))
                file2.write( "\nDecript: "+str(dec_d))
                file2.write( "\nDecript Delay: "+str(dec_time))
                file2.write( "\n--------------")

                
                
                file7.write( "\n"+str(en_time))
                
                file8.write( "\n"+str(dec_time))
                
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
    file2.close()
    file7.close()
    file8.close()
