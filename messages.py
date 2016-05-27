#!/usr/bin/env python
from constants import ITTY, HEADERS, ROOMS_URL, MESSAGES_URL
from itty import *
import requests
import json
import urllib


##
# Posts message to Devs room on Spark
#
def send_message(room_id, message):
    data = { "roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vODZhN2EwZjAtMTE3NC0xMWU2LTgxNTYtZjE0MzI0YjNkMWNk",
             "text" : message }
    resp = requests.post(MESSAGES_URL,json=data, headers=HEADERS)
    return json.loads(resp.text)

##
# Path : /messages
# Method : POST
#
# This path receives the text message posted from Tropo.
#
@post('/messages')
def _(request):
    message = request.body
    response = send_message(DEVS_ID, message)
    return Response(json.dumps(response), content_type='application/json')


run_itty(**ITTY)