---
layout: post
title:  "Goals for Week of November 10"
date:   2014-11-10 08:08:12.901895
categories:
---

### Monday

* Review Exam Solutions
* Work on DV Routing

### Wednesday

* Prelims in the lab

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

![Protocol Design](/CS341/images/dv_protocol.jpg)


### Friday

* Final routing day

