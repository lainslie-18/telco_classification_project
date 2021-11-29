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

|   Column_Name   | Description | Type      |
|   -----------   | ----------- | ---------- |
| payment_type_id | numeric representation of payment type | int64 |
| internet_service_type_id   | numeric representation of internet service type | int64  |
| contract_type_id      | numeric representation of contract type  | int64 |
| customer_id      | unique value associated with customer | int64 |
| gender   | indicates customer's gender        | object    | 
| senior_citizen      | indicates if customer is senior citizen      | int64 |
| partner   | indicates if customer has a partner       |  object |
| dependents      | indicates if customer has dependents  | object
| tenure   | indicates number of months customer has had service        | int64        | 
| phone_service   | indicates if customer has phone service | object | 
| multiple_lines      | indicates if customer has multiple lines | object
| online_security   | indicates if customer has online security | object | 
| online_backup      | indicates if customer has online backup | object |
| device_protection   | indicates if customer has device protection | object  |
| tech_support      | indicates if customer has tech support| object |
| streaming_tv   | indicates if customer has streaming tv | object  |
| streaming_movies   | indicates if customer has streaming movies | object   |
| paperless_billing      | indicates if customer has paperless billing | object |
| monthly_charges   | customer's monthly charges | float64 |
| total_charges      | customer's total accumulated charges       | float64 |
| churn   | indicates if customer has churned | object   |
| contract_type   | indicates customer's contract type (month-to-month, one year, or two year)| object        |
| internet_service_type      | indicates customer's internet service type (no internet, fiber optic, or DSL) | object
| payment_type   | indicates customer's payment type (electronic check, mailed check, bank transfer (automatic), or credit card (automatic) | object        |

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
* Ask questions/form hypotheses
  * Do customers with month-to-month contracts churn more than other contract types?
  * Is there a tenure length where customers are more likely to churn?
  * Is a specific internet service type associated with higher churn rates?
  * Is it higher monthly charges that are causing churn?
* Create visualizations to help identify drivers
* Use statistical tests to test hypotheses
* Document answers to questions and takeaways
  * Month-to-month customers churn at almost 5x the rate of those with contracts.
  * The largest portion of customers who churn do so within the first 6 months.
  * Both the chart and test show that fiber optic customers are more likely to churn.
  * Both the chart and test show that churn is associated with higher monthly charges.
  * Key takeaway is that customers are unhappy with the higher prices associated with fiber optic service and/or the quality of fiber optic service

**Modeling**
* Train model
* Make predictions
* Evaluate model
* Compute accuracy

**Delivery**
* Report will be in Jupyter Notebook
* Present via Zoom
* Audience will be direct manager and their manager

### To Recreate This Project:
* You will need an env file with your database credentials (user, password, hostname) saved to your working directory
* Create a gitignore and add your env file to prevent your credentials from getting pushed to Github
* Download the aquire.py and prepare.py files to your working directory
* Download the telco_classification_project_final notebook to your working directory
* Read this README.md
* Run the telco_classification_project_final.ipynb notebook

### Recommendations and Next Steps
* Reduce monthly price for fiber optic internet service

* Send out quarterly customer satisfaction surveys for better insights

* With more time and resources, would like to collect and explore customer satisfaction data
