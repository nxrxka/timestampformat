from datetime import datetime
import os

def convert_date_format(input_date):
    input_format = "%d/%b/%Y:%H:%M:%S"
    output_format = "%Y-%m-%d %H:%M:%S"
    # 입력 형식으로부터 datetime 객체 생성
    datetime_obj = datetime.strptime(input_date, input_format)
    # 출력 형식으로 변환
    converted_date = datetime_obj.strftime(output_format)
    return converted_date

# 입력 파일 이름과 출력 파일 이름
input_file_path = "/Users/input_dates.txt"  # input_dates.txt 파일의 절대 경로로 수정해야 합니다.
output_file_name = "output_dates.txt"

# 입력 파일 열기
if os.path.exists(input_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # 변환된 결과를 저장할 리스트
    converted_dates = []

    # 주어진 형식을 다른 형식으로 변환
    for line in lines:
        # 각 줄의 날짜와 시간 부분 추출하여 변환 후 리스트에 추가
        date_str = line.strip()
        converted_date = convert_date_format(date_str)
        converted_dates.append(converted_date)

    # 입력 파일의 디렉토리 경로 추출
    input_directory = os.path.dirname(input_file_path)

    # 출력 파일의 경로 생성
    output_file_path = os.path.join(input_directory, output_file_name)

    # 출력 파일에 변환된 결과 쓰기
    with open(output_file_path, 'w') as output_file:
        for converted_date in converted_dates:
            output_file.write(converted_date + '\n')

    print(f"날짜와 시간 형식이 변환되어 {output_file_name} 파일이 {input_directory} 디렉토리에 저장되었습니다.")
else:
    print("입력 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
