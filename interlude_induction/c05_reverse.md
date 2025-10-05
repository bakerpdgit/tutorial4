We proceed by induction on l.
In the case l ≡ nil:
⠀⠀concat(l, nil) ≡ concat(nil, nil)     since l ≡ nil
⠀⠀≡ nil                                 by definition of concat
⠀⠀≡ l                                   since l ≡ nil
And in the case l ≡ x : xs, assuming the claim for xs:
⠀⠀concat(l, nil) ≡ concat(x : xs, nil)  since l ≡ x : xs
⠀⠀≡ x : concat(xs, nil)                 by definition of concat
⠀⠀≡ x : xs                              by the inductive hypothesis
⠀⠀≡ l                                   since l ≡ x : xs
By induction, for any list l, concat(l, nil) ≡ l