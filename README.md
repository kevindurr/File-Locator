# File Locator
A Python 2.7 program csfind.py to list the regular files in the directory specified as a command line argument. The program takes two options. Option -name <regex> causes the file names listed to match the regex pattern specified. Option -grep <regex> causes the program to search the contents of each file (that matches -name <regex> when specified), matching its text lines against the specified regex pattern. For each match found in the file, list the file pathname with line number andthe line that matches the regex pattern.
  
 
The bonus part of this assignment extends the program to recursively walk a directory tree to perform the matching and file listing.
