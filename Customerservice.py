service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add():
    while True:
        #get the users input for the problem, seperated by commas for the values.
        ticket_request = input("Enter 'display' to see current tickets, 'done' to quit, 'update' to update or enter customer name, issue, and status: ")
        new_ticket = ticket_request.split(",")

        #We only want to add three values for the new key in our dictionary
        if len(new_ticket) == 3:
            customer, issue, status = new_ticket
            new_id = f"Ticket{len(service_tickets) + 1:03}"

            #creating a new entry
            customer_info = {
                "Customer": customer.strip(),
                "Issue": issue.strip(),
                "Status": status.strip()
            }
        #adding the new entry to the dictionary
            service_tickets[new_id] = customer_info
    
            print("new ticket added successfully.")
        elif ticket_request == "update":
            update()
        elif ticket_request == "display":
            display_tickets()
        elif ticket_request == "done":
            break
        else:
            print("invalid input")
        
        print(service_tickets)
        


def update ():
    fixed = input(f"Enter ticket number of fixed issue: ")
    if fixed in service_tickets:
       value_update = input("Would you like to change the name, issue, or status?: ")
       if value_update.lower() == "name":
           new_name = input("Enter the new name: ")
           service_tickets[fixed]["Customer"] = new_name
       elif value_update.lower() == "issue":
           new_issue = input ("Enter new issue: ")
           service_tickets[fixed]["Issue"] = new_issue
       elif value_update.lower() == "status":
           new_status = input("Enter new status: ")
           service_tickets[fixed]["Status"] = new_status
       else:
           print("Ticket does not exist")
           
def display_tickets():
    if not service_tickets:
        print("No tickets")
    else:
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}")
            for key, value in ticket_info.items():
                print(f"{key}: {value}")
            print()
           
add()
