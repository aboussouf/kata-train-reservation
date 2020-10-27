import cherrypy
import itertools


class BookingReferenceService:

    def __init__(self, starting_point):
        self.counter = itertools.count(starting_point)

    @cherrypy.expose()
    def booking_reference(self):
        next_number = next(self.counter)
        return str(hex(next_number))[2:]


# def main(args):
#     if args:
#         starting_point = int(args[0], 16) + 1
#     else:
#         starting_point = 123456789
#
#     cherrypy.config.update({"server.socket_port": 8082})
#     cherrypy.quickstart(BookingReferenceService(starting_point))


# if __name__ == "__main__":
#     import sys
#
#     help_text = """
# Use this program to start a booking reference service:
#
#     python3 {0}
#
# The service will start on this url:
#
#     http://localhost:8082/booking_reference
#
# If you have to restart the service, you can continue counting from the
# previous reference by passing it on the command line:
#
#     python3 {0} 75bcd15
#     """.format(sys.argv[0])
#     if "-help" in sys.argv or "--help" in sys.argv or "-h" in sys.argv:
#         print(help_text)
#     else:
#         main(sys.argv[1:])
