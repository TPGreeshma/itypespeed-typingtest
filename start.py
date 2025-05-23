import random as rr


def test():

    """To get a random paragraph of common words used regularly"""
    # To open the file full words
    f = open("textt.txt", "r")
    # To read the file
    r=f.read()
    # To get separate words
    r=r.split()

    l=rr.choices(r,k=120)
    # To join the array of words to form a single string of words separated by words
    s=' '.join(l)


    import time 
    """To the measure the time taken by the user"""

    print()
    print("Type the following as fast as you can:")
    print()
    time.sleep(1)
    print(s)
    print()
    time.sleep(1)
    input("Are you ready?  ")

    print("\nYour ",end='')
    time.sleep(1)
    print("time ",end='')
    time.sleep(1)
    print("starts ",end='')
    time.sleep(1)
    print("now!\n")
    # Start timer
    start_time = time.perf_counter()

    # Code to be timed
    inp=input()

    # End timer
    end_time = time.perf_counter()

    # Calculate elapsed time
    elapsed_time = end_time - start_time




    # Calculations
    inp_l=inp.split()
    inp_lenght=len(inp_l)
    score=0

    print()
    print("Misspelled words:")
    for i in range(inp_lenght):
        if l[i]==inp_l[i]:
            score=score+1
            
        else:
            score=score-1
            print(l[i],inp_l[i])




    # Display
    print()
    print("Start time: ",start_time,"\tEnd time: ",end_time)
    print("Elapsed time: ", elapsed_time)
    print()
    print("NUMBER OF WORDS TYPED:",inp_lenght)
    print("CORRECT :",score)
    print()
    print("SPEED: ", int(score/(elapsed_time/60)),"words per min")
    print("ACCURACY: ",(score/inp_lenght)*100,"%")

test()

while True:
    inp = input("\nWanna try again?")
    if inp in ["no", "nooo","NO","never","nah","hell no"]:
        break
    else:
        test()


