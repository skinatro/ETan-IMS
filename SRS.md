Product Name: E-Tan IMS
Version: v0.1 (The document is subject to change)

# Introduction

## Purpose

Develop an Inventory Management System which allows the users to rent available parts from E-Tan from the given catalogue.

## Intended Audience

Students from SFIT ECS and ExTC branches wanting to rent parts for their Mini Project

## Scope

## Definitions

- IMS: Inventory Management System
- LMS: Library Management System
- Administrator: The E-Tan member who will be managing the software
- Customer: The students who will be renting parts from E-Tan

## References

Pre-existing IMS and LMS

# Product Description

## Hardware Interface

The user needs to have working internet connection, modern browser with Javascript Enabled and computer with monitor, mouse and keyboard

## User Interface

The User Interface will be made using ReactJs and Tailwind CSS

The User Interface will serve two different types of users
1. Administrator
2. Customer

The interface will be divided into 2 parts
- Main Screen
- Side Panel
- Top Panel

Main Screen will house the information pertaining to that particular menu
Side Panel will allow the user to change between different menus
Top Panel will house the Application Logo, Search Bar and Profile Menu

### Administrator Interface

The menu panel will have various options like Dashboard, Orders, Inventory and Customers

- Dashboard: The admin will be able to see the number of borrowed items and recently checked out items
- Orders: It will list out the parts the customer has booked but not paid yet. The admin can accept or reject the orders here.
- Inventory: List, Add and Modify all the items present in the inventory with their various attributes
  - Item Name
  - Number of items
  - Borrowee Name
  - Item Photo
  - Component ID
  - Rental Rate
  - Item is Rentable or not
  - Purchase Date (when E-Tan acquired the product)
  
### Customer Interface

The customer menu panel will have its own Dashboard and Inventory

- Dashboard: List of all the borrowed and booked items from the inventory
- Inventory: It will list out all the items prsent in the inventory with option to toggle un-rentable, booked and out of stock items

### Profile Menu

The profile menu will list out the user data like their PID, email and password

## System Interface

### Software Interface

The software is a web application using Django Framework on a python 3+ environment
The backend will be hosted on a linux based server with support for a SQL server

### Communication Interface

The User Interface will be access via a modern web browser using HTTPS connection
The frontend and backend will communicate via RESTful APIs in JSON format
User login and data will be protected via JWT based authentication

## Constraints, Assumption, Dependencies

### Security Constraints

The user will be given five attempts to enter the password , if it fails then they would have to reset the password

### Assumption

The customer will be student of SFIT with a valid PID number
The user will have a reliable internet connection and will be operating the website on a desktop system

## User Characteristics

The program is made to accomodate two types of users
- Administrator
- Customer

# System Feature and Requirement

## Functional Requirement

The admin will be able to update the view and update the inventory and allow order confirmation
The customer will be able to view the inventory and book an item

## External Interfaces

## Database Requirement

A RDBMS database like MySQL or Postgresql will be used

# Future Scope

There will be a mobile friendly version of the site
Password will be resetted over email
