""" You've built an inflight entertainment system with on-demand movie streaming.
Users on longer flights like to start a second movie right when their first one ends,
but they complain that the plane usually lands before they can see the ending. 
So you're building a feature for choosing two movies whose total runtimes will equal 
the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether there 
are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory. """

# Start coding from here

def flight(movie_lengths, flight_length):
    movie_lengths = set(movie_lengths)
    for first_movie_length in movie_lengths:
        second_movie_length = flight_length - first_movie_length
        if second_movie_length in movie_lengths:
            return True
        movie_lengths.add(first_movie_length)
    return False
flight([134,89,90,90,40,10],50 )
