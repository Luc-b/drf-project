
# IMDB API Clone (Django REST Framework)  

A RESTful API built with Django REST Framework (DRF) that mimics key functionalities of IMDB. This API allows users to register, log in, manage streaming platforms, create watchlists, post movie reviews, and retrieve user-specific reviews.  

## **Features**  
- **User Authentication**: Registration, login, and logout functionality  
- **Streaming Platforms**: Create, retrieve, update, and delete streaming platform entries  
- **Watchlist Management**: Add movies to a personal watchlist and manage them  
- **Reviews**: Users can create, edit, and delete reviews for movies  
- **User-Specific Reviews**: Retrieve all reviews posted by a specific user  

## **Technologies Used**  
- Python 3  
- Django REST Framework  
- SQLite3 (can be replaced with another database)  
- JSON-based API responses
- Swagger UI

## **API Endpoints**  

### **User Authentication**  
- **Register:** `POST /api/account/register/`  
- **Login:** `POST /api/account/login/`  
- **Logout:** `POST /api/account/logout/`  

### **Streaming Platforms**  
- **Create & List Platforms:** `GET/POST /api/watch/stream/`  
- **Retrieve, Update & Delete Platform:** `GET/PUT/DELETE /api/watch/stream/{streamplatform_id}/`  

### **Watchlist**  
- **Create & List Movies:** `GET/POST /api/watch/`  
- **Retrieve, Update & Delete Movie:** `GET/PUT/DELETE /api/watch/{movie_id}/`  

### **Reviews**  
- **Create a Review for a Movie:** `POST /api/watch/{movie_id}/reviews/create/`  
- **List All Reviews for a Movie:** `GET /api/watch/{movie_id}/reviews/`  
- **Retrieve, Update & Delete a Review:** `GET/PUT/DELETE /api/watch/reviews/{review_id}/`  

### **User Reviews**  
- **Retrieve All Reviews by a User:** `GET /api/watch/user-reviews/?username=example`  

## **Installation and Setup**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/imdb-api-clone.git
   cd imdb-api-clone
   ```  
2. Create a virtual environment and install dependencies:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   pip install -r requirements.txt  
   ```  
3. Run database migrations:  
   ```bash
   python manage.py migrate  
   python manage.py createsuperuser  # If you want admin access  
   ```  
4. Start the development server:  
   ```bash
   python manage.py runserver  
   ```  
5. Test API endpoints using Postman or your preferred API client at:  
   ```
   http://127.0.0.1:8000/api/
   ```  

![image](https://github.com/user-attachments/assets/8a61dfe2-aae6-4af5-a289-f458380f6a16)


## **Project Structure**  
```
imdb-api-clone/
│── account/              # User authentication app  
│── watch/                # Core functionality for streaming platforms, movies, and reviews  
│   ├── views.py          # API logic  
│   ├── models.py         # Database models  
│   ├── serializers.py    # API serializers  
│   ├── urls.py           # API routes  
│── mysite/               # Project configuration  
│── db.sqlite3            # SQLite database  
│── manage.py             # Django management script  
```

## **Planned Improvements**  
- **User Permissions**: Restrict modifications to only review authors  
- **Movie Ratings**: Implement a rating system for movies  
- **Search & Filtering**: Allow filtering movies by platform, genre, or release year  

## **Author**  
Luc-b  
