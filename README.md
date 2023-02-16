# Spatic_Assignment<br />

Normal brute force approach:<br />
Check for all pairs of geographical location if distance is less than 200m and then find Levenshtein distance to reduce computation cost of Levenshtein distance logic.<br />

Observations:<br />
-> Logically there shouldn't be a lot of places within a 200m of a point. <br />
-> Assuming every location takes 10 sq. meter space we have no more than 400 points in a square of 200x200 sq. meter. <br />
-> Thus if we sort data based of longitute or latitude the we will get a better complexity than O(n*n*m*m) which we had with brute force. <br />
-> Since number of locations within a 200m of a point has an upper bound this we can say complexity if O(C*n*m*m). <br />
   Here, C is constant factor, n is number of data points and m is max lenght of name of locations.<br />
   <br />
Thus we have optimized our code to run within some seconds.<br />


# Calculating Levenshtein distance

The mathematical resoning for getDistance function:[Levenshtein_distance](https://en.wikipedia.org/wiki/Levenshtein_distance#:~:text=Informally%2C%20the%20Levenshtein%20distance%20between,considered%20this%20distance%20in%201965.) <br />

It was optimized by using memoization.
