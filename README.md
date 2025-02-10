IMDB API Clone DRF

Accounts
- Registration: http://127.0.0.1:8000/api/account/register/
- Login: http://127.0.0.1:8000/api/account/login/
- Logout: http://127.0.0.1:8000/api/account/logout/

Stream Platforms
- Create Element & Acces List: http://127.0.0.1:8000/api/watch/stream/
- Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/

Watch List
- Create & Access List: http://127.0.0.1:8000/api/watch/
- Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/

Reviews
- Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/
- List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/
- Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews//<int:review_id>/

User Review
- Access All Reviews For Specific Userr: http://127.0.0.1:8000/api/watch/user-reviews/?username=example
