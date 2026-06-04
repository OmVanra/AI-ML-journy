# Q2. Create a class with the following attributes: 
# • title 
# • author 
# • list of reviews 
# And add methods to: 
# • add a new review 
# • count reviews 
# • display all reviews

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    def add_review(self, review):
        self.reviews.append(review)
    def count_reviews(self):
        return len(self.reviews)
    def display_reviews(self):
        if self.reviews:
            print(f"Reviews for '{self.title}' by {self.author}:")
            for review in self.reviews:
                print(f"- {review}")
        else:
            print(f"No reviews for '{self.title}' yet.")

# Example usage    
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book.add_review("A masterpiece of American literature.")
book.add_review("Beautifully written and deeply moving.")
print(f"Total reviews: {book.count_reviews()}")
book.display_reviews()
