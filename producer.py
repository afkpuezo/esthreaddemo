"""
Contains a function for the thread that will produce the kafka messages.

@author: Andrew Curry
"""
from kafka import KafkaProducer


def produce(programs: list[int]):
    """
    Sends instructions through kafka about which 'programs' to run.
    Messages will be in the format 'Program:1', 'Program:2', etc
    """
    producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    for program in programs:
        message = b'Program:' + str(program).encode()
        producer.send('esthread', message)