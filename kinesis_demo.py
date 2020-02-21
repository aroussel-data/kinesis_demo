import boto3
import json
import random
import string
import uuid
import time
import logging

logging.basicConfig(level='INFO')


def generate_random_str(l):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(l)])


if __name__ == "__main__":

    session = boto3.session.Session(profile_name='alex')
    client = session.client('kinesis')
    current_streams = client.list_streams()

    if len(current_streams['StreamNames']) > 0:
        logging.info("Stream already exists, do not create")
    else:
        logging.info("Creating kinesis stream...")
        response = client.create_stream(StreamName='demo_stream', ShardCount=1)

    while True:
        my_dict = {
          "id": str(uuid.uuid1()),
          "name": generate_random_str(5),
          "address": generate_random_str(10),
          "year": random.randint(2000, 2021)
        }
        time.sleep(5)
        put = client.put_record(StreamName='demo_stream', Data=json.dumps(my_dict),
                                PartitionKey=str(random.randint(0, 101)))
        logging.info("result of put record: {}".format(put.get('ResponseMetadata').get('HTTPStatusCode')))
