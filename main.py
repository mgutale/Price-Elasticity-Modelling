import argparse
import numpy as np
import pandas as pd
import statsmodels.api as sm

def calculate_price_elasticity(sales_data_path):
    # Load the sales data from the CSV file
    sales_df = pd.read_csv(sales_data_path)

    # Calculate the percentage change in quantity sold and price
    sales_df['Pct Change Quantity Sold'] = sales_df.groupby(['Membership Type', 'Location Name'])['Memberships Sold'].pct_change()
    sales_df['Pct Change Price'] = sales_df.groupby(['Membership Type', 'Location Name'])['Average Price'].pct_change()

    # Define the independent variable (percentage change in price)
    X = sales_df.groupby(['Membership Type', 'Location Name'])['Pct Change Price'].mean()

    # Define the dependent variable (percentage change in quantity sold)
    y = sales_df.groupby(['Membership Type', 'Location Name'])['Pct Change Quantity Sold'].mean()

    # Fit a linear regression model to the data for each membership type and location
    results = []
    for membership_type in sales_df['Membership Type'].unique():
        for location_name in sales_df['Location Name'].unique():
            # Filter the sales data for the current membership type and location
            subset = sales_df[(sales_df['Membership Type'] == membership_type) & (sales_df['Location Name'] == location_name)]

            # Remove rows with missing values or zeros in the Pct Change Price variable
            subset = subset[~subset['Pct Change Price'].isnull()]
            subset = subset[subset['Pct Change Price'] != 0]

            # Define the independent variable (percentage change in price)
            X = subset['Pct Change Price']

            # Define the dependent variable (percentage change in quantity sold)
            y = subset['Pct Change Quantity Sold']

            # Fit a linear regression model to the data
            model = sm.OLS(y, sm.add_constant(X)).fit()

            # Calculate the price elasticity of demand
            price_elasticity = -1 * model.params['Pct Change Price'] * (subset['Average Price'].mean() / subset['Memberships Sold'].mean())

            # Append the results to the list
            results.append({
                'Membership Type': membership_type,
                'Location Name': location_name,
                'Price Elasticity of Demand': price_elasticity
            })

    # Convert the results to a Pandas dataframe and return it
    return pd.DataFrame(results)

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('sales_data_path', help='path to the CSV file containing the sales data')
    args = parser.parse_args()

    # Calculate the price elasticity of demand for each membership type and location
    results_df = calculate_price_elasticity(args.sales_data_path)

    # Print the results
    print(results_df)
