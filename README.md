# telco_classification_project

## About the project

### Project Goals

* To identify drivers of customer churn and find a solution for increasing customer retention
* To construct a model that accurately predicts which customers are most likely to churn to focus retention efforts

### Project Description

Reducing churn is important to the company because lost customers means lost revenue. The cost of acquiring a new customer is much higher than maintaining a customer so this project will attempt to identify strategies that reduce customer churn. In the process, we are also looking for ways to improve customer satisfaction to increase the company's rate of growth.

### Initial Hypotheses/Questions

* Do customers with month-to-month contracts churn at a higher rate? What are the churn rates with other contract types?

* Is there a certain tenure length where month-to-month customers are more likely to churn? What about customers with contracts?

* Is any specific service associated with higher churn rates?

* Is it higher monthly charges that are causing churn? If so, what is that threshold where most customers churn for their specific service?

### Data dictionary


### Project Planning

**Planning**

* Define goals
* Determine audience and delivery format
* What is my MVP?
* Ask questions/formulate hypotheses

**Acquisition**
* Create function for establishing connection to telco_churn db
* Create function for SQL query and reading in results
* Create function caching data
* Create acquire.py to save these functions for importing
* Test functions

**Preparation**
* Create function that cleans data
  * Change data type for total_charges from object to float
  * Drop monthly_charges null values where customers have less than a month of tenure therefore no opportunity to churn
  * Replace all instances of 'No internet service' as that information is in internet_service_type column and doing so simplifies encoding by creating binary values for many of the colums
  * Create dummy variables for columns with object datatype
  * Drop columns that contain duplicate information or are unnecessary
  * Rename columns 
* Create function that splits data into train, validate, and test samples
  * Split 20% (test), 24% (validate), and 56% (train)
* Create prepare.py to save these functions for importing
* Test functions

**Exploration**
* 
* 

**Modeling**

**Delivery**

### To Recreate This Project:

### Answers to Hypotheses/Questions

### Key Findings, Recommendations, and Next Steps

