import heapq
from collections import defaultdict
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # A map to quickly find the price of a movie at a specific shop
        # Key: (shop, movie), Value: price
        self.price_map = {}

        # A dictionary of min-heaps for all available movies.
        # Key: movie_id, Value: min-heap of (price, shop)
        self.available_movies = defaultdict(list)

        # A single min-heap for all rental events. This may contain stale entries.
        # Stores (price, shop, movie)
        self.rented_movies = []

        # A set for O(1) lookup to see if a specific (shop, movie) is CURRENTLY rented.
        self.rented_set = set()

        # Initialize available movies from the entries list
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            heapq.heappush(self.available_movies[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        res = []
        temp_popped = []
        heap = self.available_movies[movie]

        while heap and len(res) < 5:
            price, shop = heapq.heappop(heap)
            temp_popped.append((price, shop))

            if (shop, movie) not in self.rented_set:
                res.append(shop)
        
        for item in temp_popped:
            heapq.heappush(heap, item)
            
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        price = self.price_map[(shop, movie)]
        heapq.heappush(self.rented_movies, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if (shop, movie) in self.rented_set:
            self.rented_set.remove((shop, movie))

    def report(self) -> List[List[int]]:
        res = []
        temp_popped = []
        # 🐛 FIX: Add a set to track items added to this report
        # to prevent duplicates from stale heap entries.
        added_to_this_report = set()
        heap = self.rented_movies

        while heap and len(res) < 5:
            price, shop, movie = heapq.heappop(heap)
            temp_popped.append((price, shop, movie))
            
            # Check three things:
            # 1. Is the movie *currently* rented?
            # 2. Have we *already added* this exact (shop, movie) to our result list?
            # 3. If both are true, add it to the report.
            if (shop, movie) in self.rented_set and (shop, movie) not in added_to_this_report:
                res.append([shop, movie])
                added_to_this_report.add((shop, movie))

        # Restore the heap with all the items we popped off
        for item in temp_popped:
            heapq.heappush(heap, item)
            
        return res