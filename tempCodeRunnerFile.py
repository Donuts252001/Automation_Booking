from booking.bookings import Booking

# inst=Booking()
# inst.land()


with Booking() as inst:
    inst.land()