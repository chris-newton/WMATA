# given our station, line, the direction we want to go, and the station the train is at, is the train still catchable at our station?
# returns bool
def is_catchable(our_station_id: str, line:str, direction: int, train_station_id: str):
    # if direction == 0, sequence of stops is from front to end of array, if == 1, it's from end to front
    # Start: Shady Grove | End: Glenmont
    RD = ["A15","A14","A13","A12","A11","A10","A09","A08","A07","A06","A05","A04","A03","A02","A01","B01","B02","B03","B35","B04","B05","B06","B07","B08","B09","B10","B11"]   
    # Start: Franconia Springfield | End: Downtown Largo
    BL = ["J03","J02","C13","C12","C11","C10","C09","C08","C07","C06","C05","C04","C03","C02","C01","D01","D02","D03","D04","D05","D06","D07","D08","G01","G02","G03","G04","G05"]
    # Start: Branch Ave | End: Greenbelt
    GR = ["F11","F10","F09","F08","F07","F06","F05","F04","F03","F02","F01","E01","E02","E03","E04","E05","E06","E07","E08","E09","E10"]

    try:
        rd_tr_i = RD.index(train_station_id)
        bl_tr_i = BL.index(train_station_id)
        gr_tr_i = GR.index(train_station_id)
        rd_our_i = RD.index(our_station_id)
        bl_our_i = BL.index(our_station_id)
        gr_our_i = GR.index(our_station_id)
    except:
        return False
        
    if direction == 0:
        
        if line == "RD":
            if RD.index(train_station_id) <= RD.index(our_station_id):
                return True
            else:
                return False
        elif line == "BL":
            if BL.index(train_station_id) <= BL.index(our_station_id):
                return True
            else:
                return False
        elif line == "GR":
            if GR.index(train_station_id) <= GR.index(our_station_id):
                return True
            else:
                return False
    else:
        if line == "RD":
            if RD.index(train_station_id) >= RD.index(our_station_id):
                return True
            else:
                return False
        elif line == "BL":
            if BL.index(train_station_id) >= BL.index(our_station_id):
                return True
            else:
                return False
        elif line == "GR":
            if GR.index(train_station_id) >= GR.index(our_station_id):
                return True
            else:
                return False

def stop_to_station(stop:str):
    station = ""

    if stop[0:3] == "STN":
        station = stop[4:]
        
    return station