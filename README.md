Chatbot-for-Selling-Products

## Demo 
The chatbot demo is available in https://youtu.be/u98UvCc9tx8

## Introduction
A chatbot is developed for cheerful conversations; that present products and fancy offers. This compels buying and builds customer relations. Further, chatbot provides resource effectiveness and remote ordering.

## Problem Statement
Operational requirements in a business increase cost, reduce efficiency and speed. Transparency in operation is unachievable. Therefore, providing and maintaining a quality service is very challenging. 

## Goal
The purpose of the project is to build customer relation; by effectively presenting products and offers. Animating pleasant feeling in customers promotes  buying. Also, this aids in reducing capital required for service and marketing. 

## System Environment
![](https://forthebadge.com/images/badges/made-with-python.svg)



[<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_656e174b12c49be1cfb4723a938ea43e/pytorch.png" width=200>](https://pytorch.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     [<img target="_blank" src="https://static.wixstatic.com/media/ff7edb_c808984b12a0496da4d99066b5e7126b~mv2.png/v1/fill/w_420,h_140,al_c,lg_1,q_85,enc_auto/NLP%20NLTK%20Logo.png" width=200>](https://www.nltk.org/)     [<img target="_blank" src="https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png" width=200>](https://flask.palletsprojects.com/en/2.1.x/)     [<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwAMVIYFU7fBkYkhI_BGVqizydCiwjRIJvjQ&usqp=CAU" width=200>](https://flask.palletsprojects.com/en/2.1.x/)


## Technical Description
The main project scripts are in the "src" directory. Exceptionally, "app.py" is in app directory. The main constituting scripts are as follows

* **get_data.py:** This script downloads the data as **"restn_data.csv"** (The data is not present in the repository due to upload size restrictions of Github). NaNs are removed. Cleaned dataset is saved as **"cleaned_data.csv"**. Locations and restaurant type dictionaries are saved as **"locations_dict.pkl"** and **"rest_type_dict.pkl"**. These dictionaries are later used by Streamlit app.

* **data_analysis.py:** This script obtains various visualizations of the dataset. These visualizations are present in the **"Visualization"** directory. 

* **prepare_data.py:** The script converts the required features to **categorical** variables. Subsequent outliers are determined using Grubb's Test. These outliers are removed and cleaned dataset is saved as **"prepared_data.csv"**.   

* **split_data.py:** The cleaned dataset is split using stratified sampling. This ensures the fair splitting. Train data and test data are respectively saved as **"train_set.csv"** and **"test_set.csv"**. Labels are separated from train and test sets and saved as **"train_labels.csv"** and **"test_labels.csv"**.

* **model_data.py:** The train set is modelled using data science models. Accuracy of all the models is verified using test set. Henceforth, the best model is selected. The feature selection of the best model is optimized to increase the accuracy to **91.7%**. This model is saved as **"model.pkl"**. 

* **app.py:** The script develops a Streamlit app; that accepts six user inputs to predict the restaurant rating. 
 
* **run_project.py:** The script runs all the project scripts sequentially (including applcation). Therefore, entire project is executed with this script.  

**get_data_util.py**, **data_analysis_util.py**, **prepare_data_util.py**, **split_data_util.py**, **model_data_util.py** and **utility.py** delcare vital functions that are required by respective scripts.   



## Directory Structure

```bash
├── app                              # Application files
|  ├── app.py                        # Application script
├── config                           # Configuration files
|  ├── config.yaml                   # Configuration file  
├── data                             # Data files ()   
|  ├── restnt_data.csv.dvc           # Tracking File of Original dataset (DVC)  
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── dict                             # Dictionary Files
|  ├── locations_dict.pkl            # Locations dictionary
|  ├── rest_type_dict.pkl            # Resaturant type dictionary
├── doc                              # Documentation Files
|  ├── HDL.pdf                       # High-Level Design document
|  ├── LLD.pdf                       # Low-Level Design document
|  ├── project_report.pdf            # Detailed Project Report 
├── log                              # Log files
|  ├── get_data.log                  # "get_data.py" script logs
|  ├── data_analysis.log             # "data_analysis.py" script logs
|  ├── prepare_data.log              # "prepare_data.py" script logs 
|  ├── split_data.log                # "split_data.py" script logs 
|  ├── model_data.log                # "model_data.py" script logs 
├── model                            # Model Files
|  ├── model.pkl                     # Saved model (This file is not present in Github, it is created by running project) 
├── src                              # Main project scripts 
|  ├── get_data.log                  # Dataset acquistion and cleaning script
|  ├── data_analysis.log             # Dataset analysis and visualization script
|  ├── prepare_data.log              # Dataset preperation script
|  ├── split_data.log                # Dataset splitting script  
|  ├── model_data.log                # Dataset modelling script
├── visualizations                   # Dataset visualizations
|  ├── book_table_vs_rating.png      # Bookings vs ratings figure
|  ├── cities_vs_rating.png          # Cities vs ratings figure
|  ├── correlation_heatmap.png       # Feature correlations figure
|  ├── cuisines_vs_rating.png        # Cuisines vs rating figure 
|  ├── feature_importances.png       # Best model feature importance figure
|  ├── online_order_vs_rating.png    # Online oreder vs rating figure
|  ├── rest_type_vs_rating           # Rest-type vs rating figure 
|  ├── top_cuisines.png              # Top cuisines figure
├── requirements.txt                 # Required libraries
├── dvc.yaml                         # DVC pipelines
├── Dockerfile                       # Docker file for generating containers
├── requirements.txt                 # Required libraries
├── LICENSE                          # License
├── README.md                        # About repository
```


