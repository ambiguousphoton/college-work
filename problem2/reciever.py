class reciever:
    def recieve(payload):
        # print(payload)
        main_message = ""
        for i in payload:
            main_message += i.message
        print (main_message)