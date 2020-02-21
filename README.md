# BIP data streaming application

This pipeline is set up to:
- Poll data from the Coindesk API (https://www.coindesk.com/coindesk-api)
- Loads price data into an AWS Kinesis stream
- Have AWS Lambda ingest stream data on a FIFO basis
- Use the Lambda function to store the data in DynamoDB

## Setup
- From the `kinesis_demo` directory
- `source ../venv/bin/activate`
- `pip install -r requirements.txt`

## Running:
- `python kinesis_demo.py`

## Upcoming changes:
- Would like to find a good solution to visualise the data in DynamoDB, to get a rolling "ticker tape" style
view of BPI prices.
- Scale up the number of shards in the stream to process more data but am
constrained by costs at the moment (Kinesis is expensive)
- Start scaling up the volume to test ability for Lambda to process and find the 
point at which its synchronous processing becomes too slow, at which point modify 
Lambda to process the data asynchronously (again, this is expensive).
- Maybe output to a data warehouse (relational DB may suffice, data warehouse is probably overkill for such small data)
such as Redshift as data volume grows or simply for easier visualisation.