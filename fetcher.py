from kinesis_demo import client

# This is just here if need to fetch some records from the stream, but will probably remove.

shard_it = client.get_shard_iterator(StreamName='demo_stream', ShardId='shardId-000000000000',
                                     ShardIteratorType='LATEST')

result = client.get_records(ShardIterator=shard_it['ShardIterator'])
