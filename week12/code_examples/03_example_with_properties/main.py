from photo_post import PhotoPost
from text_post import TextPost

text_post_1 = TextPost()
text_post_1.username = "CraftyPanda"
text_post_1.message = "Hey anyone down for some knitting?"
text_post_1.add_comment("I am always down for knitting")

text_post_2 = TextPost()
text_post_2.username = "HungryTerror1980"
text_post_2.message = "faM i AM HUNGRY"
text_post_2.like()


photo_post_1 = PhotoPost()
photo_post_1.username = "ArcticCoffee"
photo_post_1.filename = "macha.jpg"
photo_post_1.caption = "I Am Branching Out Into Teas.  This Is Acceptable."

for post in [text_post_1, text_post_2, photo_post_1]:
    print(post.display())



