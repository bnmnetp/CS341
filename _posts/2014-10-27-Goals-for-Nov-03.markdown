---
layout: post
title:  "Goals for Week of November 3"
date:   2014-11-02 16:08:12.901895
categories:
---

### Monday

* Finish up DV Routing Exercise
* Protocol Design Exercise

#### DV Routing Lab

The DV Routing lab will be done in two parts.

1. You must write a program that implements the DV routing algorithm as described in the book.  
   * Your program must interact with other programs written by your classmates, so we will need to devise a protocol.  
   * Your program will need to be able to send and receive protocol messages from multiple neighbors
   * Your program will need to read a configuration file that describes the immediate neighbors and the cost of getting to that neighbor.
   * You will need to provide me with your code, and your completed routing vector.
   
2. In part two we will use the routes you create in part 1 to send messages in a peer-to-peer overlay network.
   * You will need to modify your program to accept another protocol message that contains a message and its final destination. 
   * You will need to write a small client to accept a message and destination and send the message into the network.
   * If your program is the final destination for the message you will need to print out the message.
   * part of the message protocol and design will be to allow each intermediate router to add its own address to a list so that when the message reaches the final destination not only the message but the route the message took can be printed out.

We will have a lab day next Wednesday as a "test day" for you to try out your program with the entire class.  This will likely descend into chaos on the first day that we give it a try.  By the end of class on Friday we should have all the bugs worked out of part 1.



### Wednesday

* Routing and Hierarchical Routing
* Broadcast Routing
* NAT Wireshark Lab

![Protocol Design](../images/dv_protocol.jpg)


### Friday

* Exam over chapters 3 and 4



