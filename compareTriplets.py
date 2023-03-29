alice_score = list(map(int, input().split()))
bob_score = list(map(int, input().split()))

alice_final_score = 0
bob_final_score = 0

for a_score, b_score in zip(alice_score, bob_score):
    if a_score >b_score:
        alice_final_score +=1

    elif a_score <b_score:
        bob_final_score +=1


print("{} {}".format(alice_final_score, bob_final_score))
      
