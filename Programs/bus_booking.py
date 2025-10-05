import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('bus_booking.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Buses
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   source TEXT, destination TEXT, departure_date TEXT, seats_available INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   bus_id INTEGER, passenger_name TEXT, seat_number INTEGER)''')

# Initialize tkinter
root = tk.Tk()
root.title("Online Bus Booking System")

# Functions for database operations
def search_buses():
    # Implement logic to search buses in the database
    pass

def book_ticket():
    # Implement logic to book a ticket and update the database
    pass

def view_bookings():
    # Implement logic to retrieve and display user bookings from the database
    pass

# GUI elements
label = tk.Label(root, text="Online Bus Booking System", font=("Arial", 18))
label.pack(pady=20)

search_button = tk.Button(root, text="Search Buses", command=search_buses)
search_button.pack()

book_button = tk.Button(root, text="Book Ticket", command=book_ticket)
book_button.pack()

view_button = tk.Button(root, text="View Bookings", command=view_bookings)
view_button.pack()

# Start the tkinter main loop
root.mainloop()

# Close the database connection after the application is closed
conn.close()
