## AirBnB clone - The console

This README is for 0x00. AirBnB clone - The console. This the first project in a collection of 7 projects to produce a fully functioning, simple replica of AirBnB. 

This repo has been worked on together by Allen Nicholson and Kellie Mogg, students from cohort 13 at Holberton Computer Science School in Tulsa. 

The main concepts that we tackled in this part of the project are: classes, inheritance, using *args and **kwargs, managing the datetime module, and file storage using JSON. We produced a cmd module to create, edit, and destroy objects from the command line. 

Current status: So far, in our program a user can create objects with unique IDs (uuid), update attributes of those objects, display all the objects being stored, and destroy objects all from a command line interpreter. Once an object is created it is stored using the data format, JSON. After reopening the program, the stored objects created before will be retrieved from the JSON file. 

Subclasses featured: User, City, State, Place, Review, and Amenity. These subclasses will be the foundation of our AirBnB website for the user.