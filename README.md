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

# Recommendation API Docs
Dokumentasi API rekomendasi tempat wisata pada aplikasi Tresure.

## [ML] Predict without Location
Proses _request_ yang tidak menggunakan parameter lokasi (**location**) akan diberikan rekomendasi dengan wilayah atau kota yang beragam. _Response_ telah diurutkan berdasarkan kota.

_Body request_ dapat menggunakan **JSON** atau _**urlencoded**_.
### Method: POST
>```
>https://tresure-app-v5cbzwlk4q-uc.a.run.app/users/predict
>```
### Body (**raw**)

```json
{
    "username": "alip"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTAwMDAsInVzZXJuYW1lIjoiYWxpcCIsImlhdCI6MTY4NjcyOTMwMSwiZXhwIjoxNjg2ODE1NzAxfQ.OO6NKpGkPtUbTLbTCl15II5eD5OeeEGyrXUL7oJhtps|string|


### Response: 200
```json
{
    "error": false,
    "data": [
        {
            "id": 232,
            "category_id": 3,
            "name": "Bukit Moko",
            "description": "Bandung sebagai destinasi wisata tak pernah ada habisnya. Didukung dengan lanskap yang cantik, kawasan Bandung mampu menarik perhatian wisatawan. Baik dari segi alam, budaya, kuliner, dan sen",
            "city": "Bandung",
            "price": 25000,
            "lat": -6.8422202,
            "lng": 107.6767988,
            "rating": 4.5,
            "image": "https://storage.googleapis.com/tresure-place-images/Bukit%20Moko.jpg"
        },
        {
            "id": 247,
            "category_id": 5,
            "name": "Kiara Artha Park",
            "description": "Kiara Artha Park merupakan sebuah kawasan terpadu yang memadukan konsep hunian, bisnis, komersial, dan wisata yang ikonik di Kota Bandung dengan luas + 2.9 hektar. Kiara Artha Park sendiri me",
            "city": "Bandung",
            "price": 15000,
            "lat": -6.9159459,
            "lng": 107.6421462,
            "rating": 4.4,
            "image": "https://storage.googleapis.com/tresure-place-images/Kiara%20Artha%20Park.jpg"
        },
        {
            "id": 279,
            "category_id": 6,
            "name": "Masjid Agung Trans Studio Bandung",
            "description": "Masjid Agung Trans Studio Bandung (TSB) berdiri megah. Rumah ibadah seluas 4.000 meter persegi bergaya Timur Tengah ini menjadi oase di tengah-tengah pusat perbelanjaan dan tempat rekreasi. k",
            "city": "Bandung",
            "price": 0,
            "lat": -6.9259635,
            "lng": 107.6354278,
            "rating": 4.8,
            "image": "https://storage.googleapis.com/tresure-place-images/Masjid%20Agung%20Trans%20Studio%20Bandung.jpg"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## [ML] Predict with Location
Proses _request_ yang menggunakan parameter lokasi (**location**) akan mendapatkan hasil rekomendasi dengan kota yang sesuai dengan lokasi.

_Body request_ dapat menggunakan **JSON** atau _**urlencoded**_.
### Method: POST
>```
>https://tresure-app-v5cbzwlk4q-uc.a.run.app/users/predict
>```
### Body (**raw**)

```json
{
    "username": "alip",
    "location": "Yogyakarta"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTAwMDAsInVzZXJuYW1lIjoiYWxpcCIsImlhdCI6MTY4NjcyOTMwMSwiZXhwIjoxNjg2ODE1NzAxfQ.OO6NKpGkPtUbTLbTCl15II5eD5OeeEGyrXUL7oJhtps|string|


### Response: 200
```json
{
    "error": false,
    "data": [
        {
            "id": 91,
            "category_id": 5,
            "name": "Situs Warungboto",
            "description": "Situs Warungboto atau Pesanggrahan Rejawinangun adalah salah satu bangunan cagar budaya yang terletak di Jalan Veteran No.77, Kelurahan Warungboto, Kecamatan Umbulharjo, Kota Yogyakarta, Daer",
            "city": "Yogyakarta",
            "price": 0,
            "lat": -7.8102685,
            "lng": 110.3931513,
            "rating": 4.4,
            "image": "https://storage.googleapis.com/tresure-place-images/Situs%20Warungboto.jpg"
        },
        {
            "id": 103,
            "category_id": 5,
            "name": "Tugu Pal Putih Jogja",
            "description": "Tugu Yogyakarta (Jawa: , Tugu Ngayogyakarta) adalah sebuah landmark bersejarah yang penting di kota Yogyakarta, Indonesia. Tugu berarti tugu, yang biasanya dibangun sebagai simbol suatu kawas",
            "city": "Yogyakarta",
            "price": 0,
            "lat": -7.7829437,
            "lng": 110.3670548,
            "rating": 4.7,
            "image": "https://storage.googleapis.com/tresure-place-images/Tugu%20Pal%20Putih%20Jogja.jpg"
        },
        {
            "id": 122,
            "category_id": 2,
            "name": "Watu Goyang",
            "description": "Watu Goyang ini berasal dari Bahasa Jawa yang berarti Batu yang bergoyang. Dulunya di tempat ini terdapat batu yang berada di puncak yang bias bergoyang ketika disentuh maupun didorong. Batu ",
            "city": "Yogyakarta",
            "price": 2500,
            "lat": -7.9274086,
            "lng": 110.4120586,
            "rating": 4.4,
            "image": "https://storage.googleapis.com/tresure-place-images/Watu%20Goyang.jpg"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃