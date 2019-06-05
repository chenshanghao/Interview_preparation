class Solution:
    """
    @param restaurant: 
    @param n: 
    @return: nothing
    """
    def nearestRestaurant(self, restaurant, n):
        # Write your code here
        res = []
        if not restaurant or n > len(restaurant):
            return res
        L = len(restaurant)
        distance = []
        count = 0
        for coordinates in restaurant:
            dis = int(coordinates[0]) ** 2 + int(coordinates[1]) ** 2
            distance.append(dis)
        distance = sorted(distance)
        threshold = distance[n - 1]
        
        for coordinates in restaurant:
            dis = int(coordinates[0]) ** 2 + int(coordinates[1]) ** 2
            if (dis <= distance[n-1]):
                res.append(coordinates)
                count += 1
            if count == n:
                break
        return res