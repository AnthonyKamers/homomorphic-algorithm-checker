# Homomorphic Algorithm Checker

This project is meant to auxiliar the study of
homomorphic algorithms. It is a web application
that allows the user to input an arbitrary equation,
that is possible to be evaluated by the Python math
library. Given that, it will be give and algorithm
that suits best for your purpose.

## About Homomorphic Encryption

With Homomorphic Encryption (HE), you do not need to decrypt
the function with a private key to evaluate some
operation on it. In other words, for applications
like cloud computing, you can send your encrypted
data and the server will perform all the operations
you need, without knowing what is the data.

There are basically three variants of HE:
- Partially Homomorphic Encryption (PHE)
  - Makes one operation over ciphertext
- Somewhat Homomorphic Encryption (SHE)
  - Makes two operations over ciphertext (being one
  unlimited, normally addition and another limited,
  normally multiplication)
- Leveled Fully Homomorphic Encryption (LFHE)
  - It can evaluate additions and multiplications
  over ciphertext, but it has a limit of depth
  in the circuit evaluated
- Fully Homomorphic Encryption (FHE)
  - Unlimited number of multiplications and additions

## What I believe for Homomorphic Encryption

I believe that Homomorphic Encryption will be the
future, but until we find a reasonable way to make
evaluations with a reasonable time and with a reasonable
amount of resources, it will be hard to use it in
real applications.

Nevertheless, I also believe that we should be using
Homomorphic Encryption in our applications whenever
as possible, with the algorithms we already know
it works, for determined purposes. Maybe you don't
know what algorithm you could use with a reasonable
time of evaluation and of resources, so this should
help you.

## The project

This application is an open-source project,
submited as BCS degree (Bachelor Computer
Science) final project at UFSC -
Universidade Federal de Santa Catarina, Brazil by
Anthony Bernardo Kamers. There is a MIT license,
so you can use as you wish.

The code is a very simple Flask application to serve
it all and the main asset is localized in
`static/json/algorithms.json`, where it has the
algorithms that are available to be checked upon.

The input code is evaluated by the Python `ast` and
run all the child nodes to find the operations needed
to be performed into the ciphertext.
