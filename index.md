Link to this GitHub repository: <https://github.com/WWMarin/Cloud-Data-Ingestion-and-Analysis>
# Cloud Data Ingestion and Analysis
by [Werner W. Marin](https://github.com/WWMarin)
## Summary
This is an example project in which we access a cloud database via Python and run scripts to analyse the data using the Pandas library.

The cloud service used was Google Cloud Platform's Cloud SQL running a PostgreSQL database, and the data was extracted, transfered and loaded using Tableu and pgAdmin.

All the scripts were written in Jupyter Notebook, to allow for easy understanding of the process through which the data was manipulated.

## QuickStart
There are three options to viewing the scripts and their outputs. The first is to download the project, install Jupyter Notebook and the dependencies, and then run locally.

The second is to access the scripts on [Jupyter Notebook Viewer](https://nbviewer.jupyter.org/). The downside to this option is that you cannot interact with the scripts. It simply presents a render of the notebook file.

Finally, you can view an interactive docker image of the notebooks on [Binder](https://mybinder.org/). This is the most convenient option, as it allows to interact with the scripts without any setup.

### Running Locally
#### Prerequisites
- [Python](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)

To run the project locally, download the project and open the folder in a terminal. Then, run ``pip install -r requirements.txt``. This will install the necessary Python libraries on your computer. Namely, the necessary libraries are:
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [seaborn](https://seaborn.pydata.org/)

After these libraries are successfully installed, run ``jupyter-notebook``. This will open the Jupyter Notebook file browser on your web browser. If it does not open automatically, it is usually accessed at <localhost:8888/tree>.

Then, navigate to the project folder and into ``./project/``. There you will find the jupyter notebook files for execution.

### Viewing Online
To view the notebooks online, simply click on the respective links for each script for Jupyter Notebook Viewer, or the Binder badge:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/)

to run them on Binder.

## Project Architecture
The database was structured in the following manner:

![Database Model Diagram][dataModel]

The database was created in PostgreSQL for it's scalability and closer adherence to standard SQL over MySQL.

For hosting, the elected platform was Google Cloud Platform's Cloud SQL. While Cloud SQL's support for PostgreSQL is currently in beta, it proved sufficient for this project.

For uploading the data to the server, the software used was Tableau, and eventual simple queries were made in pgAdmin.

![Tableau Dashboard][tableauDashboard]

Further elaboration on decisions made while writing the scripts are written in the notebooks.

## Data Analysis
### Analysis 1
In this analysis we find the number of sales order details for each sales order, filtering for sales orders with three or more detail lines.

[Link for this notebook on Nbviewer](https://nbviewer.jupyter.org/github/WWMarin/Cloud-Data-Ingestion-and-Analysis/blob/main/project/Analysis1.ipynb)

Launch this notebook on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/wwmarin-cloud-d-on-and-analysis-n2rpv461/notebooks/project/Analysis1.ipynb)

![Analysis 1][analysis1]

### Analysis 2
In this analysis we find the three best selling products grouped by the number of days it takes to manufacture them.

[Link for this notebook on Nbviewer](https://nbviewer.jupyter.org/github/WWMarin/Cloud-Data-Ingestion-and-Analysis/blob/main/project/Analysis2.ipynb)

Launch this notebook on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/wwmarin-cloud-d-on-and-analysis-n2rpv461/notebooks/project/Analysis2.ipynb)

![Analysis 2][analysis2]

### Analysis 3
In this analysis we find a list of client names and how many orders they each made.

[Link for this notebook on Nbviewer](https://nbviewer.jupyter.org/github/WWMarin/Cloud-Data-Ingestion-and-Analysis/blob/main/project/Analysis3.ipynb)

Launch this notebook on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/wwmarin-cloud-d-on-and-analysis-n2rpv461/notebooks/project/Analysis3.ipynb)

![Analysis 3][analysis3]

### Analysis 4
In this analysis we find a list of order quantity by product and order date.

[Link for this notebook on Nbviewer](https://nbviewer.jupyter.org/github/WWMarin/Cloud-Data-Ingestion-and-Analysis/blob/main/project/Analysis4.ipynb)

Launch this notebook on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/wwmarin-cloud-d-on-and-analysis-n2rpv461/notebooks/project/Analysis4.ipynb)

![Analysis 4][analysis4]

### Analysis 5
In this analysis we find the ID, date and total due for instances of sales orders made during September 2011 where the total due is over 1000, by descending order of total due.

[Link for this notebook on Nbviewer](https://nbviewer.jupyter.org/github/WWMarin/Cloud-Data-Ingestion-and-Analysis/blob/main/project/Analysis5.ipynb)

Launch this notebook on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/wwmarin-cloud-d-on-and-analysis-n2rpv461/notebooks/project/Analysis5.ipynb)

![Analysis 5][analysis5]

## Conclusion
This project is hosted at <https://github.com/WWMarin/Cloud-Data-Ingestion-and-Analysis>

[dataModel]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/dataModel.png
[tableauDashboard]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/tableauDashboard.png
[analysis1]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/analysis1.png
[analysis2]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/analysis2.png
[analysis3]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/analysis3.png
[analysis4]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/analysis4.png
[analysis5]: https://raw.githubusercontent.com/WWMarin/Cloud-Data-Ingestion-and-Analysis/main/assets/analysis5.png
