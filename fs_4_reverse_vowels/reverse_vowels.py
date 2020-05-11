def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels="aeiouAEIOU"
    s=list(s)
    i=0
    get_v=[]
    inds =[]
    for letter in s:
        if letter in vowels:
            get_v.append(letter)
            inds.append(i)
        i+=1

    inds =inds[::-1]
    
    for i in range(len(inds)):
        s[inds[i]]=get_v[i]
        
    return "".join(s)
    