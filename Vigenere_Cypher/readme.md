<h1 align="centre"> Vigenere Cypher </h1>
<p align="centre" > This game uses the algorithm of Vigenere Cypher to encrypt and decrypt the message. This algorithm is described below.

The input key is supposed to be a 26 letters word ( with all 26 unique letters of english alphabet). The original 26 letters of english are written in a row and then the key is written below it (say in the form of double list). And then each letter in the text is replaced by the letter below it in the double list. Means, every a in the text will be replaced by the first letter in the key , every b in the text will be replaced by the second letter in the key and so on. 

For example,

<b> Message : </b> The quick brown fox jumps over the lazy dog <br>
<b> Key : </b> zyxwvutsrqponmlkjihgfedcba (say the key is letters in reverse order)

So every a in message will be replaced by z, every b in message will be replaced by y and so on.

<b> Encrypted message :</b> gsvjfrxpyildmulcqfnkhlevigsvozabwlt 


This method took decades to be cracked but the method to crack the message is only applicable on very large text. So encrypting small messages is safe. Using brute force will take canturies to crack the message.