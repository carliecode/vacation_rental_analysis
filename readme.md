Vacation Rental Analysis 
=========================

Overview
------------
This repository contains Python code for analyzing a dataset of vacation rental listings and reviews. The analysis addresses seven specific questions related to neighborhood price differences, correlation analysis, professional host analysis, and median price premiums.

Dataset Description
----------------------
The dataset consists of two files:
listings.csv: A table containing information about vacation rental listings, including attributes related to the listing and its host.
reviews.csv: A table containing information about guest reviews for the listings, including attributes such as review date and reviewer name.

Tasks
--------

**Task 1: Neighborhood Price Difference**
What is the neighborhood in which superhosts have the biggest median price difference with respect to non-superhosts? This task uses the following columns in the listings dataset:
host_is_superhost
neighbourhood_cleansed
price

**Task 2: Correlation Analysis**
Which of the review scores has the strongest correlation to price? This task uses the following review score columns in the listings dataset:
review_scores_rating
review_scores_accuracy
review_scores_cleanliness
review_scores_checkin
review_scores_communication
review_scores_location
review_scores_value

**Task 3: Professional Host Analysis**
What is the average price difference between a professional host and a non-professional one? For the purpose of this task, a host is considered professional if they have listings in more than 5 different locations, defined by the neighbourhood_cleansed column.

**Task 4: Median Price Premium**
What is the median price premium given to entire homes / entire apartments with respect to other listings of the same neighborhood? Report the average across all neighborhoods. This task uses the room_type column in the listings dataset.

Code Organization
---------------------
Each task is implemented as a separate function in a single Python file.

Requirements
------------
Python 3.x
Pandas library

Usage
-----
  - Clone the repository to your local machine.
  - Install the required libraries using pip install pandas numpy matplotlib.
  - Run the Python file to execute the functions for each task.

