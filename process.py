#Opening the file named "um-server-01.txt"
log_file = open("um-server-01.txt")


#Creating a function named "sales_reports" that takes in a paramater (log_file - the file opened previously)
def sales_reports(log_file):
    #Creating a for loop to loop over each line in opened file (um-server-01.txt)
    for line in log_file:
        #Using rstrip to remove white space at the end of each line
        line = line.rstrip()
        #Defining a variable to include data at a specific index in each line
        day = line[0:3]
        #Creating a function to return a specific day's orders
        if day == "Mon":
            #Returning the specified data in the terminal
            print(line)

#Calling the function created above
sales_reports(log_file)
