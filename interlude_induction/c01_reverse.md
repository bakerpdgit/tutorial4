Claim: For every natural number n, either n is even or succ(n) is even

We proceed by induction on n.
In the case that n ≡ 0:
  0 is even                       definition of even
  n is even                       by the above and since n ≡ 0
In the case that n ≡ succ(k), assuming the claim for k:
  k is even or succ(k) is even    the inductive hypothesis
  In the case that k is even:
    succ(succ(k)) is even         definition of even
    succ(n) ≡ succ(succ(k))       n ≡ succ(k)
    succ(n) is even               above two statements
  In the case that succ(k) is even:
    n is even                     by the assumption and since n ≡ succ(k)
  By cases, n is even or succ(n) is even
By induction, for all n, either n is even or succ(n) is even.