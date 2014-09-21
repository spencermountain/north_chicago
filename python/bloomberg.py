import blpapi
import json
from countries import wpop, unemp

# Function to get stock ticker from Company Names.
# Returns "No Results Found" if there are no results. If the input string is
# a country, this function returns vaious data points about the country
def return_data(query):
    response = {}
    try:
        #If we can find the country in the list of countries,
        #treat it like a country with these attributes
        population = wpop[query.lower()]
        unemployment = unemp[query.lower()]
        return countries(population, unemployment)
    except:
        #Otherwise it is a company, or not anything
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
    print return_data("Mozilla")
    print return_data("Bloomberg")
    print "DONE!"

#test()
