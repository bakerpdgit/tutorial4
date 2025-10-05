We proceed by induction on n.
In the case n ≡ 0:
⠀⠀double(n) ≡ 0                         definition of double
⠀⠀hence double(n) is even               by definition of even
And in the case n ≡ succ(k), assuming the claim for k:
⠀⠀double(k) is even                     the inductive hypothesis
⠀⠀and double(n) ≡ succ(succ(double(k))  by definition of double
⠀⠀hence double(n) is even               by definition of even
By induction, for all n, double(n) is even