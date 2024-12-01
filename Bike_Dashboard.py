# Step 1: Organize and Import the Data
# Step 1: Set up the environment and import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
bike_data = pd.read_csv('merged_citibike_weather.csv', low_memory=False)
weather_data = pd.read_csv('weather_2022.csv')

# Display the first few rows to confirm successful loading
print("Bike Data:")
print(bike_data.head())
print("\nWeather Data:")
print(weather_data.head())

# Step 3: Create a random sample of the bike data
sample_size = 25 * 1024 * 1024  # Approximate maximum file size: 25 MB
random_sample = bike_data.sample(frac=0.1, random_state=32)

# Save the sampled data
random_sample.to_csv('bike_sample.csv', index=False)

print("Sample created and saved as 'bike_sample.csv'")

# Load the sampled data with low_memory=False
df = pd.read_csv('bike_sample.csv', low_memory=False)

import streamlit as st
import pandas as pd

# Load the sampled data
df = pd.read_csv(
    'bike_sample.csv', 
    low_memory=False  # Suppresses the DtypeWarning
)

# Sidebar for page navigation
st.sidebar.title("Citi Bike Dashboard")
page = st.sidebar.selectbox("Choose a Page:", ["Intro", "Dual-Axis Chart", "Popular Stations", "Map", "Recommendations"])

# Page Content
if page == "Intro":
    st.title("Welcome to the Citi Bike Dashboard!")
    st.write("Explore the data and gain insights into Citi Bike usage.")
elif page == "Dual-Axis Chart":
    st.write("Dual-Axis Chart page under construction.")
elif page == "Popular Stations":
    st.write("Popular Stations page under construction.")
elif page == "Map":
    st.write("Map visualization page under construction.")
elif page == "Recommendations":
    st.write("Recommendations page under construction.")


# Step 5: Intro Page
if page == "Intro":
    st.title("Citi Bike Dashboard")
    st.image("citibike_orig.png", caption="Citi Bike Rides in Action", use_container_width=True)
    st.markdown("""
    ## Welcome to the Citi Bike Dashboard

    Citi Bike is New York City's premier bike-sharing system, offering a sustainable and convenient way to navigate one of the busiest cities in the world. Every day, thousands of people rely on Citi Bike for commuting, leisure, and exploration. This dashboard is your gateway to understanding the wealth of data generated by Citi Bike rides across the city.

    ### What This Dashboard Offers:
    This dashboard is designed to provide you with insightful analyses of Citi Bike usage patterns, key performance metrics, and trends over time. By exploring the data, you can discover how weather conditions, popular stations, and user preferences influence Citi Bike activity.

    ### Key Features:
    - **Dual-Axis Charts**: Compare key metrics like ride duration and user demographics across different time periods.
    - **Popular Stations**: Identify hotspots where Citi Bike sees the highest demand.
    - **Interactive Maps**: Visualize the locations of rides, stations, and clusters of activity across the city.
    - **Data-Driven Recommendations**: Explore suggestions for improving bike-sharing efficiency and user satisfaction.

    ### Why Citi Bike Data Matters:
    Bike-sharing systems like Citi Bike are an essential part of urban mobility, helping to reduce traffic congestion, promote fitness, and lower carbon emissions. Understanding the trends and patterns in Citi Bike usage can help city planners, businesses, and the community make data-driven decisions that enhance the overall biking experience.

    ### Navigate and Explore:
    Use the sidebar to navigate through the various pages of this dashboard:
    - **Introduction**: Learn about the purpose and features of this dashboard.
    - **Dual-Axis Chart**: Dive deep into comparative analysis of Citi Bike data.
    - **Popular Stations**: Discover the most frequently used stations.
    - **Map**: Visualize bike rides and station locations across the city.
    - **Recommendations**: Explore actionable insights for improving bike-sharing operations.

    Citi Bike is more than just a transportation option – it's a glimpse into the future of sustainable urban living. Dive into the data and uncover the stories hidden within!
    """)

# Step 6: Dual-Axis Line Chart
# Import required libraries
import matplotlib.pyplot as plt  # Fix for the plt error
import seaborn as sns  # For enhanced visualizations

if page == "Dual-Axis Chart":
    # Heading for the Dual-Axis Chart Page
    st.title("Dual-Axis Line Chart: Temperature vs. Ride Count")
    
    # Introduction to the Chart
    st.markdown("""
    ### Understanding the Relationship Between Temperature and Ride Count
    This chart explores how the number of Citi Bike rides varies with temperature. The dual-axis line chart combines:
    - **Ride Count**: Number of rides for a given temperature (left y-axis).
    - **Temperature**: Temperature in degrees Celsius (right y-axis).
    """)

    # Step 1: Data Preparation
    temp_ride_data = df.groupby('Temperature').size().reset_index(name='Ride_Count')

    # Step 2: Plot Creation
    fig, ax1 = plt.subplots(figsize=(10, 6))  # Create figure with primary axis
    ax2 = ax1.twinx()  # Add a secondary y-axis

    # Plot Ride Count on the primary axis
    sns.lineplot(
        x='Temperature', 
        y='Ride_Count', 
        data=temp_ride_data, 
        ax=ax1, 
        label='Ride Count', 
        color='blue'
    )

    # Plot Temperature on the secondary axis
    sns.lineplot(
        x='Temperature', 
        y='Temperature', 
        data=temp_ride_data, 
        ax=ax2, 
        label='Temperature', 
        color='red'
    )

    # Customize Axes
    ax1.set_ylabel('Ride Count', color='blue')  # Left y-axis label and color
    ax2.set_ylabel('Temperature (°C)', color='red')  # Right y-axis label and color
    ax1.set_xlabel('Temperature (°C)')  # x-axis label

    # Add Titles and Legends
    plt.title('Temperature vs. Ride Count')  # Chart title
    ax1.legend(loc='upper left')  # Legend for Ride Count
    ax2.legend(loc='upper right')  # Legend for Temperature

    # Display the Chart in Streamlit
    st.pyplot(fig)

    # Add Interpretation
    st.markdown("""
    ### Interpretation:
    - Ride counts increase or decrease significantly based on temperature changes.
    - This chart helps identify optimal temperature ranges for high Citi Bike usage, providing valuable insights for both users and planners.
    """)


#Step 7: Popular Stations Bar Chart
if page == "Popular Stations":
    # Page Title
    st.title("Popular Stations: Where Riders Begin Their Journeys")
    
    # Step 1: Calculate Most Popular Start Stations
    st.markdown("""
    ### Exploring the Top 10 Start Stations
    This chart shows the most frequently used starting stations in the Citi Bike system. Understanding these stations helps identify high-demand locations.
    """)
    
    # Get the top 10 popular start stations
    popular_stations = df['start_station_name'].value_counts().head(10)

    # Step 2: Plot the Data
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis for plotting
    popular_stations.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')  # Bar chart
    
    # Add Titles and Labels
    ax.set_title("Most Popular Start Stations", fontsize=16)
    ax.set_xlabel("Station Name", fontsize=12)
    ax.set_ylabel("Ride Count", fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Step 3: Display the Chart in Streamlit
    st.pyplot(fig)  # Render the matplotlib figure in the Streamlit app

    # Step 4: Add Interpretation Section
    st.markdown("""
    ### Interpretation:
    - This chart highlights the top 10 starting stations based on ride counts.
    - These stations often serve as hubs for commuters or tourists, indicating their strategic importance in the Citi Bike network.
    - Insights from this chart can help with resource allocation, such as bike availability or station maintenance.
    """)

# Step 8: Kepler.gl Map Placeholder
import streamlit as st
import pydeck as pdk
import pandas as pd

if page == "Map":
    # Page Title
    st.title("Kepler.gl Map: Citi Bike Trip Visualizations")

    # Description for the page
    st.markdown("""
    ### Visualization of Citi Bike Trips on the Map
    This map visualizes the trips made using the Citi Bike service. You can interact with the map to explore the rides and their geographical distribution.
    """)

    # Example: Load the Citi Bike data (make sure to replace with your actual file or dataframe)
    # Assuming `df` contains Citi Bike trip data with latitudes and longitudes
    df = pd.read_csv('bike_sample.csv')  # Adjust this to the actual path of your data

    # Step 1: Setup the data
    # Here, using 'start_lat' and 'start_lng' as an example
    # You can replace it with the appropriate columns from your dataset
    data = df[['start_lat', 'start_lng']].dropna()  # Clean up the data (drop NaN)

    # Step 2: Define the Pydeck Map Layer
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=data['start_lat'].mean(),  # Center the map around the average latitude
            longitude=data['start_lng'].mean(),  # Center the map around the average longitude
            zoom=11,  # Zoom level
            pitch=0  # Tilt angle of the map
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',  # Type of map layer
                data,  # Data for the layer
                get_position='[start_lng, start_lat]',  # Coordinates for the points
                get_radius=100,  # Radius size of the scatterplot points
                get_fill_color='[200, 30, 0, 160]',  # Point color (RGBA)
                pickable=True  # Enable picking (hovering over points for details)
            )
        ]
    )

    # Step 3: Render the Map in Streamlit
    st.pydeck_chart(deck)

    # Step 4: Optional: Add some more interaction or explanation
    st.markdown("""
    ### Interact with the Map:
    You can zoom in and out, and click on individual dots to get more information about each trip.
    """)

#Step 9: Membership Analysis Chart
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming `df` is your DataFrame containing Citi Bike data

if page == "Additional Chart":
    # Title for the page
    st.title("Additional Chart: Membership Analysis")
    
    # Step 1: Count the number of 'member_casual' entries
    member_count = df['member_casual'].value_counts()  # Count of 'member' vs 'casual' riders
    
    # Step 2: Create a bar plot to visualize the count of 'member' vs 'casual'
    member_count.plot(kind='bar', figsize=(10, 6))  # Plot bar chart
    
    # Step 3: Customize plot with title and labels
    plt.title("Member vs Casual Riders")
    plt.xlabel("Rider Type")  # X-axis label
    plt.ylabel("Count")       # Y-axis label
    
    # Step 4: Display the plot in Streamlit
    st.pyplot(plt)  # Use Streamlit's `pyplot` function to render the plot

    # Step 5: Interpretation text
    st.markdown("### Interpretation: Members dominate the Citi Bike usage.")

    import streamlit as st

# Assuming the variable 'page' is already defined and is controlling the page navigation.

if page == "Recommendations":
    # Title of the Recommendations page
    st.title("Recommendations")
    
    # Step 1: Display a markdown section with the key recommendations
    st.markdown("""
    ### Key Recommendations:
    
    1. **Increase bike supply at popular stations during peak hours.**
       - Popular stations tend to see a higher demand during peak times. By increasing bike availability at these stations, you can reduce wait times and improve user satisfaction.
    
    2. **Implement dynamic pricing during extreme weather conditions.**
       - In extreme weather conditions (either very hot or cold), bike usage may drop. Implementing dynamic pricing can help manage demand and encourage more users to rent bikes during off-peak weather conditions.
    
    3. **Focus on improving member retention strategies.**
       - While casual riders make up a significant portion of the user base, retaining members should be a key focus. Offering incentives, discounts, or loyalty programs can help increase member retention and ensure steady ridership.

    """)
