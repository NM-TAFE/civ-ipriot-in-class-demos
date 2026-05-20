from post import Post
from photo import Photo

text_post_1 = Post()
text_post_1.username = "CraftyPanda"
text_post_1.message = "Hey anyone down for some knitting?"
text_post_1.add_comment("I am always down for knitting")

text_post_2 = Post()
text_post_2.username = "HungryTerror1980"
text_post_2.message = "faM i AM HUNGRY"
text_post_2.like()


photo_post_1 = Post()
photo_post_1.username = "ArcticCoffee"
photo_post_1.message = "I Am Branching Out Into Teas.  This Is Acceptable."
photo = Photo(filename ="macha.jpg", alt_text="a cup of macha" )
photo_post_1.add_photo(photo)

for post in [text_post_1, text_post_2, photo_post_1]:
    print(post.display())



