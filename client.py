#!/usr/bin/python
import socket
import sys
import random
import md5

def calculate_verify_hash(string, n):
    print("**********************")
    seed = hex(random.randint(0, 16777215))
    print("Seed: "+ seed) #random #string
    num = seed+string #seed|string-> str type
    print("Seed|String: " + num) #str
    m = md5.new()
    m.update(num)
    m.hexdigest()
    #print(m)
    hash_MD5 = m.hexdigest()[:32]
    print("Hash: " + hash_MD5)
    print("Primele 2n cifre din hash: " + hash_MD5[0:2*n])
    temp = ''
    if hash_MD5[0:2*n] == temp.zfill(2*n):
        check = 1;
    else:
        check = 0;
    print("Check: " + str(check))
    print("**********************")
    return check, seed, hash_MD5

# Create a UDP socket


server_address = ('localhost', 1400)
message = "hello"

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send data
    print >>sys.stderr, 'trimite mesaj "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'asteapta mesaj'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'a receptionat "%s"' % data
    data = data.split()
    n = int(data[0])
    sir = data[1]

    msg = "Nu s-a gasit seed-ul"
    while msg != "S-a gasit seedul":
        
        res = calculate_verify_hash(sir, n)
        check = res[0]
        seed = res[1]
        hash_MD5 = res[2]
        
        if check == 1:
            msg = "S-a gasit seedul"
            sent = sock.sendto("S-a gasit seedul" + seed, server_address)

            break
        else:
            sent = sock.sendto("Nu s-a gasit seedul", server_address)
        
        
except:
    print ("Nu s-a conectat. Mai incercati o data.")

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
