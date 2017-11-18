import requests, json
from time import sleep
import i2c_lcd  # First you need to run "pip install i2c_lcd"

def getBitcoinPriceStr(currency):
        URL = 'https://api.coinbase.com/v2/prices/BTC-%s/spot' % currency

        try:
                r = requests.get(URL)
                priceStr = "{0:.2f}".format(float(json.loads(r.text)['data']['amount']))
                return priceStr
        except requests.ConnectionError:
                print "Error fetching Bitcoin price from Coinbase API"


lcd = i2c_lcd.lcd()

try:
        line1 = "BTC/EUR " + str(getBitcoinPriceStr('EUR'))
        line2 = "BTC/USD " + str(getBitcoinPriceStr('USD'))
        lcd.lcd_display_string(line1,1)
        lcd.lcd_display_string(line2,2)

except:
        lcd.lcd_display_string('Cannot reach API',1)
        "Error getting price"