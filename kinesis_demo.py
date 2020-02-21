import boto3
import json
import random
import uuid
import time
import logging
import requests
from constants import COINDESK_ENDPOINT

logging.basicConfig(level='INFO')


def poll_price_data():
    """
    Polls the Coindesk API to fetch the latest price data.
    :return: dict of USD Bitcoin price with time.
    """
    resp = requests.get(COINDESK_ENDPOINT)  # Powered by CoinDesk
    if resp.status_code == 200:
        logging.info("GET request succeeded")
        data = resp.json()
        data_dict = {
            "id": str(uuid.uuid1()),
            "time": data['time']['updated'],
            "currency": data['bpi']['USD']['code'],
            "price": data['bpi']['USD']['rate']
        }
        return data_dict
    else:
        logging.error("GET request failed")


if __name__ == "__main__":
    """
    Entry point for the Kinesis stream that (for the moment) has dummy data written to it, before being processed
    by a Lambda function and written to DynamoDB.
    """

    session = boto3.session.Session(profile_name='alex')
    client = session.client('kinesis')
    current_streams = client.list_streams()

    if len(current_streams['StreamNames']) > 0:
        logging.info("Stream already exists, do not create")
    else:
        logging.info("Creating kinesis stream...")
        response = client.create_stream(StreamName='demo_stream', ShardCount=1)

    while True:
        payload = poll_price_data()
        time.sleep(5)
        put = client.put_record(StreamName='demo_stream', Data=json.dumps(payload),
                                PartitionKey=str(random.randint(0, 101)))
        logging.info("result of put record: {}".format(put.get('ResponseMetadata').get('HTTPStatusCode')))
