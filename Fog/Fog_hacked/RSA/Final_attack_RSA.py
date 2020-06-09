import datetime
import hashlib
import time
import random 
import string
from pymsgbox import *
from random import randint
from math import sqrt, ceil, log, floor
plaintext='ibrahim'

cont = "y"
while cont.lower() == "y":
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

    print("Totient n", totient)
    print("Private Key d", prikeyexponent)
    print("Public Key e", pubkeyexponent)
    print("Modulus", modulus)
    print()
    
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
             print("Start of Hacking Time : ")
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
                #print(data)
                
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
                return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) +"\nMessage that Sent: "+str(networkmessage)+"\nEncrypted: "+str(h)+"\nEncrypet Delay time: "+str(en_time)+"\nDecript: "+str(decrypted)+"\nDecript Delay: "+str(dec_time)+"\n--------------"
       
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
