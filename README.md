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
The main project scripts are in the "scripts" directory. Exceptionally, "app.py" is in main project directory. The main constituting scripts are as follows

* **nltk_utils.py:** 

* **model.py:** 

* **train.py:** 

* **chat.py:** T

* **app.py:** 


## Directory Structure

```bash
├── data                             # Application files
|  ├── intent.json                   # Application script
├── model                            # Configuration files
|  ├── config.yaml                   # Configuration file  
├── scripts                          # Data files ()   
|  ├── restnt_data.csv.dvc           # Tracking File of Original dataset (DVC)  
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── static                           # Dictionary Files
|  ├── locations_dict.pkl            # Locations dictionary
|  ├── rest_type_dict.pkl            # Resaturant type dictionary
├── templates                        # Documentation Files
|  ├── HDL.pdf                       # High-Level Design document
|  ├── LLD.pdf                       # Low-Level Design document
|  ├── project_report.pdf            # Detailed Project Report 
├── app.py                           # DVC pipelines
├── chat.py                          # Docker file for generating containers
├── requirements.txt                 # Required libraries
├── LICENSE                          # License
├── README.md                        # About repository
```


