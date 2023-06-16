# Machine Learning Models for Predicting Tourist Recommendations

## Description
This Machine Learning model is developed to provide predictions or recommendations for tourist attractions based on several factors such as category, domicile location, and age of the user. This model aims to provide more personalized and relevant recommendations to users, thus improving their travel experience.

## Training Data
This model uses training data consisting of users who have rated several tourist attractions. The training data includes the following features:
- User ID: The unique identity of the user
- Location: User's location (city)
- Destination Location: Location of tourist attractions visited by the user
- Category: Category of tourist attractions
- Rating: The rating value given by the user to the tourist attractions

This training data is used to train the model so that it can recognize patterns and correlations between these factors and the ratings given.

## Input Features
To get recommendations for tourist attractions, users are asked to enter several features as input, namely:
- User Id: The unique identity of the user
- Places Not Visited: The places that not visited yet by user
- Number of Recommendation: Number of recommendation result (default is 30)

These features help the model provide recommendations that are more personalized and in accordance with user preferences.

## Inference Process
After the user enters the input features, the model will perform an inference process to provide recommendations for tourist attractions. The model will analyze the user input features and look for patterns and correlations with training data that has been rated by other users. Based on this analysis, the model will provide recommendations for tourist attractions that best match the user's preferences.
