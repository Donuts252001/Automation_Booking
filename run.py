from booking.bookings import Booking

# inst=Booking()
# inst.land()

# try: have an indent after this
with Booking() as inst:
        inst.land()
        inst.curr("USD")
        inst.going("New York")
        inst.when("2022-06-25","2022-06-30")
        inst.who(count=2)
        inst.search()
        inst.apply_filters()
        inst.report_class()
        # # print("exit")
        #after this out of indent
    #__exit__ will be called
# except Exception as e:
    # if "in Path" in str(e):
    #         print("Exception: " + str(e))
    #         print("Do the following")
    #         print("Windows:\n"
    #               "set PATH=%PATH%;C:path-of-driver\ \n "
    #               "Linux:\n"
    #               "PATH=$PATH:/path/toyour/folder/\n")
    # else:
    #     raise
    
