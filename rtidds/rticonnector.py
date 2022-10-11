# -*-coding: "utf-8"-*-

"""
# File:        rticonnector.py
# Author:      "liyi"
# CreateTime:  2022/7/20 16:03
# Version:     python 3.6
# Description:   
"""
from time import sleep
from sys import path as sys_path
from os import path as os_path
from threading import Thread

import rticonnextdds_connector

file_path = os_path.dirname(os_path.realpath(__file__))
sys_path.append(file_path)


import rticonnextdds_connector as rti

def writer(connector):

        print(connector)

        output = connector.get_output("MyPublisher::MySquareWriter")
        print("Waiting for subscriptions...")
        a = output.wait_for_subscriptions(timeout=100000)
        print(a)

        print("Writing...")
        for i in range(1,5):
            output.instance.set_number("x", i)
            output.instance.set_number("y", i*2)
            output.instance.set_number("shapesize", 30)
            output.instance.set_string("color", "BLUE")
            output.write()
            print(i)

            sleep(0.5)

        print("Exiting...")
        output.wait()

def reader(connector):
    input = connector.get_input("MySubscriber::MySquareReader")

    print("Waiting for publications...")
    input.wait_for_publications()  # wait for at least one matching publication

    print("Waiting for data...")
    for i in range(1, 500):
        input.wait()  # wait for data on this input
        input.take()
        for sample in input.samples.valid_data_iter:
            # You can get all the fields in a get_dictionary()
            data = sample.get_dictionary()
            x = data['x']
            y = data['y']

            # Or you can access the field individually
            size = sample.get_number("shapesize")
            color = sample.get_string("color")
            print("Received x: " + repr(x) + " y: " + repr(y) +
                  " size: " + repr(size) + " color: " + repr(color))

if __name__ == "__main__":
    connector = rti.Connector(config_name="MyParticipantLibrary::MyParticipant",
                              url=file_path + "/ShapeExample.xml")
    # thread1 = Thread(target=writer(connector))
    # thread2 = Thread(target=reader(connector))
    # thread1.start()
    # thread2.start()
    writer(connector)
    reader(connector)