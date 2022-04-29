from app import app, login_manager, login
from forms import LoginForm

client = app.test_client()


# def test_create_func():
#     assert client.post('/create', data={'level': 'TEST', 'date_time': '2021-04-25T10:00', 'source': 'TEST', 'event_id': '4444' }).status_code==200
    
# def test_delete_func():
#     assert client.get('/data/999/delete').status_code == 401
#     print("deletes successfuly")
# def test_update():
#     assert client.post('/data/4/update').status_code == 200
#     print("updates successfuly")

# def test_get_users(): #testing we inserted
#     response = client.get('/')
#     assert b"TEST" in response.data

# def test_search():
#     assert client.post('/search').status_code == 200

def test_index_page__not_logged_in():
    res = client.get('/')
    assert b"Hi" not in res.data

def test_login_page():
    res = client.get('/login')
    assert b"Please enter your login and password!" in res.data

# def test_login():
    
#     client.post('/login', {form.username: 'Svetlin', form.password: 'Ivan1234', form.submit: 'Login' })

# def test_that_something_works():
#     client.post('login', { LoginForm.username: 'Svetlin', LoginForm.password: 'Ivan1234' })
#     # this will fail, because current_user is an AnonymousUser
#     assert current_user.username == "Svetlin"

if __name__ == "__main__":
    app.main()
    