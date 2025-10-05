Claim: if all elements of a list l are even, then sum(l) is even

We proceed by induction on l.
In the case l ≡ nil:
  sum(l) ≡ 0            definition of sum
  0 is even             definition of even
  sum(l) is even        since sum(l) ≡ 0
And in the case l ≡ x : xs, assuming the claim for xs:
  sum(l) ≡ x + sum(xs)  definition of sum
  x is even             since all elements of l are even
  sum(xs) is even       inductive hypothesis
  x + sum(xs) is even   since the sum of two even numbers is even
  sum(l) is even        since sum(l) ≡ x + xs
By induction, if all elements of a list l are even, then sum(l) is even