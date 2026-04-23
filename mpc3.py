tickets = []
def display_menu():
    print("\n====== MOVIE BOOKING SYSTEM ======")
    print("1. Add Ticket")
    print("2. Display Tickets")
    print("3. Search Ticket")
    print("4. Sort Tickets")
    print("5. Statistics")
    print("6. Save to File")
    print("0. Exit")
def add_ticket(tickets):
    ticket_id = input("ID: ")

    # check duplicate
    for t in tickets:
        if t["id"] == ticket_id:
            print("ID already exists!")
            return tickets

    movie = input("Movie: ")
    customer = input("Customer: ")
    seat = input("Seat: ")

    try:
        price = float(input("Price: "))
        if price <= 0:
            print("Price must > 0")
            return tickets
    except:
        print("Invalid price!")
        return tickets

    tickets.append({
        "id": ticket_id,
        "movie": movie,
        "customer": customer,
        "seat": seat,
        "price": price
    })

    print("Added successfully!")
    return tickets