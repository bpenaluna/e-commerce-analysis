<h1>Online Retail Dataset Analysis</h1>

<h2>Dashboard</h2>

An interactive dashboard built using Microsoft Power BI visualises business KPIs to monitor revenue, customer base, churn and more.

Key takeaways:

<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>

<h3>Screenshots of the interactive dashboard:</h3>

<img width="1336" height="750" alt="dashboard-screenshot-1" src="images/Dashboard-screenshot.png" />

<h2>Similar Customers</h2>

<h3>K-means Clustering</h3>

K-means clustering is an unsupervised machine learning algorithm that creates a predetermined (k) number of groups (clusters) of points base on one or more variables.

Inertia is a measure of the spread of the points in each cluster. Lower Inertia means the distance between the points in each group is smaller, which in this case means the customers have more similar spending patterns to other customers in the same group compared to if the inertia was higher. The elbow method is a heuristic method of finding the 
"best" k, looking for a value where the decrease in inertia is marginal.

<img width="1336" alt=elbow method src="images/elbow_method.png">

The customers were grouped into 7 categories, with the K-means algorithm trained on the following engineered features:

<ul>
    <li><strong>recency</strong>: Number of days since the customers last purchase.</li>
    <li><strong>frequency</strong>: Number of transactions the customer has made.</li>
    <li><strong>monetary</strong>: Total amount spent by the customer.</li>
</ul>

The distributions of each cluster for each of the variables defined above are given below.

<img width="1336" alt=box plot of recency src="images/boxplot_recency.png">
<img width="1336" alt=box plot of frequency src="images/boxplot_frequency.png">
<img width="1336" alt=box plot of monetary src="images/boxplot_monetary.png">

<h2>Dataset</h2>
Dataset obtained from <a href='https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business'>Kaggle</a>
