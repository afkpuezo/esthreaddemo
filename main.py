"""
Triggers the kafka producer to send instructions, then uses a different thread to execute
each of the actions in the instructed program's action list.

@author: Andrew Curry
"""
import threading
from action_parsing import parse_action_list
from kafka import KafkaConsumer
from threading import Thread
import random
from producer import produce
from action_retrieval import get_action_list
from range_printing import print_range


def main():
    """
    Triggers the kafka producer to send instructions, then uses a different thread to execute
    each of the actions in the instructed program's action list.
    """
    # prepare the producer
    programs = [] 
    programs.append(random.randint(1, 3)) # may have other way of picking later?
    prod_thread = Thread(target = produce, kwargs = {'programs' : programs})
    # consume those messages
    consumer = KafkaConsumer('esthread')
    #print("DEBUG: consumer initialized")
    consumer.pause()
    prod_thread.start()
    consumer.resume()
    action_lists = []
    #print("DEBUG: about to start consumer loop")
    for message in consumer:
        if message.value == b'END':
            break
        else:
            action_lists.append(get_action_list(message.value))
    # execute the instructions
    print("Received instructions to execute the following programs:")
    for action_list in action_lists:
        print("     " + action_list)
    print("Executing...")
    lock = threading.Lock()
    for action_list in action_lists:
        print("     " + action_list)
        ranges = parse_action_list(action_list)
        threads = []
        for r in ranges:
            t = Thread(
                target = print_range, 
                kwargs = {'start' : r[0], 'end' : r[1], 'delay' : 0.05, 'lock' : lock})
            threads.append(t)
            t.start()
        for t in threads:
            t.join()


main()