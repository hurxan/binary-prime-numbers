# Binary Prime Numbers
This is an unrealistic attempt to discover something about prime numbers by extrapolating data using the binary representation.

## First things first
I've included a dataset with the first million prime numbers (yes, a million). There is also a smaller version for testing (~10K).

## Intuition
I was playing around with prime numbers trying to win a million dollars (cough), and then I got stuck with the idea of manipulating them using binary representation. I tried also other base-n representations, but they weren't that helpful. What caught my attention is the fact that prime numbers follow some sort of structure; they all begin and end with a binary value <code>0b1</code>.

## Nucleus of the prime number
With this idea in mind, I wrote down a script that elaborates the dataset of prime numbers in decimal and transformed them into binary. Then, I proceeded by "unwrapping" the common structure of these binary numbers by removing the first and the last digit, which in all cases occurred to be 1. (Note that the first digit is always 1 for any base-2 number, and the last digit is always 1 too because they're all odd numbers except for <code>0b10</code>). So here comes the idea of the "nucleus" of the number.

To give you an example, this is a sample of the outcome of the script.

<p align="center">
  <image src="https://github.com/hurxan/binary-prime-numbers/assets/24367273/fa7fc7a6-84dc-4329-8334-e0ad858a5f72" width="800px" />
</p>

## Eureka! Sort of...
Then I noticed something quite strange (actually, it's not that strange, but I was enthusiastic about it): the decimal nucleus works in a... cyclical way. Whenever there is an overflow in the binary nucleus, a new digit is needed, so the counter starts from the beginning because we are taking into consideration only the nucleus and not the whole number.

I plotted the output of the script using R, and this is the result.

<p align="center">
  <image src="https://github.com/hurxan/binary-prime-numbers/assets/24367273/913ee7cb-1fa3-4b2a-94a6-33fab3a14f07" width="800px" />
</p>

It has a curious behavior, and the shape is always the same independently of the size of the dataset.

<p align="center">
  <image src="https://github.com/hurxan/binary-prime-numbers/assets/24367273/e2cf7b12-cdcd-44ed-b1f0-c5282ed2ab28" width="800px" />
</p>

## Conclusions
It was fun; I tried some other manipulations but didn't really bring anything that looks useful, to say the least.

Maybe it's not a groundbreaking result, but it caught my attention.
