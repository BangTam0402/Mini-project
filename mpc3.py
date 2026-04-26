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
def display_tickets(tickets):
    if not tickets:
        print("No tickets!")
        return

    print(f"{'ID':<10}{'Movie':<20}{'Customer':<15}{'Seat':<10}{'Price':<10}")
    print("-" * 65)

    for t in tickets:
        print(f"{t['id']:<10}{t['movie']:<20}{t['customer']:<15}{t['seat']:<10}{t['price']:<10}")
def search_ticket(tickets):
    keyword = input("Enter ID: ")

    for t in tickets:
        if t["id"] == keyword:
            print("Found:", t)
            return

    print("Not found!")
def sort_tickets(tickets):
    tickets.sort(key=lambda x: x["price"])
    print("Sorted by price successfully!")
    return tickets

def statistics(tickets):
    if not tickets:
        print("No data!")
        return

    total_tickets = len(tickets)
    total_money = sum(t["price"] for t in tickets)
    average_price = total_money / total_tickets

    print("Total tickets:", total_tickets)
    print("Total money:", total_money)
    print("Average price:", average_price)