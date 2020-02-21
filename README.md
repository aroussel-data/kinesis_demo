# Demo streaming application

This repo is set up to demonstrate a streaming app which:
- Uses the Python AWS SDK as a Kinesis streams producer
- Puts the data to a Kinesis stream
- Outputs data to a Lambda function as a Kinesis consumer
- Uses the Lambda function to store data in DynamoDB

## Setup
- From the `kinesis_demo` directory
- `source ../venv/bin/activate`
- `pip install -r requirements.txt`

## Running:

- To run the Python Kinesis producer which just writes a dict of values
repeatedly to a stream:
- `python kinesis_demo.py`

## Upcoming changes:
- Now that PoC works, clean up code and make it more modular
- Rather than generating dummy data I would like to either connect to real-time
device data, or fetch some interesting open data from a web API
- Scale up the number of shards in the stream to process more data but am
constrained by costs at the moment
- Start scaling up the volume to test ability for Lambda to process and find the 
point at which its synchronous processing becomes too slow, at which point modify 
Lambda to process the data asynchronously.
- Output to a data warehouse such as Redshift as data volume grows 