import boto3
import json
import numpy as np
import random
import string
import uuid
import time

session = boto3.session.Session(profile_name='alex')

client = session.client('kinesis')

if client.describe_stream(StreamName='demo_stream'):
    print('Stream already exists, do not create')
else:
    response = client.create_stream(StreamName='demo_stream', ShardCount=1)


def generate_random_str(l):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(l)])


if __name__ == "__main__":
    while True:
        my_dict = {
          "id": str(uuid.uuid1()),
          "name": generate_random_str(5),
          "address": generate_random_str(10),
          "year": str(np.random.randint(2000))
        }

        put = client.put_record(StreamName='demo_stream', Data=json.dumps(my_dict),
                                PartitionKey=str(np.random.randint(100)))
        print("result of put record: {}".format(put.get('ResponseMetadata').get('HTTPStatusCode')))

        time.sleep(5)
