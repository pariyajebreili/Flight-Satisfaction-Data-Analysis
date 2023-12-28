# Define a mapping for the encoding
gender_mapping = {'Male': 0, 'Female': 1}
Customer_Type_mapping={'Loyal Customer':0, 'disloyal Customer':1}
Type_of_Travel_mapping ={'Personal Travel':0, 'Business travel':1}
satisfaction_mapping={'satisfied':1, 'neutral or dissatisfied':0}



# Create a new column 'Gender_Code' with numeric encoding
new_dataset_flight_distance['Gender_Code'] = new_dataset_flight_distance['Gender'].map(gender_mapping)

new_dataset_flight_distance = new_dataset_flight_distance.drop('Gender', axis=1)
# Rename the 'Gender_Code' column to 'Gender'
new_dataset_flight_distance = new_dataset_flight_distance.rename(columns={'Gender_Code': 'Gender'})




# Create a new column 'Customer_Type_Code' with numeric encoding
new_dataset_flight_distance['Customer Type_Code'] = new_dataset_flight_distance['Customer Type'].map(Customer_Type_mapping)

new_dataset_flight_distance = new_dataset_flight_distance.drop('Customer Type', axis=1)
# Rename the column 
new_dataset_flight_distance = new_dataset_flight_distance.rename(columns={'Customer Type_Code': 'Customer Type'})




# Create a new column 'Customer_Type_Code' with numeric encoding
new_dataset_flight_distance['Type of Travel_Code'] = new_dataset_flight_distance['Type of Travel'].map(Type_of_Travel_mapping)

new_dataset_flight_distance = new_dataset_flight_distance.drop('Type of Travel', axis=1)
# Rename the column 
new_dataset_flight_distance = new_dataset_flight_distance.rename(columns={'Type of Travel_Code': 'Type of Travel'})


# Create a new column 'satisfaction_Code' with numeric encoding
new_dataset_flight_distance['satisfaction_Code'] = new_dataset_flight_distance['satisfaction'].map(satisfaction_mapping)

new_dataset_flight_distance = new_dataset_flight_distance.drop('satisfaction', axis=1)
# Rename the column 
new_dataset_flight_distance = new_dataset_flight_distance.rename(columns={'satisfaction_Code': 'satisfaction'})


