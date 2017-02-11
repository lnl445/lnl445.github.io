def calcTotalBeats(line, numEndBeats):                      #Add the prefix beats to the end phrase beats to get the total beats
    beats = numberPrefixBeats(line) + numEndBeats
    return beats

def numberPrefixBeats(line):                                #Find the number of prefix beats for a given line
    return int(line[1])
    
def numberEndingBeats(endPhrase, endings_file):             #Find the number of end phrase beats - given a phrase
    ending_file = open(endings_file, "r")
                                                            
    for end in ending_file:                                 #go through the ending_file
        end = end.strip();
        end = end.split("::");                              #strip and then split at the "::"
        
        endBeats = 0                                        #set the number of end phrase beats to 0
       
        if (endPhrase == end[0]):                           #find the phrase that matches the endPhrase in the endings_file 
            endBeats += int(end[2])                         #then count those beats and return the count
            return endBeats
        else:
            continue
    return endBeats                                         #if the end phrase is blank, return 0

def findRhythm(line, file_name):
    ending_file = open(file_name, "r")

    rhythm = ""                                             #create the rhyme variable

    for end in ending_file:                                 #go through the ending_file
        end = end.strip();
        end = end.split("::")                               #strip and then split at the "::"
    
        if(line[2] == end[0]):                              #find the phrase that matches the line's endPhrase in the endings_file
            rhythm = end[1]                                 #then save the corresponding rhythm
            return rhythm                                   #and return the rhythm
        else:
            continue
    return rhythm
       
    
def main():
    endings_file = open("endings.txt", "r");                                    #Open the file with the ending phrases
    skeleton_file = open("skeleton_SamuraiShowdown.txt", "r");                  #Open the file with the rap              
        
    skeleton_file_copy = open("skeleton_SamuraiShowdown.txt", "r");             #Make a copy of the rap file and 
    first_line = skeleton_file_copy.readline();                                 #read the first line of the file.
    first_line = first_line.strip();                                            #This is how we will start keeping track of previous lines.
    first_line = first_line.split("::")                                         #Create a list out of the line.


    #When reading the first line, the current line = previous line = first_Line
    current = first_line
    previous = current

   
    for line in skeleton_file:
        line = line.strip();
        line = line.split("::");                                                #split the lines of the rap file into lists

        #During the first iteration of the file, leave current line = previous line = first_Line 
        if current == first_line and previous == first_line and current == line:
            ending = current[2]
            
        #After the first iteration, reassign the current value that way the first_Line isn't repeated
        else:
            current =  line
            ending = current[2]
        
        #If the end of the line is complete, print it out
        if (ending != "XXX"):
            
            endWord = current[2]                                        #This is the end of the line 
            endingBeats = numberEndingBeats(endWord, "endings.txt")     #This is the number of ending beats in the current line
            totalPrevBeats = calcTotalBeats(current, endingBeats)       #Calculate the total number of beats in the current line


            #if it is blank,  return the first part of the current line. It is complete.
            if endWord == '':
                lyric =  current[0]
                print lyric
                
            #Otherwise, return the first and last parts of the current line.
            #Keep track of the current rhythm being followed
            else:
                rhythm = findRhythm(current, "endings.txt")
                print current[0] + " " + current[2]
                previous  = current                                     #the current line will now be used as a reference for the next line
          
        else:
            prefixBeats = numberPrefixBeats(current)                    #Calculate the number of current prefixBeats
            neededRhythm = findRhythm(previous, "endings.txt")          #Find the rhythm from the previous line containing the rhythm
            neededBeats = totalPrevBeats - prefixBeats                  #Calculate the number of neededBeats
          
            for end in endings_file:                                    #Go through the endings file
                end = end.strip();                      
                end = end.split("::");
                endWord = end[0]                                        #Locate the ending that follows the rhythm of the rap and                                             
                wordBeats = end[2]                                      #has the number of beats needed to complete the line   
                rhythm = end[1]
                if (int(wordBeats) == neededBeats) and (rhythm == neededRhythm):
                    print current[0] + " " + endWord                    #Once the ending is found, print the beginning of the line + endWord
                    line = [current[0],current[1],endWord]              #Rewrite the current line  that way the next line can refer to it
                    current = line
                    previous = current                                  #the current line will now be used as a reference for the next line
                    break
                else:
                    continue
        
                  
  
main()
