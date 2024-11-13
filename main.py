# Programmers: Ethan D'Souza & Liv Oakes
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/13/2024
# Lab Assignment: 09
# Problem Statement: Organize a dinner party with assigned seats by reading a list of attendees from a file, determining the number of tables needed (with each table seating 5 people), and displaying seat assignments for each table and seat.
# Data In: A filename provided by the user, which contains one attendee name per line.
# Data Out: Display the number of tables needed and formatted seating assignments for each guest, including table and seat numbers.

def get_filename():
    # Purpose: To prompt the user to enter the filename that contains the list of attendees.
    # Parameters: None
    # Return: A string representing the filename entered by the user.
    filename = input("Enter the filename with attendee names: ")
    return filename

def read_names_file(filename):
    # Purpose: To read names from the specified file and store them in a list.
    # Parameters: filename - a string representing the name of the file
    # Return: A list of names (each element is a string from the file).
    names = []
    try:
        file = open(filename, 'r')
        for line in file:
            names.append(line.strip())
        file.close()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    return names

def format_display_seat(names):
    # Purpose: To format and display the seating arrangement based on tables and seats.
    # Parameters: names - a list of attendee names
    # Return: None.
    table_count = len(names) // 5  # Each table seats 5 people
    for table in range(1, table_count + 1):
        print(f"Table {table}")
        for seat in range(1, 6):
            name_index = (table - 1) * 5 + (seat - 1)
            print(f"~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Table {table}, Seat {seat}, {names[name_index]}")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~")
        print()

def main():
    # Purpose: To control the flow of the program.
    # Parameters: None
    # Return: None.
    filename = get_filename()
    names = read_names_file(filename)
    if len(names) > 0:
        format_display_seat(names)

# Run the main function to start the program
main()
