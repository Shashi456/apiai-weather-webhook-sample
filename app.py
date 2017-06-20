#!/usr/bin/env python


import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebHookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

 
 def makeWebhookResult(req):
    if req.get("result").get("action") != "HotelSearch":
        return {}
    re = req.get("result")
    parameters = result.get("parameters")
    city=parameters.get("geo-city")
    
    place={"barcelona"="guide/spain/barcelona/" ,
    "paris"="guide/france/paris"
    }
    
    main="https://www.alpharooms.com/"
    search=str(place[city])
    end="default.aspx?channel=AlphaRoomsUK"

    # print(json.dumps(item, indent=4))

    speech = main+search+end
    speech=str(speech)

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "HotelSearch Sample"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
