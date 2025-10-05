(lambda f: f(idem))(lambda g: (lambda h: (lambda x: g(h(x)))))(y)(z)
≡ (lambda g: (lambda h: (lambda x: g(h(x)))))(idem)(y)(z)                      beta-reduction
≡ (lambda h: (lambda x: idem(h(x))))(y)(z)                                     beta-reduction
≡ (lambda h: (lambda x: h(x)))(y)(z)                                           definition of idem
≡ (lambda x: y(x))(z)                                                          beta-reduction
≡ y(z)                                                                         beta-reduction
≡ idem(y)(z)                                                                   substituting out the definition of idem
⇒ (lambda f: f(idem))(lambda g: (lambda h: (lambda x: g(h(x)))))(y) ≡ idem(y)  extensional equality
⇒ (lambda f: f(idem))(lambda g: (lambda h: (lambda x: g(h(x))))) ≡ idem        extensional equality