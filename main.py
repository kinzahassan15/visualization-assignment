import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.read_csv('world_population.csv')

def line_chart_analysis():
    """ This function handles line chart analysis """
    continent_population = df.groupby('Continent').sum()[['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']]
    continent_population = continent_population.T

    plt.figure(figsize=(12, 6))

    for continent in continent_population.columns:
        plt.plot(continent_population.index, continent_population[continent], label=continent)

    plt.xlabel('Year')
    plt.ylabel('Population (Billions)')
    plt.title('Population Growth by Continent')
    plt.legend()
    plt.grid(True)

    # Reverse the x-axis
    plt.gca().invert_xaxis()

    # Display only years on the x-axis
    plt.xticks(continent_population.index, rotation=45)

    # Format the y-axis to display population in billions
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: f'{x / 1e9:.2f}B'))

    plt.show()
    return

line_chart_analysis()

def pie_chart_analysis():
    """ This function handles pie chart analysis """
    # Group the data by continent and sum the 2022 population
    continent_population_2022 = df.groupby('Continent')['2022 Population'].sum()

    # Define custom colors for each continent
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(continent_population_2022, labels=continent_population_2022.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('2022 Population by Continent')

    # Add a legend
    plt.legend(continent_population_2022.index, title="Continents", loc="center left", bbox_to_anchor=(1, 0.5))

    plt.show()
    return

pie_chart_analysis()



def barh_chart_analysis():
    """ This function handles horizontal bar chart analysis """
    # Sort the data by 2022 Population and get the top 5 countries
    top_5_countries = df.sort_values(by='2022 Population', ascending=False).head(10)
    plt.figure(figsize=(10, 6))

    # Assign different colors to each country
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'violet', 'green', 'red', 'purple',]

    # Create horizontal bar plots for the top 5 countries in descending order
    for i, (country, population) in enumerate(zip(top_5_countries['Country/Territory'], top_5_countries['2022 Population'])):
        plt.barh(country, population, color=colors[i], label=country)

    plt.xlabel('Population (Billions)')
    plt.ylabel('Country')
    plt.title('Top 5 Most Populated Countries in 2022')
    plt.legend()

    # Format the x-axis to display population in billions
    plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: f'{x / 1e9:.2f}B'))
    plt.tight_layout()

    # Invert the y-axis to display the highest population at the top
    plt.gca().invert_yaxis()
    plt.show()
    return

barh_chart_analysis()

if __name__ == "__main__":
    line_chart_analysis()
    pie_chart_analysis()
    barh_chart_analysis()