from technology_stack.backend.database.mongodb import MongoDB

class SocialMediaAnalyzer:
   def __init__(self):
       self.db = MongoDB()
   
   def analyze_hashtags(self, posts):
       hashtag_counts = {}
       for post in posts:
           hashtags = post.get('hashtags', [])
           for hashtag in hashtags:
               if hashtag in hashtag_counts:
                  hashtag_counts[hashtag] += 1
               else:
                  hashtag_counts[hashtag] = 1
       return hashtag_counts
   
   def track_post_performance(self, posts):
       post_performance = {}
       for post in posts:
           post_id = post.get('id')
           likes = post.get('likes', 0)
           comments = post.get('comments', 0)
           shares = post.get('shares', 0)
           post_performance[post_id] = {
               'likes': likes,
               'comments': comments,
               'shares': shares
           }
       return post_performance
