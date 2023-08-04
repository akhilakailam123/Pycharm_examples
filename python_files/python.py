# import json
# import logging
# # from forex_python.converter import CurrencyRates
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
#
# def lambda_handler(event, context):
#     """
#     The Lambda handler function that gets invoked when the API endpoint is hit
#     """
#     amount = event['queryStringParameters']['amount']
#     from_Currency = event['queryStringParameters']['fromCurrency']
#     to_Currency = event['queryStringParameters']['toCurrency']
#     logger.info('## Input Parameters: %s, %s, %s', amount, from_Currency, to_Currency)
#     # res = convert_currency(amount, from_Currency, to_Currency)
#     res = amount
#     logger.info('## Currency result: %s', res)
#     response = {
#         "statusCode": 200,
#         "body": json.dumps({'result': res}),
#     }
#     logger.info('## Response returned: %s', response)
#     return response
# # def convert_currency(amount: float, fromCurrency: str, toCurrency: str) -> float:
# #     """
# #     Function to convert an amount from one currency to another
# #     """
# #     c = CurrencyRates()
# #     res = c.convert(fromCurrency, toCurrency, float(amount))
# #     return float(res)
import os
import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    endpoint = os.environ.get("end_point")
    data = requests.get(endpoint)
    print(data)
    logger.info("returned response :",data)
    return{
        'status_code': 200,
        'body': json.dumps(data)
    }