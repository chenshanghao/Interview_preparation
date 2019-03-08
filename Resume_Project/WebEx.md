# WebEx Meeting Data Analysis

## 1. Daily Work (WebEx Meeting Analysis)

In order to output the analysis dashboard,  there are four steps on Platfora.

#### 1) Define Data Sources to Connect to Raw Data in Hadoop.
Usually, I need to write SQL on Hue to generate the required raw data.

#### 2) Create Datasets to describe the structured of the data.

#### 3) Build a Lens to pull data from Hadoop into Platfora
It submits a series of **MapReduce jobs** to Hadoop, collects the results, and brings the results back into Platfora. From the perspective of an ETL workflow, the lens build is the load part of the process

Lens build is time-consuming and one lens may depend on multiple Datasets. Therefore, I should carefully choose how to build a lens for future analyze.

#### 4) Create vizboards to analyze and visualize the data
Visualizations can take various forms such as **charts, graphs, maps or cross-table**. 
Then I can share the dashboard with relevant teams to help them reduce workloads.

## 2. WebEx Meeting KPP
KPP = Key Performance Parameters

The most important KPP we care about is **JMT(means join meeting time)** which means how long did a customer actually join a WebEx meeting after clicking the join meeting button from WebEx. The JMT consists of **ClientJMT**, **CbServerJMT**, **PageJMT**, **PagePluginJMT**, **gpyDoneJMT** and **GpcJMT**. Different teams are responsible for different JMT.

My work is helping them to analyze JMT on our data analysis platform(Platfora). For example, the **change trend** of JMT on different WebEx version, operation system, browser, region and so on.

The **visualization vizborad** can help them find the potential problem for their JMT which may help them debug or optimize the software.


## 3. "Data Extraction and Migration", difficulties you met and how to solve it.

We had a **test and production environment** for our data platform. Firstly, data analysists usually create dashboards **on the test environment**. After testing, we have to rebuild the dashboard on the production environment. A migration tool can help them do this job quickly.

At that time, Platfora was **acquired** by another company named Workday. So, Ploatfora would not be updated and the customer service response is slow. 

From the latest version of the document, it supports **REST API** but did not have detailed document for this. So I have to do this step by step.
**1).** Called the API successfully to download the JSON file for a simple dataset, lens or vizboard. The JSON file represents the structure for a dataset, lens, vizboard.
**2).** Understand JSON file meaning and then change then content of it. Finally, put the JSON file to production environment and created a simple dataset.
**3).** Successfully download a dataset/lens/vizboard JSON file from test environment, change the content and then put it to production environment.
**4).** Finally, successfully do the same job for a complicated dataset/lens/vizboard.

The whole process like a cycle of **reading, understanding, testing**. Also, I have to do many tedious works, like naming rules unification on testing and production environment.

## 4. "Fault Preduction System": what does data look like? and what is the targeted "fault"

#### 1. Label The Data
Fault WebEx meeting means that JMT is larger than the experience value. Since JMT has many different components, different larger JMT will lead to label this customer JMT meeting as fault JMT.

#### 2. Why you choose Random Forest
When I first tried to do this, I plan to use the decision tree to predict fault WebEx meeting since it is easy to understand and interpret.

Firstly, I extracted the WebEx Meeting log files from different data sources since different team store log fires in different ways. Then, I transformed and loaded the data to Python Pandas DataFrame and each row contained all the features for a meeting. 

In the beginning, the number of the feature is too large with many problems like the same **repeat features**, **,categorical features, unique value features, low variance features**, and **numeric features**. Therefore, it is better to use the Random Forest.

Finally, I can set the **hyperparameters** for the random forest to improve the training data results. The hyperparameters includes **‘max_features’**, **‘max_depth’**, **‘min_samples_split’**, **‘min_samples_leaf’**, **‘n_estimatiors’**, **‘bootstrap’**.


From this project, I realized that **data engineering** is the most important part when applying machine learning in the real world. 

Some part of work can be done by myself like drop **the repeat features**, **unique value features**, and **low variance features**. When training the model, I found that **category encoding** is the key point. **One-hot encoding** is not a good solution compared to encode by experience engineer. 

Therefore, as a data engineer or a data scientist, I should be not only familiar with **different machine learning algorithms** but also **understanding the data**.













