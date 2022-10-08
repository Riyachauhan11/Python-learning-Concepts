def print_k_freq_words(s,k):
    words=s.split()
    d={}
    for word in words:
        d[word]=d.get(word,0)+1
    for ele in d:
        if d[ele]==k:
            print(ele)

s=input()
k=int(input())
print_k_freq_words(s,k)
