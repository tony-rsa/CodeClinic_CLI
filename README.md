# Code_Clinic_CLI_Python3

# TO RUN
  -> activate venv : '. .venv/bin/activate'
  -> run : 'python3 ./cc'
  -> get help: 'python3 ./cc help'


# Description of the project
WeThinkCode_ introduced Coding Clinics to help students share challenges they are facing with the coding problems. A student needs to book a specific time slot to attend a Coding Clinic session, and typically these sessions are one-on-one sessions with a more experienced person who can advise on the coding problem at hand.

Your team is tasked to create a set of command-line tools that will automate the booking system. The system must allow students to see where there are available time slots for specific dates and campuses, and allow them to book sessions. To ensure that there are no double bookings, it must synchronise with the Coding Clinic’s Google calendars, as well as the students’ own calendars.


# Overview of the Coding Clinic Booking System
The booking system will be implemented as a set of command-line tools that must satisfy the following criteria, in addition to the requirements below.

run on the Linux version that you are using on campus
take command-line arguments as input
it must have a help command that describes the command-line arguments
it must provide output either to a file and/or to standard output, so that it can be used by another command-line tool in the system
if providing output via standard output, it means the output can also be piped to a file using the linux pipe operators
you can choose in what data format you will store any internal data, e.g. json, xml, or something else entirely.
