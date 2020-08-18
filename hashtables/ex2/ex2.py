#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    trip = {}

    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    route = [None]*len(tickets)
    index = 0
    look_ticket = trip["NONE"]

    while index < len(tickets):
        route[index] = look_ticket
        index += 1
        look_ticket = trip.get(look_ticket)
    
    # print(route)

    return route