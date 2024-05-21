# Lab 1

class ReservationSystem:
    def bookRoom(self, roomType):
        print(f"Booking a {roomType} room")

class CleaningService:
    def scheduleCleaning(self, roomId):
        print(f"Scheduling cleaning for room {roomId}")

class DiningService:
    def orderFood(self, roomNumber, foodItem):
        print(f"Ordering {foodItem} for room {roomNumber}")

class CustomerRequests:
    def requestItem(self, roomNumber, item):
        print(f"Requesting {item} for room {roomNumber}")

class HotelManagementFacade:
    def __init__(self):
        self.reservation_system = ReservationSystem()
        self.cleaning_service = CleaningService()
        self.dining_service = DiningService()
        self.customer_requests = CustomerRequests()

    def book_room(self, room_type):
        self.reservation_system.bookRoom(room_type)

    def schedule_cleaning(self, room_id):
        self.cleaning_service.scheduleCleaning(room_id)

    def order_food(self, room_number, food_item):
        self.dining_service.orderFood(room_number, food_item)

    def request_item(self, room_number, item):
        self.customer_requests.requestItem(room_number, item)


# 예시 사용법
hotel_facade = HotelManagementFacade()
hotel_facade.book_room("Deluxe")
hotel_facade.schedule_cleaning(101)
hotel_facade.order_food(101, "Pizza")
hotel_facade.request_item(101, "Extra Pillow")


# Lab 2
# third party APIs
class TwitterAPI:
    def get_tweets(self):
        print("Fetching tweets from Twitter")
        stat = {"tweet": "Hello Twitter!", "likes": 10, "date": "2022-01-01"}
        return stat
    
class FacebookAPI:
    def get_posts(self):
        print("Fetching posts from Facebook")
        stat = {"post": "Hello Facebook!", "reactions": 5, "date": "2022-01-02"}
        return stat
    
class InstagramAPI:
    def get_photos(self):
        print("Fetching photos from Instagram")
        stat = {"photo": "Hello Instagram!", "likes": 15, "date": "2022-01-03"}
        return stat
    

# API , fetch_posts
class SocialMediaAdapter:
    def __init__(self, api):
        self.api = api

    def fetch_posts(self):
        pass


class TwitterAdapter(SocialMediaAdapter):
    def __init__(self, api:TwitterAPI):
        self.api = api

    def fetch_posts(self):
        return self.api.get_tweets()


class FacebookAdapter(SocialMediaAdapter):
    def __init__(self, api:FacebookAPI):
        self.api = api

    def fetch_posts(self):
        return self.api.get_posts()


class InstagramAdapter(SocialMediaAdapter):
    def __init__(self, api:InstagramAPI):
        self.api = api

    def fetch_posts(self):
        return self.api.get_photos()


def main():
    twitter = TwitterAdapter(TwitterAPI())
    facebook = FacebookAdapter(FacebookAPI())
    instagram = InstagramAdapter(InstagramAPI())
    for adapter in [twitter, facebook, instagram]:
        posts = adapter.fetch_posts()
        print(posts)


if __name__ == "__main__":
    main()
