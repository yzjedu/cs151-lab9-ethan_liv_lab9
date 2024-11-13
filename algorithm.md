# Algorithm Document

1. Get File Name from the User
- Purpose: To prompt the user to enter the file name that contains the list of attendees. 
- Name: get_filename 
- Parameters: None 
- Return: A file name, represented by a string. 
- Algorithm:
  1. Prompt the user to enter the filename. 
  1. Read the input from the user. 
  1. Return the file name that was entered. 

2. Read Names from File into a List
- Purpose: To read names from the specified file and store them in a list.
- Name: read_names_file
- Parameters: filename - a string representing the name of the file.
- Return: A list of names (each element is a string from the file).
- Algorithm:
  1. Open the file using the given filename. 
  2. Read each line in the file and strip any whitespace. 
  3. Append each cleaned name to a list. 
  4. Close the file. 
  5. Return the list of names. 

3. Format and Display the Seating Arrangement
- Purpose: To format and display the seating arrangement based on tables and seats. 
- Name: format_display_seat 
- Parameters: names - a list of attendee names. 
- Return: None. 
- Algorithm:
  1. Determine the number of tables by dividing the length of names by 5. 
  2. Loop over the names list, grouping each set of five names as one table. 
     3. For each table:
     - Print the table number. 
     - Loop through each name (up to five per table), displaying the seat number and guest’s name. 
     - Ensure output is formatted to include table and seat number.
  
4. Main Function
- Purpose: To control the flow of the program. 
- Name: main 
- Parameters: None. 
- Return: None. 
- Algorithm:
  1. Call get_filename to get the filename from the user. 
  2. Use read_names_file with the filename to read the names into a list. 
  3. Call format_display_seat with the list of names to display the seating arrangement.
