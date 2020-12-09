from sage.all import *
import hashlib
import hmac
from sage.crypto.mq.rijndael_gf import RijndaelGF
#reset()

q= random_prime(27)
F=GF(q)
g=F(2)

a= randint(1,q-1)
b= randint(1,q-1)

A=g**a
B=g**b

print "g=",g, ",q=",q ,"rand a=",a, ",A=",A, ",rand b=", b, ",B=",B, B**a, A**b

print "secreto compartido Incial", B**a

Kij=g**(a*b)
print "kij", Kij

hash1=hashlib.sha256()
hash1.update(str(Kij))
hash1.digest()
#hash_kij=int(hash1.hexdigest(),16)
hash_kij=hash1.hexdigest()
print "hash_kij = " , hash_kij

print ""
print "Mensaje 1"
print ""


rgf = RijndaelGF(4, 8)
plaintext = "00112233001122330011223300112233"
key=hash_kij
print "texto plano= ", plaintext 
print "texto cifrado="
mensajeCifrado=rgf.encrypt(plaintext, key)
print (mensajeCifrado)

a= randint(1,q-1)
print ("Ana envia nuevo aleatorio: " ,a, "y mensajeCifrado k1,1 : ", mensajeCifrado)
print "Beto Descifra el mensaje con k1,1 "

print "Descifrado"
print(rgf.decrypt(mensajeCifrado, key))

macUno=hashlib.sha256()
macUno.update(hash_kij)
macUno.digest()


macAna=hmac.new(macUno.hexdigest(), mensajeCifrado)
print "Mac ana"
print macAna.hexdigest()

print "Beto valida la autenticidad"
macValida = macAna.hexdigest()
hashTemp = hashlib.sha256()
hashTemp.update(key)
hashTemp.digest()
macCalculadoBero=hmac.new(hashTemp.hexdigest(),mensajeCifrado)


print macValida == macCalculadoBero.hexdigest()




print ""
print "Mensaje 2"
print ""


rgf = RijndaelGF(4, 8)
plaintext = "44556677445566774455667744556677"

Kij=g**(a*b)
print "kij=", Kij

key=hash_kij
print "texto plano= ", plaintext 
print "texto cifrado="
mensajeCifrado=rgf.encrypt(plaintext, key)
print (mensajeCifrado)

b= randint(1,q-1)
print ("Beto envia nuevo aleatorio: " ,b, "y mensajeCifrado k2,1 : ", mensajeCifrado)
print "Ana Descifra el mensaje con k2,1 "

print "Descifrado"
print(rgf.decrypt(mensajeCifrado, key))

macDos=hashlib.sha256()
macDos.update(hash_kij)
macDos.digest()


macBeto=hmac.new(macDos.hexdigest(), mensajeCifrado)
print "Mac Beto"
print macBeto.hexdigest()

print "Ana valida la autenticidad"
macValida = macBeto.hexdigest()
hashTemp = hashlib.sha256()
hashTemp.update(key)
hashTemp.digest()
macCalculadoBero=hmac.new(hashTemp.hexdigest(),mensajeCifrado)


print macValida == macCalculadoBero.hexdigest()


