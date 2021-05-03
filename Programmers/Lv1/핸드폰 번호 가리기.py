def solution(phone_number):
    front_len = len(phone_number)-4
    answer = "*" * front_len + phone_number[len(phone_number)-4:]   # phone_number[len(phone_number)-4:]  ==  phone_number[-4:] 
    return answer