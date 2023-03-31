# Price Elasticity Modelling

This project explores the price elasticity of demand for different membership types across various locations. The goal is to estimate the responsiveness of quantity demanded to changes in price, and to identify which membership types and locations are most sensitive to price changes.

## Data
The sales data used in this project is stored in a CSV file sales_data.csv. It includes the following columns:

    Month: The month in which the sales were made (integer)
    Membership Type: The type of membership sold (string)
    Headline Price: The advertised price for the membership (float)
    Underlying Prices: The actual prices paid for the membership, as a list of floats (one for each membership sold)
    Location Name: The name of the location where the sales were made (string)
    Memberships Sold: The number of memberships sold (integer)
    Total Revenue: The total revenue generated from the sale (float)
    Average Price: The average price per membership sold (float)
    Pct Change Quantity Sold: The percentage change in quantity sold, relative to the previous month (float)
    Pct Change Price: The percentage change in price, relative to the previous month (float)

## Analysis
The analysis of the sales data involves calculating the percentage change in quantity sold and price for each membership type and location, and then fitting a linear regression model to the data. The price elasticity of demand is then calculated from the slope of the regression line, using the formula:

price_elasticity = -1 * model.params['Pct Change Price'] * (subset['Average Price'].mean() / subset['Memberships Sold'].mean())

The price elasticity of demand is reported for each membership type and location combination.

## Usage
To run the analysis, simply run the price_elasticity_modelling.py script. This will generate the output for each membership type and location combination.

An example on how you can run this code via the commmand line as follows

python calculate_price_elasticity.py sales_data.csv


## Dependencies
This project requires the following Python packages:

NumPy
Pandas
Statsmodels
These packages can be installed using pip:

pip install numpy pandas statsmodels
