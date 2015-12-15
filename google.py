from googlefinance import getQuotes
import json
print json.dumps(getQuotes('CSCO'),indent=2)
