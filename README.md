# DNA_python


## About this project

 A program written in Python by CLI that receives a blood test with a sequence of nucleotides, and checks if there is someone with comparable blood in an SQLITE database;
 Inside the sequence folder, we have 20 blood tests with a sequence of
nucleotides. We will pass one of these files and a database to the program, then it will return to us if there is someone in the database that matches, then displaying the name;

### Exemple;
  The sequence chosen to analyze is the one below, and we pass it to program together with the database;
  
  sequence;
    AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATA
   CLI;
    `python dna.py databases/small.csv sequences/1.txt`
    
   Now the program will be executed, obtaining the database passed to it (SQlite), and will try to find someone who corresponds to the blood test, in this case,      'it will find and return the name 'Bob.
   
  More information, go to https://cs50.harvard.edu/x/2021/psets/6/dna/#:~:text=python%20dna.py%20databases/small.csv%20sequences/1.txt
    

