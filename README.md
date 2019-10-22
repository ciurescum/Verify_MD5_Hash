# Verify_MD5_Hash
Obiectiv:

Se vor crea 2 programe server.py si client.py care sa respecte conditiile urmatoare:

Programul  server  va  avea  ca  parametri  în  linia  de  comandă  un  număr n și  un șir  de  caractere string
(reprezentarea  text  a  unui  număr  hexazecimal  de  genul  A7C02215FC).  Alternativ,  dacă  se  apelează fără 
parametri, el va cere introducerea lui nși string.  Scopul va fi găsirea de către client a unei valori 
hexazecimale numite seed care, concatenată la începutul lui string exprimat în hexazecimal, să dea ca rezultat un 
hash de tip MD5 al numărului hexazecimal rezultat seed | string care să înceapă cu n octeți de valoare 00. Seed-ul 
va fi aflat prin incercari.

Clientul va folosi funcția md5.digest()  pentru  a calcula MD5-ul (hash-ul) de 16 octeți. Primul client care va găsi 
o soluție a problemei o va transmite la server si va comanda incetarea activitatii serverului cat si a celuilalt client.

Instructiuni:

Se va porni serverul cu sintaxa: python server.py 1 ab5
Se va porni clientul cu sintaxa: python client.py 127.0.0.1

Implementare:

In primul rand, am creat o functie care imi construieste si verifica hash-ul. Aceasta imi genereaza un seed random
si verifica daca aplicand acestuia impreuna cu stringul dat functia md5, va fi indeplinita conditia ca rezultatul sa
inceapa cu '00'*n. In functie de rezultat, variabila check va deveni 0 sau 1 (1 daca este indeplinita conditia, 0 altfel).
In final, functia de verificare si gasire seed va afisa seed-ul gasit, valoarea check-ului si valoarea returnata de functia md5.

Apoi clientul va trimite serverului un mesaj "hello" de recunoastere. Ulterior asteapta valorile pentru n si pentru string de la 
server si dupa ce le receptioneaza incepe gasirea seed-ului. Daca seed-ul a fost gasit, clientul va trimite un mesaj serverului de
tipul "Seed-ul a fost gasit" impreuna cu seedul gasit. Dupa accea, conexiunea cu socketul se va inchide.

Intre timp, serverul afiseaza mesaje de informare asupra starii programului si anume, daca s-a gasit sau nu seedul. La fiecare 1000
de incercari, serverul va afisa numarul de incercari facute pana in acel moment. La final, severul va afisa seedul gasit, numarul de
incercari efectuate pana la gasirea seedului si adresa clientului care a gasit seedul.
