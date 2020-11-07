#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Reconstruct ticket order given array of ticket classes. Source is start,
        dest is end.

        First flight = source of None
        Final flight = destination of None

    Returns array of strings with entire route by airports.
    """
    # convert ticket list into a dictionary
    # set cur_flight to None
    # while x, find dest of cur_flight
        # add dest to flight_route  
        # add dest as cur_flight
    # return flight_route

    ticket_store = { ticket.source:ticket.destination for ticket in tickets }
    flight_route = []
    cur_flight = "NONE"
    cur_dest = ""

    while cur_dest is not "NONE":
        cur_dest = ticket_store[cur_flight]
        flight_route.append(cur_dest)
        cur_flight = cur_dest

    return flight_route
