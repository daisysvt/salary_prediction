import streamlit as st


def show_analysis_page():
    st.title("Salary Analysis")

    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/image/analysis_page.png?raw=true"
    )

    st.write("""### Average Salary by Gender""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/average_salary_by_gender.png?raw=true"
    )
    st.write(
        'The x-axis labeled "Gender" has two categories: "Male" and "Female". The y-axis labeled "Average Salary" is scaled from 0 to 80, with tick marks at increments of 10. The bar for "Male" is taller than the bar for "Female", indicating that the average salary for males is higher than the average salary for females in this dataset. The exact difference in salary cannot be determined from the graph, but it appears to be somewhere around 20 to 30 units on the y-axis.'
    )

    st.write("""### Top 10 City Distribution""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/city_distribution.png?raw=true"
    )
    st.write(
        "This bar chart shows the frequency of certain cities, with Istanbul having the highest frequency, followed by Ankara and Izmir. Other cities like Kocaeli, Bursa, Antalya, and more have progressively lower frequencies. "
    )

    st.write("""### Average Salary by Work Type""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/mean_salary_by_work_type.png?raw=true"
    )
    st.write(
        "The chart suggests a trend where work arrangements with remote options (remote-hybrid, remote, and hybrid) have higher mean salaries compared to traditional office settings. The highest mean salaries are associated with roles that offer a combination of remote and hybrid work, while the lowest is for fully on-site (office) roles. This could reflect the increasing value and competitiveness of flexible work arrangements in the job market."
    )

    st.write("""### Highest Average Salary with Number of Technologies""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/highest_average_salary_with_technologies.png?raw=true"
    )
    st.write(
        "The chart illustrates that the highest average salary is associated with individuals who know 18 technologies, with a noticeable decrease as the number of known technologies declines. Interestingly, after the initial drop, the salary levels off and remains relatively consistent across the range from 10 to 6 technologies. It could suggest that beyond a certain threshold of technological expertise, the average salary does not significantly increase with knowledge of additional technologies."
    )

    st.write("""### Outlier Values by Salary""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/outlier_detection_scatter_plot.png?raw=true"
    )
    st.write(
        "The scatter plot displays converted salary data points and identifies outliers using Z-score, a statistical measure for outlier detection. The majority of data points cluster at the lower range of salaries, while outliers are dispersed across the index with higher salary values. These outliers significantly deviate from the typical salary range, suggesting they are exceptional cases. The index may represent individual respondents, companies, or entities in a dataset."
    )

    st.write("""### Top 10 Cities by Highest Average Salaries""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/top_10_cities_salary.png?raw=true"
    )
    st.write(
        "This bar chart lists the top 10 cities with the highest average salary, with the first city having the highest average salary and the last city having the lowest within this top 10 ranking. All cities are represented with an asterisk, which suggests that their full names are not displayed, possibly due to privacy reasons or space constraints in the visualization. The average salary decreases from left to right, indicating that while these cities are the top earners, there is a range within their average salaries."
    )

    st.write("""### Frequency of Top 10 Positions""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/top_10_positions_frequency.png?raw=true"
    )
    st.write(
        "The vertical bar chart represents the frequency of the top 10 positions, likely within a specific sector, like technology. Backend developer positions have the highest frequency, followed by full-stack and front-end developers. Team leads and mobile application developers (Android) also have significant counts, but less than the top three. The remaining roles show a more modest frequency, suggesting they are less common or in less demand within the dataset s context. This could imply a greater need for backend and full-stack developers in the job market from which the data was taken."
    )

    st.write("""### Top 10 Positions by Highest Average Salaries""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/top_10_positions_salary.png?raw=true"
    )
    st.write(
        "The bar chart shows the top 10 positions with the highest average salaries. The position of Director of Software Development has the highest average salary, closely followed by CTO, Site Reliability Engineer, and Solution Architect. Engineering Manager and Research & Development are also among the top earners, albeit with slightly lower average salaries. The average salaries decrease progressively for Software Architect, Cloud Platform Engineer, Team Tech Lead, and AI Engineer. This indicates a hierarchy of average salaries among high-level technical positions."
    )

    st.write("""### Top 10 Fields by Highest Average Salaries""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/top_10_field_average_salary.png?raw=true"
    )
    st.write(
        'The bar chart depicts the top 10 fields with the highest average salary. Technology ("teknoloji") leads with the highest average salary, followed by the automotive ("otomobil") and finance ("finans") sectors. Other sectors like IoT, energy ("enerji"), construction & real estate ("inşaat & emlak"), agriculture ("tarım"), banking ("banka"), insurance ("sigorta"), and again automotive in a different spelling ("otomotiv"), follow with slightly lower average salaries. This suggests that technology-related fields tend to offer higher average salaries compared to other industries.'
    )

    st.write("""### Fruquency of Levels""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/frequency_of_levels.png?raw=true"
    )
    st.write(
        "The bar chart presents the frequency of different professional levels: Junior, Middle, and Senior. The frequency is highest for the Junior level, indicating there are more individuals or positions at this entry-level. The frequency for the Middle level is less, and it decreases further for the Senior level, which has the lowest frequency among the three. This could imply a typical career progression pyramid, with more entry-level positions available and progressively fewer positions at higher levels."
    )

    st.write("""### Correlation by Salary""")
    st.image(
        "https://github.com/alicenkbaytop/salary_prediction/blob/master/chart/correlation_matrix_heatmap.png?raw=true"
    )
    st.write(
        "In a correlation matrix, each cell represents the correlation coefficient between the variables on the x-axis and y-axis. The color scale on the right indicates the strength of correlation, where 1 is a perfect positive correlation (red), 0 indicates no correlation (white), and -1 indicates a perfect negative correlation (blue). Diagonal cells represent the correlation of variables with themselves, which is why they are perfect 1s (dark red)."
    )