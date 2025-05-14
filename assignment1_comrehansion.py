products = [
    {"product_name": "Laptop", "category": "Electronics", "price": 1200},
    {"product_name": "Jeans", "category": "Apparel", "price": 40},
    {"product_name": "Coffee Maker", "category": "Home Appliances", "price": 80},
    {"product_name": "Smartphone", "category": "Electronics", "price": 999},
    {"product_name": "Jacket", "category": "Apparel", "price": 60},
    {"product_name": "Blender", "category": "Home Appliances", "price": 150},
    {"product_name": "Book", "category": "Literature", "price": 15}
]
#categories = set()
# for i in range(0, len(products)):
#     categories.add(products[i]['category'])
# print(categories)

#categories = {product['category'] for product in products}
#print(categories)

#task 2
concert_a_attendees = {"Alice", "Bob", "Charlie", "Diana"}
concert_b_attendees = {"Bob", "Diana", "Eve", "Frank"}
concert_c_attendees = {"Alice", "George", "Elle", "Frank","Bob"}

common_attendees = concert_a_attendees & concert_b_attendees & concert_c_attendees
# print(f"Common Attendees Between All Concerts: {common_attendees}")
#
# print(f"Unique Attendees for Each Concert:")
# print(f"- Concert A Only:{concert_a_attendees - (concert_b_attendees | concert_c_attendees)}")
# print(f"- Concert B Only:{concert_b_attendees - (concert_a_attendees | concert_c_attendees)}")
# print(f"- Concert C Only:{concert_c_attendees - (concert_b_attendees | concert_a_attendees)}")


# task 3
daily_temperatures = [68, 71, 74, 69, 70, 71, 68, 73, 72, 71, 70, 74, 72, 68]
filtered_daily_temperatures = [t for t in daily_temperatures if t > 70 ]
unique_daily_temperatures = set(filtered_daily_temperatures)


# task 5

grouped_daily_temp = {t:filtered_daily_temperatures.count(t) for t in filtered_daily_temperatures }

#print(grouped_daily_temp)

#task 6
posts = [
    {"content": "Loving the sunny weather today! #sunny #happy", "likes": 120},
    {"content": "Nothing beats a beach day. #beachday #sunny", "likes": 350},
    {"content": "A rainy day at home. #rainy #lazyday", "likes": 75},
    {"content": "Best coffee in town. #coffeelove #morning", "likes": 180},
    {"content": "Can't wait for the weekend. #weekend #party", "likes": 90}
]
popular_posts = [p for p in posts if p['likes'] > 100]
#print(popular_posts)

# task 7
def find_hash_tag(text):
    words = text.split()
    hashtag = {t for t in words if t.startswith('#')}
    return hashtag

unique_hashtags = {t for p in popular_posts for t in find_hash_tag(p['content'])}
#print(unique_hashtags)

# task 8
hashtag_count = {t: sum( t in p for p in popular_posts) for t in unique_hashtags}
print(hashtag_count)
