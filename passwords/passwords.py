#Author: Lily Li
import hashlib
import binascii


# word list: strip words from word file
words = [line.strip().lower() for line in open('words.txt')]
username_and_hashes = [line.strip().split(':') for line in open('passwords1.txt')]
username_and_hashes2 = [line.strip().split(':') for line in open('passwords2.txt')]
username_and_hashes3 = [line.strip().split(':') for line in open('passwords3.txt')]
cracked1 = open('cracked1.txt','w+')
cracked2 = open('cracked2.txt','w+')
cracked3 = open('cracked3.txt','w+')

#code for part 1
for word in words:
    hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
    for username_and_hash in username_and_hashes:
        username = username_and_hash[0]
        hash = username_and_hash[1]
        if hash == hashed_word:
            cracked1.write(username+':'+word+'\n')
            break
            

#code for part 2
for word in words:
    print(word)
    not_get_answer = True
    for word2 in words:
        final_word = word + word2
        hashed_word = hashlib.sha256(final_word.encode('utf-8')).hexdigest()
        for username_and_hash in username_and_hashes2:
            username = username_and_hash[0]
            hash2 = username_and_hash[1]
            if hash2 == hashed_word:
                cracked2.write(username+':'+final_word+'\n')
                not_get_answer = False
                print(username+':'+final_word+'\n')
                break
    if not_get_answer:
        hashed_word_org = hashlib.sha256(word.encode('utf-8')).hexdigest()
        for username_and_hash in username_and_hashes2:
            username = username_and_hash[0]
            hash2 = username_and_hash[1]
            if hash2 == hashed_word_org:
                cracked2.write(username+':'+word+'\n')
                not_get_answer = False
                print(username+':'+word+'\n')
                break


#code for part 3
for username_and_hash in username_and_hashes3:
    username = username_and_hash[0]
    further_split = username_and_hash[1].split('$')
    hash3 = further_split[3]
    salt = further_split[2]
    for word in words:
        concatentated = salt + word
        hashed_concatenate= hashlib.sha256(concatentated.encode('utf-8')).hexdigest()
        if hashed_concatenate == hash3:
            cracked3.write(username+':'+hash3+word+'\n')
            print(username+':'+word+'\n')
    
cracked1.close()
cracked2.close()
cracked3.close()

print('cracking done')



