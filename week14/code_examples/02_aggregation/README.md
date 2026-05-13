It's weird that Text Posts can't have photos and photo posts can't have attachments.

Or maybe that's normal.  I guess it depends on what your social media experience is.


In any case -- we want to allow any post to have attachments -- those attachments can then be typed instead.  This will take some refactoring.

Post -> make it concrete, make all posts have an optional message.
-> Add "self.attachments = []" to the post

This will aggregate an "Attachment" abstract class
- Video
- Audio
- Photo
(for example!)


---

# Exercise!
## Part 1

Take this code as your starter code.

We think that comments should be more than text strings.  They need their own attributes, like 'username' and 'posted_at'.

1. Create a class representing Comments
2. Change Post.add_comment so that posts can now aggregate Comments.


## Part 2
- Both comments and Posts have a concept of having been 'authored' at a certain time by a certain person (username, timestamp).
- Modify Comment and Post to include a class "Authorship" which can encapsulate the username and timestamp.



## Part 3
- Go forth and read the requirements for AT4-1.
- Highly recommend attempting to get your acceptance criteria and question out now, if possible.