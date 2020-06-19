#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear time: O(n)

As the size of n increases, the runtime increases by the same rate.

b) Exponential time: O(2^n)  - n log n

As the size of n increases, the runtime increases by a much faster rate.

c) Linear time: O(n)

As the size of n increases, the runtime will increase at the same rate.

## Exercise II

To minimize the number of broken eggs while determining which floor of a building
is the lowest floor from which an egg can be dropped and will break, one would
use a binary search, as explained below.

Start at the center floor and drop an egg. If the does not break, we need to go
higher up. If the egg breaks, we need to go lower. Whichever direction we are
going, we go to the center floor of the floors between the current floor and
either the ground or top floor. These steps are repeated using the last tested
floors as their upper and lower bounds until we find the floor at which the egg
breaks when dropped but does not break when dropped from the floor below.

This is the most efficient use of eggs, because the result when starting from
the midpoint of each known range of floors automatically cuts the size of the
next range to be tested in half each time.

Given n floors to test, this solution will identify the target floor in
logarithmic time, O(log n).
