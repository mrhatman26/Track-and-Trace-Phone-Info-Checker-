import tkinter as t #Import tkinter and set it to t
from tkinter import messagebox as m #import the messagebox function from tkinter
import phonenumbers as p #import phonenumbers and set it to p
from phonenumbers import timezone, geocoder, carrier #import the timezone function from phonenumbers
def submit_button():#Defines the code run when the submit button is pressed
    suc_parse = True #Create a boolean var
    entered_text = entry_text_entry.get() #Get the text from the entry box
    entry_text_entry.delete(0, "end") #Delete the text in the entry box
    try: #Try to parse the number
        number_parse = p.parse(entered_text) #Set number_parse to hold the parsed information
    except: #If an exception is raised while parsing the number, it will instead do the following
        print("An error parsing the entered phone number has occured")
        m.showerror("Error", "Error: The phone number is either not international or invalid\n(Error Code: NUM_PARSE)") #Creates a dialogue box that tells the user there has been an error with an okay button
        suc_parse = False
    if suc_parse is True:
        print("Number:", number_parse)
        number_time = timezone.time_zones_for_number(number_parse) #Get the timezone for the number
        number_time_single = number_time[0] #Set number_time_single to the first value of the list of time zones
        print("Time Zone: ", number_time_single)
        number_car = carrier.name_for_number(number_parse, 'GB') #Get the number's carrier
        print("Carrier: ", number_car)
        number_loc = geocoder.description_for_number(number_parse, 'en') #Get the numbers location (Kinda creepy...)
        print("Location: ", number_loc)
        number_is_valid = str(p.is_valid_number(number_parse)) #Check if the number is a valid number
        print("Valid Number: ", number_is_valid)
        number_is_possible = str(p.is_possible_number(number_parse)) #Check if the number is possible
        print("Possible Number: ", number_is_possible)
        number_country_code = str(number_parse.country_code) #Get the country code and make it a string
        print("Country Code: ", number_country_code)
        output_textbox.configure(state="normal") #Sets the output text box to normal to allow it to be edited by the program
        output_textbox.delete("1.0", "end") #Delete all previous text from the text box
        output_textbox.insert("1.0", "Output:") #Print "Output:" at the start of the textbox
        output_textbox.insert("end", "\nNumber: " + entered_text) #Prints the variables at the end of the last line in the textbox
        output_textbox.insert("end", "\nLocation: " + number_loc) #Ditto
        output_textbox.insert("end", "\nCountry Code: " + number_country_code) #Ditto
        output_textbox.insert("end", "\nTime Zone: " + number_time_single) #Ditto
        output_textbox.insert("end", "\nCarrier: " + number_car) #Ditto
        output_textbox.insert("end", "\nValid Number: " + number_is_valid) #Ditto
        output_textbox.configure(state="disabled") #Sets the output text box to be disabled to prevent the user typing in it
    else:
        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end") #Ditto
        output_textbox.insert("1.0", "Output:") #Ditto
        output_textbox.insert("end", "\nError") #Ditto
        output_textbox.configure(state="disabled")
def clear_button(): #Defines the code run when the clear button is pressed
    output_textbox.delete("1.0", "end") #Ditto
    output_textbox.insert("1.0", "Output:") #Ditto
def exit_button(): #Defines the code run when the exit button is pressed
    window.destroy() #Exits the program
window = t.Tk() #Creates the window base
window.title("Track and Trace") #Sets the title of the window to "Track and Trace"
window.geometry("360x270") #Sets the size of the window to 360 pixels by 270 pixels
entry_frame = t.Frame(window) #Creates a frame to hold the entry widgets
entry_label = t.Label(entry_frame, text="Phone Number:").pack(fill=t.Y) #Creates a label that says "Phone Number: "
entry_button = t.Button(entry_frame, text="Submit", command=submit_button).pack(side=t.RIGHT, fill=t.Y, padx=5) #Creates a button that says "Submit", runs the submit_button() function and is positioned to the right with 5 pixels of padding
entry_text_entry = t.Entry(entry_frame) #Creates an entry box for the user to enter the phone number
entry_text_entry.pack(side=t.RIGHT, fill=t.Y) #Packs the entry box and positions it to the right
output_frame = t.Frame(window) #Creates a frame to hold the output widgets
output_textbox = t.Text(output_frame, height=7.5, width=32) #Creates the output text box
output_textbox.pack(side=t.TOP, fill=t.X) #Packs the output text box and positions it to the top
output_clearbutton = t.Button(output_frame, text="Clear", command = clear_button).pack(fill=t.X, pady=5) #Creates a button that says "Clear", runs the clear_button() function and is set to fill the X axis with 5 pixels of padding on the X axis
output_textbox.insert("1.0", "Output:") #Sets the text box to say "Output:"
output_textbox.configure(state="disabled")
output_exit_button = t.Button(output_frame, text="Exit", width=32, command = exit_button).pack(side=t.BOTTOM, fill=t.X) #Creates a button that says "Exit, runs the exit_button() function and is positioned to the bottom and set to fill the X axis
entry_frame.pack() #Packs the entry_frame frame
output_frame.pack(pady=5)
window.resizable(False, False)#Packs the output_frame frame
window.mainloop() #Runs the graphical user interface
