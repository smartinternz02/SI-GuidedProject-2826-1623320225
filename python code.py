import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "h1ka6y",
        "typeId": "iotdevice",
        "deviceId":"1001"
    },
    "auth": {
        "token": "1234567890"
    }
}
   
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    slot=random.randint(0,30)
    count=random.randint(0,30)
    #slot=int(input())
    #count=int(input())
    myData={"d":{'slot':slot, 'count':count}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: ", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
