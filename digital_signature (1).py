# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:51:07 2020

@author: sayya
"""

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b'Message to be sent to Sayyad'
#hashing the message using SHA256
hash = SHA256.new(msg)

signer = PKCS115_SigScheme(keyPair)

#signing  the message which was hashed earlier
signature = signer.sign(hash)
print("Signature message:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'Message to be sent to Sayyad'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
   verifier.verify(hash, signature)
   print("Signature is valid.")
except:
   print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'incorrect message'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
   verifier.verify(hash, signature)
   print("Signature is valid.")
except:
   print("Signature is invalid.")
