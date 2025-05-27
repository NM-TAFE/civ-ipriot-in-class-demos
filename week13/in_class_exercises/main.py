from user import User
user = User('my_name', 'my_name@name.com')
post = user.create_post("Hello, world!")
post.display_post()