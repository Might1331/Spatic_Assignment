# Spatic_Assignment

Normal brute force approach:
Check for all pairs of geographical location if distance is less than 200m and then find Levenshtein distance to reduce computation cost of Levenshtein distance logic.

Observations:
-> Logically there shouldn't be a lot of places within a 200m of a point.
-> Assuming every location takes 10 sq. meter space we have no more than 400 points in a square of 200x200 sq. meter.
-> Thus if we sort data based of longitute or latitude the we will get a better complexity than O(n*n*m*m) which we had with brute force.
-> Since number of locations within a 200m of a point has an upper bound this we can say complexity if O(C*n*m*m).
   Here, C is constant factor, n is number of data points and m is max lenght of name of locations.
   
Thus we have optimized our code to run within some seconds.
