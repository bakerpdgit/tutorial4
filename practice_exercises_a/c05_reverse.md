In the case l ≡ nil:
⠀⠀(tail ∘ repeat_first_element)(nil)
⠀⠀≡ tail(repeat_first_element(nil))      by definition of composition
⠀⠀≡ tail(nil)                            by definition of repeat_first_element
⠀⠀≡ nil                                  by definition of tail
⠀⠀≡ idem(nil)                            by definition of idem
And in the case l ≡ x  : xs:
⠀⠀(tail ∘ repeat_first_element)(x : xs)
⠀⠀≡ tail(repeat_first_element(x : xs))   by definition of composition
⠀⠀≡ tail(x : x : xs)                     by definition of repeat_first_element
⠀⠀≡ x : xs                               by definition of tail
⠀⠀≡ idem(x : xs)                         by definition of idem
By extensional equality, tail ∘ repeat_first_element ≡ idem