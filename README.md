# estimating_pi
Estimating the value of pi using the Monte Carlo statistical method

The Monte Carlo method is a statistical technique to predict the possible outcomes of an uncertain event.
In this program, I've tried to estimate the value of pi by dividing the number of points that fall inside a circle by the total number of points created and then multiplying it by 4. The radius of the circle is half of the length of the side of the square.
Explanation:
area of circle = pi * r^2.
area of square = l^2 = (2r)^2.
area of circle/area of square = pi*r^2/4r^2 = pi/4.
Considering there are infinite points to cover the whole surface of a square:
points inside circle/points inside square (total number of points) = pi/4.
Therefore,
(points inside circle/total number of points) * 4 = pi.
