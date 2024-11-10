# Proyect-3-DataAnalysis :floppy_disk:

This project is a comprehensive data analysis of course reviews using Python. The analysis includes various visualizations to explore patterns in ratings, review distributions, and course popularity. The project leverages
JustPy and HighCharts for interactive and web-based visualization. The dataset used in this project, reviews.csv, contains course reviews with timestamps, ratings, and course names.

## Features
- **Data Loading and Preprocessing:** The project starts by reading and processing review data.
- **Interactive Visualizations:** Generates a total of 7 distinct graphs to showcase different aspects of the data.
- **Web-Based Interface:** Uses JustPy to display visualizations interactively on a web page.
- **Easy Customization:** The charts and layouts are flexible, allowing easy customization.

## Requirements
- Python 3.x
- JustPy
- Pandas

## Dataset
- File: reviews.csv
- Columns:
  - **Timestamp** - Date of the review
  - **Course Name** - Name of the course reviewed
  - **Rating** - Rating given to the course (1-5 scale)

## Explanation
- **Data Loading and Aggregation:** The data is read from reviews.csv, and then grouped by course name, counting the total ratings per course.
- **Chart Definition:** I used the website [Highcharts](https://www.highcharts.com/?_gl=1*1gelqi3*_up*MQ..&gclid=Cj0KCQiArby5BhCDARIsAIJvjIQ-XrxE4-whwvzKVOGNa_-epyAjpwLWPbWznfXDfcNFmHO_jtTFDEkaApqbEALw_wcB) to find a awesome charts to include
- **Tooltip and Data Labels:** Tooltips show percentage values, and data labels display percentages only for segments greater than 10%.
- **Data Insertion:** The hc_data array is populated with the course names and their respective rating counts. This data is then assigned to the chart options for rendering.
- **Web Interface:** The function app() creates a Quasar-based web page using JustPy, where the chart and text elements are embedded.

## Visualizations
The project includes 7 different visualizations. Each graph focuses on a unique aspect of the dataset, helping to reveal trends and insights.



- **Average Rating by Day:** Shows how ratings vary over day for each course.
  
  ![Average Rating by Day](/screenshots/1-av-rat-day.png)
  
- **Average Rating by Week:** Shows how ratings vary over week for each course.

  ![Average Rating by Week](/screenshots/2-av-rat-week.png)
  
- **Average Rating by Month:** Shows how ratings vary over months for each course.

  ![Average Rating by Month](/screenshots/3-av-rat-month.png)
  
- **Amount of Rewies by Month:** Shows amount of rewies vary over months for each course.

  ![Amount Ratingg by Month](/screenshots/4-av-rat-crs-month.png)
  
- **Amount of Rewies by Month:** Shows amount of rewies vary over months for each course with another chart.

  ![Amount Ratingg by Month](/screenshots/5-av-rat-crs-month-stream.png)

-  **Number of ratings by Course:** Shows amount of rewies vary over months for each course. Pie chart

  ![Amount Ratingg by Month Pie Version](/screenshots/7-av-mont-pie.png)
  
- **The Happiest Day!:** Shows the day of the week with better rewiews. Of course it's Friday! :grinning:
  
  ![Happiest Day of the Week](/screenshots/6-hap-day.png)

Each chart provides a unique perspective on the data, allowing for a detailed analysis of course reviews.

## Contact
For any questions or feedback, please contact [rmartinez28590@gmail.com].

## Thanks for making it to the end!
 Share if you liked it :smile:
  
