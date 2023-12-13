<h1 align="center"> Modified Vigenere Cypher </h1>
<p align="center">
I added the game of encrypting any message. The method used for encryption is not much known and described below.


Let the length of password (key) and message be whatever. For sake of simplicity , we assumed both to have just lower case alphabets ( 26 letters of english) in the game.

In the message , we will shift the letters by the number corresponding to letter in key.Understanding by example,

<b>message:</b> its the sample message for encryption<br>
<b>key:</b> hello

mapping for key : a -> 1  , b -> 2 , and so on till z -> 26

So the first letter of key is h , which is 8th letter of alphabet. So we will shift the first letter of message by 8 letters. So i will become q.  e is the 5th letter of alphabet. So t will become y. And so on.

So the encrypted message will be : qyaqebzqkzvoqyaqkzvonzvqkzvo  (spaces are not allowed in encrypted message)

This method is hard to crack and can not be decrypted by brute force method. The only way to decrypt is to know the key ( for small messages only). 

Long ago this method was actually used to encrypt messages but later it was cracked and new methods were developed. But the cracking algorithm was for long texts, short messages are fully protected.</p>
