import blpapi
import json

wpop={'samoa': 'WPOPSAMO Index', 'cayman islands': 'WPOPCAYM Index', 'azerbaijan': 'WPOPAZER Index', 'uzbekistan': 'WPOPUZBE Index', 'senegal': 'WPOPSENE Index', 'malta': 'WPOPMALT Index', 'japan': 'WPOPJAPA Index', 'taiwan': 'WPOPTAIW Index', 'cyprus': 'WPOPCYPR Index', 'barbados': 'WPOPBARB Index', 'lithuania': 'WPOPLITH Index', 'mongolia': 'WPOPMONG Index', 'united kingdom': 'WPOPUK Index', 'egypt': 'WPOPEGYP Index', 'rwanda': 'WPOPRWAN Index', 'puerto rico': 'WPOPPUER Index', 'argentina': 'WPOPARGE Index', 'norway': 'WPOPNORW Index', 'sierra leone': 'WPOPSIER Index', 'somalia': 'WPOPSOMA Index', 'bahrain': 'WPOPBAHR Index', 'belarus': 'WPOPBELA Index', 'cuba': 'WPOPCUBA Index', 'zambia': 'WPOPZAMB Index', 'guatemala': 'WPOPGUAT Index', 'zimbabwe': 'WPOPZIMB Index', 'belgium': 'WPOPBELG Index', 'haiti': 'WPOPHAIT Index', 'kazakhstan': 'WPOPKAZA Index', 'burkina faso': 'WPOPBURK Index', 'kyrgyzstan': 'WPOPKYRG Index', 'netherlands': 'WPOPNETH Index', 'bosnia': 'WPOPBOSN Index', 'denmark': 'WPOPDENM Index', 'philippines': 'WPOPPHIL Index', 'moldova': 'WPOPMOLD Index', 'emu': 'WPOPEMU Index', 'latvia': 'WPOPLATV Index', 'croatia': 'WPOPHR Index', 'switzerland': 'WPOPSWIT Index', 'bulgaria': 'WPOPBULG Index', 'jamaica': 'WPOPJAMA Index', 'albania': 'WPOPALBA Index', 'angola': 'WPOPANGO Index', 'ivory coast': 'WPOPIVOR Index', 'trinidad & tobago': 'WPOPTRIN Index', 'lebanon': 'WPOPLEBA Index', 'malaysia': 'WPOPMALA Index', 'mozambique': 'WPOPMOZA Index', 'greece': 'WPOPGREE Index', 'nicaragua': 'WPOPNICA Index', 'niger': 'WPOPNIGR Index', 'canada': 'WPOPCANA Index', 'qatar': 'WPOPQUAT Index', 'turkmenistan': 'WPOPTRKM Index', 'sudan': 'WPOPSUDA Index', 'fiji': 'WPOPFIJI Index', 'panama': 'WPOPPANA Index', 'nepal': 'WPOPNEPA Index', 'luxembourg': 'WPOPLUXE Index', 'swaziland': 'WPOPSWAZ Index', 'cook islands': 'WPOPCOOK Index', 'namibia': 'WPOPNAMI Index', 'venezuela': 'WPOPVENE Index', 'brunei': 'WPOPBRUN Index', 'iran': 'WPOPIRAN Index', 'united arab emirates': 'WPOPUAE Index', 'mali': 'WPOPMALI Index', 'madagascar': 'WPOPMADA Index', 'sri lanka': 'WPOPSRIL Index', 'china': 'WPOPCHIN Index', 'armenia': 'WPOPARME Index', 'thailand': 'WPOPTHAI Index', 'belize': 'WPOPBELI Index', 'ukraine': 'WPOPUKRA Index', 'yemen': 'WPOPYEME Index', 'libya': 'WPOPLIBY Index', 'gambia': 'WPOPGAMB Index', 'finland': 'WPOPFINL Index', 'macedonia': 'WPOPMACE Index', 'mauritius': 'WPOPMAUR Index', 'estonia': 'WPOPESTO Index', 'syria': 'WPOPSYRI Index', 'dominican republic': 'WPOPDREP Index', 'pakistan': 'WPOPPAKI Index', 'romania': 'WPOPROMA Index', 'seychelles': 'WPOPSEYC Index', 'czech republic': 'WPOPCZEC Index', 'tunisia': 'WPOPTUNI Index', 'guam': 'WPOPGUAM Index', 'united states': 'WPOPUS Index', 'austria': 'WPOPAUST Index', 'congo': 'WPOPCONG Index', 'hungary': 'WPOPHUNG Index', 'colombia': 'WPOPCOLO Index', 'st vincent and the grenadines': 'WPOPSVIN Index', 'honduras': 'WPOPHOND Index', 'new zealand': 'WPOPNEWZ Index', 'democratic republic of congo': 'WPOPCOND Index', 'turkey': 'WPOPTURK Index', 'saudi arabia': 'WPOPSAUD Index', 'iraq': 'WPOPIRAQ Index', 'bangladesh': 'WPOPBDT Index', 'uruguay': 'WPOPURUG Index', 'france': 'WPOPFRAN Index', 'bahamas': 'WPOPBAHA Index', 'slovakia': 'WPOPSLOV Index', 'ireland': 'WPOPIREL Index', 'laos': 'WPOPLAK Index', 'nigeria': 'WPOPNIGE Index', 'bolivia': 'WPOPBOLI Index', 'malawi': 'WPOPMALW Index', 'ecuador': 'WPOPECUA Index', 'israel': 'WPOPISRA Index', 'peru': 'WPOPPERU Index', 'algeria': 'WPOPALGE Index', 'serbia': 'WPOPSERB Index', 'tanzania': 'WPOPTANZ Index', 'montenegro': 'WPOPMONT Index', 'tajikistan': 'WPOPTAJI Index', 'togo': 'WPOPTOGO Index', 'jordan': 'WPOPJORD Index', 'chile': 'WPOPCHIL Index', 'martinique': 'WPOPMART Index', 'oman': 'WPOPOMAN Index', 'south korea': 'WPOPSKOR Index', 'spain': 'WPOPSPAI Index', 'georgia': 'WPOPGEOR Index', 'morocco': 'WPOPMORO Index', 'sweden': 'WPOPSWED Index', 'gabon': 'WPOPGABO Index', 'central african rep': 'WPOPCAFR Index', 'guyana': 'WPOPGUYA Index', 'grenada': 'WPOPGREN Index', 'guadeloupe': 'WPOPGUAD Index', 'hong kong': 'WPOPHONG Index', 'russia': 'WPOPRUSS Index', 'ghana': 'WPOPGHAN Index', 'portugal': 'WPOPPORT Index', 'mexico': 'WPOPMEXI Index', 'india': 'WPOPINDI Index', 'st lucia': 'WPOPSLUC Index', 'paraguay': 'WPOPPARA Index', 'australia': 'WPOPAUSL Index', 'uganda': 'WPOPUGAN Index', 'burundi': 'WPOPBURU Index', 'kenya': 'WPOPKENY Index', 'macao': 'WPOPMACA Index', 'botswana': 'WPOPBOTW Index', 'italy': 'WPOPITAL Index', 'south africa': 'WPOPSAFR Index', 'cambodia': 'WPOPCAMB Index', 'ethiopia': 'WPOPETHI Index', 'bermuda': 'WPOPBERM Index', 'vanuatu': 'WPOPVANU Index', 'cameroon': 'WPOPCAME Index', 'benin': 'WPOPBENI Index', 'brazil': 'WPOPBRAZ Index', 'singapore': 'WPOPSING Index', 'solomon islands': 'WPOPSOLO Index', 'iceland': 'WPOPICEL Index', 'monaco': 'WPOPMONA Index', 'costa rica': 'WPOPCOST Index', 'slovenia': 'WPOPSLVE Index', 'germany': 'WPOPGERM Index', 'dominica': 'WPOPDOMI Index', 'suriname': 'WPOPSURI Index', 'tonga': 'WPOPTONG Index', 'maldives': 'WPOPMALD Index', 'el salvador': 'WPOPELSA Index', 'poland': 'WPOPPOLA Index', 'indonesia': 'WPOPINDO Index', 'cape verde': 'WPOPCAPE Index', 'liechtenstein': 'WPOPLIEC Index', 'vietnam': 'WPOPVIET Index', 'kuwait': 'WPOPKUWA Index'}
unemp={'japan': 'EHUPJPY Index', 'lithuania': 'EHUPLTY Index', 'north america': 'EHUPNAMY Index', 'luxembourg': 'EHUPLUY Index', 'hungary': 'EHUPHUY Index', 'taiwan': 'EHUPTWY Index', 'estonia': 'EHUPEEY Index', 'european union': 'EHUPEUN Index', 'latvia': 'EHUPLV Index', 'argentina': 'EHUPARY Index', 'norway': 'EHUPNOY Index', 'ghana': 'EHUPGH Index', 'australia': 'EHUPAUY Index', 'belgium': 'EHUPBEY Index', 'world': 'EHUPWLDY Index', 'kazakhstan': 'EHUPKZ Index', 'latin america': 'EHUPLATY Index', 'ukraine': 'EHUPUAY Index', 'netherlands': 'EHUPNLY Index', 'denmark': 'EHUPDKY Index', 'philippines': 'EHUPPHY Index', 'croatia': 'EHUPHR Index', 'switzerland': 'EHUPCHY Index', 'western europe': 'EHUPWEUY Index', 'bulgaria': 'EHUPBGY Index', 'jamaica': 'EHUPJMY Index', 'angola': 'EHUPAOY Index', 'sri lanka': 'EHUPLK Index', 'serbia': 'EHUPRSY Index', 'lithuania': 'EHUPLT Index', 'malaysia': 'EHUPMYY Index', 'latvia': 'EHUPLVY Index', 'greece': 'EHUPGRY Index', 'nicaragua': 'EHUPNIY Index', 'g-20': 'EHUP20Y Index', 'canada': 'EHUPCAY Index', 'qatar': 'EHUPQA Index', 'guatemala': 'EHUPGT Index', 'kuwait': 'EHUPKWY Index', 'panama': 'EHUPPA Index', 'asia': 'EHUPASAY Index', 'venezuela': 'EHUPVE Index', 'europe': 'EHUPEURY Index', 'brics': 'EHUPBRCY Index', 'sri lanka': 'EHUPLKY Index', 'china': 'EHUPCNY Index', 'thailand': 'EHUPTHY Index', 'honduras': 'EHUPHN Index', 'oman': 'EHUPOMY Index', 'finland': 'EHUPFIY Index', 'nicaragua': 'EHUPNI Index', 'bangladesh': 'EHUPBD Index', 'dominican republic': 'EHUPDO Index', 'pakistan': 'EHUPPKY Index', 'romania': 'EHUPROY Index', 'czech republic': 'EHUPCZY Index', 'egypt': 'EHUPEGY Index', 'africa': 'EHUPAFRY Index', 'austria': 'EHUPATY Index', 'colombia': 'EHUPCOY Index', 'estonia': 'EHUPEE Index', 'new zealand': 'EHUPNZY Index', 'turkey': 'EHUPTRY Index', 'saudi arabia': 'EHUPSA Index', 'bangladesh': 'EHUPBDY Index', 'uruguay': 'EHUPUYY Index', 'france': 'EHUPFRY Index', 'g-8': 'EHUPG8Y Index', 'slovakia': 'EHUPSKY Index', 'ireland': 'EHUPIEY Index', 'luxembourg': 'EHUPLU Index', 'nigeria': 'EHUPNG Index', 'ecuador': 'EHUPECY Index', 'eurozone': 'EHUPEUY Index', 'israel': 'EHUPILY Index', 'peru': 'EHUPPEY Index', 'mid east': 'EHUPMETY Index', 'chile': 'EHUPCLY Index', 'south korea': 'EHUPKRY Index', 'spain': 'EHUPESY Index', 'cyprus': 'EHUPCYY Index', 'us': 'EHUPUSY Index', 'morocco': 'EHUPMAY Index', 'sweden': 'EHUPSEY Index', 'uk': 'EHUPGBY Index', 'hong kong': 'EHUPHKY Index', 'russia': 'EHUPRUY Index', 'bahrain': 'EHUPBHY Index', 'portugal': 'EHUPPTY Index', 'mexico': 'EHUPMXY Index', 'india': 'EHUPINY Index', 'kenya': 'EHUPKE Index', 'uae': 'EHUPAE Index', 'ukraine': 'EHUPUA Index', 'gcc': 'EHUPGCY Index', 'cyprus': 'EHUPCY Index', 'italy': 'EHUPITY Index', 'south africa': 'EHUPZAY Index', 'serbia unemployment rate historical (%)': 'EHUPRS Index', 'el salvador unemployment rate historical (%)': 'EHUPSV Index', 'brazil': 'EHUPBRY Index', 'singapore': 'EHUPSGY Index', 'iceland': 'EHUPISY Index', 'costa rica': 'EHUPCRY Index', 'slovenia': 'EHUPSIY Index', 'honduras': 'EHUPHNY Index', 'germany': 'EHUPDEY Index', 'middle east': 'EHUPMET Index', 'slovenia': 'EHUPSI Index', 'el salvador': 'EHUPSVY Index', 'poland': 'EHUPPLY Index', 'indonesia': 'EHUPIDY Index', 'emerging europe & africa': 'EHUPEEAY Index', 'vietnam': 'EHUPVNY Index', 'g10 region': 'EHUPG10 Index', 'g10': 'EHUPG10Y Index'}

# Function to get stock ticker from Strings (Company Names).
# Returns "No Results Found" if there are no results
def return_data(query):
    response = {}
    try:
        x = wpop[query.lower()]
        y = unemp[query.lower()]
        return countries(x, y)
    except:
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost("10.8.8.1")
        sessionOptions.setServerPort(8194)
        session = blpapi.Session(sessionOptions)
        session.start()
        session.openService("//blp/instruments")

        instrumentService = session.getService("//blp/instruments")
        request = instrumentService.createRequest("instrumentListRequest")

        request.set("query", query)
        request.set("maxResults", 1)

        session.sendRequest(request)

        event = session.nextEvent()
        run = True

        while (run):
            event = session.nextEvent()
            if event.eventType() == 5:
                for msg in event:
                    if msg.hasElement("results"):
                        fields = msg.getElement("results")
                        if fields.numValues() > 0:
                            for field in fields.values():
                                sec = field.getElementAsString("security")
                                dec = field.getElementAsString("description")
                                return companies(sec)
                            run = False
                        else:
                            print "No Results Found"
                            run = False
                    else:
                        print "No Results Found"
                        run = False

#Functions to get Stock Information
def companies(security):
    response = {}
    if "<equity>" not in security:
        response['status'] = False
        response['type'] = "Fail"
        response['error'] = "Not a Valid Security"
        return json.dumps(response)
    else:
        security = security.replace("<equity>", " Equity")
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost("10.8.8.1")
        sessionOptions.setServerPort(8194)
        session = blpapi.Session(sessionOptions)
        session.start()
        session.openService("//blp/refdata")
        refDataService = session.getService("//blp/refdata")
        request = refDataService.createRequest("ReferenceDataRequest")

        # append securities to request
        request.append("securities", security)
        request.append("fields", "PX_LAST")
        request.append("fields", "DS002")
        request.append("fields", "PX_BID")
        request.append("fields", "PX_ASK")
        request.append("fields", "VOLUME_AVG_30D")
        request.append("fields", "VOLATILITY_90D")

        session.sendRequest(request)

        try:
            while(True):
                event = session.nextEvent()
                if event.eventType() == 5:
                    for msg in event:
                        if msg.hasElement("securityData"):
                            fields = msg.getElement("securityData")
                            #print fields
                            for field in fields.values():
                                if field.hasElement("security"):
                                    response['security'] = field.getElementAsString("security")
                                    response['status'] = True
                                    response['type'] = "Security"
                                else:
                                    response['security'] = None

                                fd = field.getElement("fieldData")

                                if fd.hasElement("PX_LAST"):
                                    response['PX_LAST'] = fd.getElementAsString("PX_LAST")
                                else:
                                    response['PX_LAST'] = None

                                if fd.hasElement("DS002"):
                                    response['DS002'] = fd.getElementAsString("DS002")
                                else:
                                    response['DS002'] = None

                                if fd.hasElement("PX_BID"):
                                    response['PX_BID'] = fd.getElementAsString("PX_BID")
                                else:
                                    response['PX_BID'] = None

                                if fd.hasElement("PX_ASK"):
                                    response['PX_ASK'] = fd.getElementAsString("PX_ASK")
                                else:
                                    response['PX_ASK'] = None

                                if fd.hasElement['VOLUME_AVG_30D']:
                                    response['VOLUME_AVG_30D'] = fd.getElementAsString("VOLUME_AVG_30D")
                                else:
                                    response['VOLUME_AVG_30D'] = None

                                if fd.hasElement['VOLATILITY_90D']:
                                    response['VOLATILITY_90D'] = fd.getElementAsString("VOLATILITY_90D")
                                else:
                                    response['VOLATILITY_90D'] = None
                        else:
                            response['status'] = False
                            response['error'] = "Security Not Found"
                            response['type'] = "Security"
                if event.eventType() == blpapi.Event.RESPONSE:
                    break
        finally:
            session.stop()
            return json.dumps(response)

# Function to get Country Information
def countries(country_population, unemployment_rate):
    sessionOptions = blpapi.SessionOptions()
    sessionOptions.setServerHost("10.8.8.1")
    sessionOptions.setServerPort(8194)
    session = blpapi.Session(sessionOptions)
    session.start()
    session.openService("//blp/refdata")
    refDataService = session.getService("//blp/refdata")
    request = refDataService.createRequest("ReferenceDataRequest")

    # append securities to request
    request.append("securities", country_population)
    request.append("fields", "PX_LAST")

    #print "Sending Request:", request
    session.sendRequest(request)

    response = {}

    try:
        while(True):
            event = session.nextEvent()
            if event.eventType() == 5:
                for msg in event:
                    if msg.hasElement("securityData"):
                        fields = msg.getElement("securityData")
                        #print fields
                        for field in fields.values():
                            if field.hasElement("security"):
                                response['security'] = field.getElementAsString("security")
                                response['status'] = True
                                response['type'] = 'Country'
                                response['error'] = None
                            else:
                                response['security'] = None

                            fd = field.getElement("fieldData")

                            if fd.hasElement("PX_LAST"):
                                response['WPOP'] = fd.getElementAsString("PX_LAST")
                            else:
                                response['WPOP'] = None

                    else:
                        response['status'] = False
                        response['error'] = "Security Not Found"
                        response['type'] = "Security"
            if event.eventType() == blpapi.Event.RESPONSE:
                break
    finally:
        session.stop()

    sessionOptions = blpapi.SessionOptions()
    sessionOptions.setServerHost("10.8.8.1")
    sessionOptions.setServerPort(8194)
    session = blpapi.Session(sessionOptions)
    session.start()
    session.openService("//blp/refdata")
    refDataService = session.getService("//blp/refdata")
    request = refDataService.createRequest("ReferenceDataRequest")

    # append securities to request
    request.append("securities", unemployment_rate)
    request.append("fields", "PX_LAST")

    #print "Sending Request:", request
    session.sendRequest(request)

    try:
        while(True):
            event = session.nextEvent()
            if event.eventType() == 5:
                for msg in event:
                    if msg.hasElement("securityData"):
                        fields = msg.getElement("securityData")
                        #print fields
                        for field in fields.values():
                            if field.hasElement("security"):
                                response['security'] = field.getElementAsString("security")
                                response['status'] = True
                                response['type'] = 'Country'
                                response['error'] = None
                            else:
                                response['security'] = None

                            fd = field.getElement("fieldData")

                            if fd.hasElement("PX_LAST"):
                                response['UNEMP'] = fd.getElementAsString("PX_LAST")
                            else:
                                response['UNEMP'] = None

                    else:
                        response['status'] = False
                        response['error'] = "Security Not Found"
                        response['type'] = "Security"
            if event.eventType() == blpapi.Event.RESPONSE:
                break
    finally:
        session.stop()
        return json.dumps(response)

def test():
    print "IBM"
    print return_data("ibm")
    print "Canada"
    print return_data("Canada")
    print "Apple"
    print return_data("apple")
    print "DONE!"

#test()
