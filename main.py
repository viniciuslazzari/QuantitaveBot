from scores.moving_average import return_moving_average_score
from scores.put_and_call import return_put_and_call_score

def main():
    moving_average_score = return_moving_average_score()
    put_and_call_score = return_put_and_call_score()

    print(moving_average_score, put_and_call_score)
    
if __name__ == "__main__":
    main()