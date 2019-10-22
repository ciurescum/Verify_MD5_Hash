#!/usr/bin/python
import socket
import sys




# Initialize port
server_address = ('localhost', 1400)
print >>sys.stderr, 'Serverul porneste la adresa %s pe portul %s' % server_address

try:
    mess=str(sys.argv[1])+" " + str(sys.argv[2])
except:
    n = raw_input("Introduceti numarul n: ")
    string = raw_input("Introduceti un string: ")
    mess = n + " " + string

print >>sys.stderr, '\n asteapta mesaj de la client'
count = 0
while True:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    
    data, address = sock.recvfrom(4096)
    
    #print >>sys.stderr,"a receptionat de la client %s" % data
    
    sent = sock.sendto(mess, address)
    
    stare, address = sock.recvfrom(4096)
    count = count +1
    
    #stare = stare.split()
    print stare

    if stare.startswith("S-a gasit"):
        print "Seed-ul a fost gasit "
        print "Seedul este", stare [15:]
        print "Seedul a fost gasit de clientul cu adresa", address[0]
        print "s-au facut pana acum " +str(count)+"incercari"
        sock.close()
        break
    else:
        print "Seedul nu a fost gasit"
        if count %1000==0:
            print "s-au facut pana acum " +str(count)+"incercari"