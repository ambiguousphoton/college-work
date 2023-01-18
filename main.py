import sender 
snder  = sender.sender()
if __name__ == "__main__":   
    client_name = "LCO20377"
    data = "Ram  Nagar is located in Panchkula  District. it is about 12 km from Chandigarh."
    p_name = "Ram Nagar"
    sendr = snder
    print(len(data))
    sendr.send(data,p_name,client_name)


