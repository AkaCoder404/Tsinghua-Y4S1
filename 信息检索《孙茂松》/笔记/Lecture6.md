# Lecture 6 2021年10月18日

http://web.eecs.umich.edu/~mihalcea/498IR/Lectures/TextProperties.pdf

# Zipf's Law

> models the distribution of terms in a corpus. How is the frequency of different words distributed? How many times does the kth most frequent word appear in a corpus size of N words.

- $r_1$ - last word of the words with occurrence of 1, prob of 1/2
- $r_n$ - last words of words with occurrence of n
- $r_{n +1}$ - last of words with occurence of n + 1

occurence == frequency

This law is important for dtermining index terms and properties of compression algorithms.

1. Number of words appearing exactly f times, $I_f$
2. Fraction of words with frequency f is $I_f / D$
3. Inverse document frequency weight...
4. Weight, collection freq and document freq https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html
5. Signal-noise ratio
6. Term discrimination value


# Heaps Law
