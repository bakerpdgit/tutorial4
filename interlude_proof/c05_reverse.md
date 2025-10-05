(lambda f: (lambda x: (lambda y: f(x))))(idem)(a)(b)
≡ (lambda x: (lambda y: idem(x)))(a)(b)                         beta reduction
≡ (lambda y: idem(a))(b)                                        beta reduction
≡ idem(a)                                                       beta reduction
≡ a                                                             definition of idem
≡ const(a)(b)                                                   substituting out the definition of const
⇒ (lambda f: (lambda x: (lambda y: f(x))))(idem)(a) ≡ const(a)  extensional equality
⇒ (lambda f: (lambda x: (lambda y: f(x))))(idem) ≡ const        extensional equality