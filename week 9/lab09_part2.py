# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''

output_file = open('words_updated.txt', 'w')



