from scores.moving_average import return_moving_average_score
from scores.put_and_call import return_put_and_call_score
from scores.safe_heaven import return_safe_heaven_score

def main():
    moving_average_score = return_moving_average_score()
    put_and_call_score = return_put_and_call_score()
    safe_heaven_score = return_safe_heaven_score()

    overall = moving_average_score + put_and_call_score + safe_heaven_score

    print(overall)
    
if __name__ == "__main__":
    main()