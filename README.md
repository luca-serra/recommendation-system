# Recommendation system using collaborative filtering

Recommendation systems are more and more useful with all the data-driven platforms envolving users and items (e.g. *Amazon*, *Netflix* etc...)

Among the different possible strategies to decide which items are best to recommend to a user, several approaches are possible:
* **Content-based filtering**: using the content of the user's favorite items to find which new items are the closest.
* **Collaborative-based filtering** can be either *memory-based*: computing similarities between users (user-based filtering) or items (item-based filtering) based on the previous actions of users (ratings, like/dislike...) 
or *model-based*: using matrix factorization thanks to SVD, PCA or others.

This mini-projet aims to discover the "surprise" library, very useful to build simple recommendation engine, with a few lines of code.
