import sys

# 분을 hh:mm 형식으로 변환하는 클래스
class AirTime:
    def __init__(self, minutes):
        self.minutes = minutes

    def get_hour_and_min(self):
        return f"{(self.minutes // 60) % 24:02d}:{self.minutes % 60:02d}"

# 일(day)을 분(minute)으로 변환
def day_to_min(day):
    return day * 24 * 60

# 문제 해결 함수
def air_times(day, stop_min):
    stop_terms = [3 * 60, 3 * 60, 18 * 60]
    result = []
    count = 0
    current_min = 15 * 60  # 0일 15:00부터 시작
    today = day_to_min(day)
    tomorrow = day_to_min(day + 1)

    while current_min < tomorrow:
        if current_min >= today:
            result.append(AirTime(current_min))
        current_min += stop_terms[count % 3]
        if count % 3 == 2:
            current_min += stop_min
        count += 1
    return result

# 입력 처리
def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    result = air_times(n, k)
    print(len(result))
    for time in result:
        print(time.get_hour_and_min())

if __name__ == "__main__":
    main()
