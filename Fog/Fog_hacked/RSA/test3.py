import datetime
import hashlib
import time
import random
import string
from pymsgbox import *
import re

from random import randint
from math import sqrt, ceil, log, floor

file2 = open("fog_blocks.txt","w")
file1 = open("hacked_block.txt","w")
file7 = open("Fog_Encryption_time.txt","w")
file8 = open("Fog_Decryption_time.txt","w")
def hello_printer(plaintext,choice):
    #plaintext='ibrahim'

     #These are the private keys the bank uses
    bankPrime1 = 6619319052850372576671203008980947142174030778088896832879139788043990604607
    bankPrime2 = 89981040860183284202926925086489690550566335265876097787978356913003610730551
    #This is the public key
    clientPrime1 = 0
    clientPrime2 = 0

    #FOR FUNCTIONALITY
    bankPrime = bankPrime1
    clientPrime = bankPrime2

    #Calculate modulus
    modulus = bankPrime * clientPrime

    #Calculate totient of modulus
    totient = (bankPrime - 1)*(clientPrime - 1)

    #Creates random numbers until it passes Euclid's algorithm with the GCD being 1 - coprime generator

    def XGCD(b, n):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
            q, b, n = b // n, n, b % n
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0

    while True:
        pubkeyexponent = randint(3, ceil(sqrt(totient)))
        gcd, prikeyexponent = XGCD(pubkeyexponent, totient)
        if prikeyexponent < 0:
            prikeyexponent += totient
        if gcd == 1:
            break

    #print("Totient n", totient)
    #print("Private Key d", prikeyexponent)
    #print("Public Key e", pubkeyexponent)
    #print("Modulus", modulus)
    #print()
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
                    encrypted = 0
                    for x in range(len(data)):
                        h = encrypted + (256**x) * ord(data[x])
                    #print(h)
 
                    networkmessage = pow(h, pubkeyexponent, modulus)
                    #print("The number message sent over the network to the bank is this:", networkmessage)
                    encryptedd = pow(networkmessage, prikeyexponent, modulus)
                    #print("The number message sent back to the client is this:", encryptedd)
                    length = ceil(log(encryptedd, 256))
                    en_time=time.perf_counter()
                if len(data)>0:
                    encrypted = 0
                    for x in range(len(data)):
                        encrypted += (256**x) * ord(data[x])
             
                    decrypted = ""
                    for x in range(length-1, -1, -1):
                        num = floor(encrypted / (256**x))
                        decrypted = chr(num) + decrypted
                        encrypted -= (num * (256**x))
                    print(decrypted)
                    dec_time=time.perf_counter()
                    
                    info = "Meet me tomorrow at 2pm with a bag of taka 2 lac near at BRAC BANK, Mtijheel Brance."
                    file1.write( "\nData Info: " + str(info))
                    file1.write( "\nBlock Hash: " + str(self.hash()))
                    file1.write( "\nBlockNo: " + str(self.blockNo))
                    file1.write( "\nBlock Data: " + str(self.data))
                    file1.write( "\nHashes: " + str(self.nonce))
                    file1.write( "\nEncrypted: "+ str(h))
                    file1.write( "\nEncrypet Delay time: "+str(en_time))
                    file1.write( "\nDecript: "+str(decrypted))
                    file1.write( "\nDecript Delay: "+str(dec_time))
                    file1.write( "\n--------------")
                    
                    file2.write( "\n-------Start-------")
                    file2.write( "\nData Info: " + str(info))
                    file2.write( "\nBlock Hash: " + str(self.hash()))
                    file2.write( "\nBlockNo: " + str(self.blockNo))
                    file2.write( "\nBlock Data: " + str(self.data))
                    file2.write( "\nHashes: " + str(self.nonce))
                    file2.write( "\nEncrypted: "+ str(h))
                    file2.write( "\nEncrypet Delay time: "+str(en_time))
                    file2.write( "\nDecript: "+str(decrypted))
                    file2.write( "\nDecript Delay: "+str(dec_time))
                    file2.write( "\n------End--------")
                    
                return "Data Info: " + str(info) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(h)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(decrypted)+"\nDecript Delay: "+str(dec_time)+"\n--------------"       
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

    #These are the private keys the bank uses
    bankPrime1 = 6619319052850372576671203008980947142174030778088896832879139788043990604607
    bankPrime2 = 89981040860183284202926925086489690550566335265876097787978356913003610730551
    #This is the public key
    clientPrime1 = 0
    clientPrime2 = 0

    #FOR FUNCTIONALITY
    bankPrime = bankPrime1
    clientPrime = bankPrime2

    #Calculate modulus
    modulus = bankPrime * clientPrime

    #Calculate totient of modulus
    totient = (bankPrime - 1)*(clientPrime - 1)

    #Creates random numbers until it passes Euclid's algorithm with the GCD being 1 - coprime generator

    def XGCD(b, n):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
            q, b, n = b // n, n, b % n
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0

    while True:
        pubkeyexponent = randint(3, ceil(sqrt(totient)))
        gcd, prikeyexponent = XGCD(pubkeyexponent, totient)
        if prikeyexponent < 0:
            prikeyexponent += totient
        if gcd == 1:
            break

    #print("Totient n", totient)
    #print("Private Key d", prikeyexponent)
    #print("Public Key e", pubkeyexponent)
    #print("Modulus", modulus)
    #print()
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
                encrypted = 0
                for x in range(len(data)):
                    h = encrypted + (256**x) * ord(data[x])
                    #print(h)

                networkmessage = pow(h, pubkeyexponent, modulus)
                #print("The number message sent over the network to the bank is this:", networkmessage)
                encryptedd = pow(networkmessage, prikeyexponent, modulus)
                #print("The number message sent back to the client is this:", encryptedd)
                length = ceil(log(encryptedd, 256))
                en_time=time.perf_counter()
            if len(data)>0:
                encrypted = 0
                for x in range(len(data)):
                    encrypted += (256**x) * ord(data[x])
                
                decrypted = ""
                for x in range(length-1, -1, -1):
                    num = floor(encrypted / (256**x))
                    decrypted = chr(num) + decrypted
                    encrypted -= (num * (256**x))
                print(decrypted)
                dec_time=time.perf_counter()
                info = "Meet me tomorrow at 2pm with a bag of taka 2 lac near at BRAC BANK, Mtijheel Brance."
                file2.write( "\nData Info: " + str(info))
                file2.write( "\nBlock Hash: " + str(self.hash()))
                file2.write( "\nBlockNo: " + str(self.blockNo))
                file2.write( "\nBlock Data: " + str(self.data))
                file2.write( "\nHashes: " + str(self.nonce))
                file2.write( "\nEncrypted: "+ str(h))
                file2.write( "\nEncrypet Delay time: "+str(en_time))
                file2.write( "\nDecript: "+str(decrypted))
                file2.write( "\nDecript Delay: "+str(dec_time))
                file2.write( "\n--------------")

                
                
                file7.write(str(en_time)+"\n")
                
                file8.write(str(dec_time)+"\n")
                
            return "Data Info: " + str(info) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nEncrypted: "+str(h)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(decrypted)+"\nDecript Delay: "+str(dec_time)+"\n--------------"
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
