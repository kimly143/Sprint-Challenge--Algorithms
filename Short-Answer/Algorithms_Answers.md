#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe it is O(n) because even though we iterate while a < n^3 we add n^2 to a every iteration, n^3/n^2 = n 


b) I believe it is O(n^2) since the outer loop uses a range to n and the inner loop also loops till n but increments it's counter by multiplying it by 2 -- since we don't consider constans in big-O notation we end up with O(n) for the inner loop which results in O(n^2) overall for both loops


c) I believe it is O(n) becuase each call will call itself with bunnies - 1 until it hits 0 so it will loop until 0 before returning, meaning it's runtime is affected by the size of bunnies.
Although this will probably break or fail if called with a negative number.

## Exercise II

Use a binary search algorithm and start at the (0 + n) // 2 floor, if the egg does not break search higher floors and if the egg does break search lower floors. Continue this process until a single floor is found such that dropping an egg from that floor does not break and dropping an egg from that floor + 1 breaks

The runtime complexity of a binary search is O(log n) since we cut our search space in half each pass.
