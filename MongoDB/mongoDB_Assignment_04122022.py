# import pandas module
import pandas as pd
import pymongo

# MongoDB connection string
dbConn=pymongo.MongoClient("mongodb://localhost:27017/")

# database creation
dbname = 'ineuron'
db=dbConn[dbname]

# collection name creation 
collection_name="admissin_details"
collection=db[collection_name]

# extracting admission data 
admission_df=pd.read_csv("https://raw.githubusercontent.com/vigneshk/Admission-Dataset/master/Admission.csv")

# data preparation (Json format)
admission_df.reset_index(inplace=True)
data_dict = admission_df.to_dict("records")

# insering data into mongoDB collection 
collection.insert_many(data_dict)
