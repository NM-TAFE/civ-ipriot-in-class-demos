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