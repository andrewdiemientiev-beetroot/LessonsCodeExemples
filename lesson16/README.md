# House simulation program

## Description
Write a program that simulates life in house. It means that there will be a family that owns this house. House also can 
visit other people. They should be registered and they should be in the house all the time. Also if all members of the 
house will exit it the house should be locked. Also the house have clocks in it and each action takes exactly an hour.
Create user interface with console to use all this methods.

## Requirements
Class house should contain arguments:
* family
* guests
* is_locked
* clock

Class also should have ability to:
* Let in one or several people of the family.
* Let out one or several people of the family.
* Let in one or more guests if some one from the family in the house
* Let out one or more guests.
* Each action should take 1 hour. (Write decorator which will do the math)
* Let out guests if night came (If it's 11:00pm or later).
* Put every one to sleep, which fast-forward time to 8:00 am.

For clocks use build in library **time**. 

## Validation

* House should be locked if there is no one in house and vice versa.
* House should not contain any guests after 11:00 pm.
* Guests allowed to be in the house if only one our several members of family in the house.
* Guests allowed to be in the house only from 8:00 am till 11:00 pm.
* People name should contain Name and Surname written in title.
* People name should not contain numbers or symbols in it, only letters and whitespaces.


## Task with *
People should be presented as a separate class called **Person**.
Each person should contain name, age and type (Family/Guest)

** Additional validation for task with *
* If if there are only children in house, guests are not allowed to be in house.
* Elder members of family should not go out from house starting from 9:00 pm if they have child or children.
* There should be at least one member of family with children if they are in house.
