from photo import Photo
from post import Post

bird_photo = Photo()
bird_photo.filepath = "/usr/share/images/australian_raven.png"
bird_photo.alt_text = "A photo of a bird"
# print(bird_photo.__class__.__name__)
# print(bird_photo)

post = Post()
post.username = "Birdwatching Account"
post.message = "Help, how do I attach a photo?"
# Let's add the same bird photo 3 times:
for _ in range(3):
    post.add_attachment(bird_photo)

# And like the post a bit:
for _ in range(420):
    # It would be nice if we could jsut set this, but we decided to protect the likes.
    post.like()

post.add_comment("Crow!")

print("about to display")
post.display()
