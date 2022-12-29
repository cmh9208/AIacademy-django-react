import random
import string
import datetime
lambda_string = lambda k: ''.join(random.sample(string.ascii_lowercase, k))
random_number = lambda start, end: random.randrange(start, end)
lambda_number = lambda k: ''.join(str(random_number(0, 10)) for _ in range(k))
lambda_time = lambda x: datetime.datetime.now().strftime(x) # '%Y-%m-%d %H:%M:%S'
first_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권"]
name_words = ["가", "강", "건", "경", "고", "관", "광", "구", "규", "근", "기", "길", "나", "남", "노", "누", "다", "단", "달",
              "담", "대", "덕", "도", "동", "두", "라", "래", "로", "루", "리", "마", "만", "명", "무", "문", "미", "민", "바",
              "박", "백", "범", "별", "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", "설", "섭", "성", "세", "소",
              "솔", "수", "숙", "순", "숭", "슬", "승", "시", "신", "아", "안", "애", "엄", "여", "연", "영", "예", "오", "옥",
              "완", "요", "용", "우", "원", "월", "위", "유", "윤", "율", "으", "은", "의", "이", "익", "인", "일", "잎", "자",
              "잔", "장", "재", "전", "정", "제", "조", "종", "주", "준", "중", "지", "진", "찬", "창", "채", "천", "철", "초",
              "춘", "충", "치", "탐", "태", "택", "판", "하", "한", "해", "혁", "현", "형", "혜", "호", "홍", "화", "환", "회",
              "효", "훈", "휘", "희", "운", "모", "배", "부", "림", "봉", "혼", "황", "량", "린", "을", "비", "솜", "공", "면",
              "탁", "온", "디", "항", "후", "려", "균", "묵", "송", "욱", "휴", "언", "령", "섬", "들", "견", "추", "걸", "삼",
              "열", "웅", "분", "변", "양", "출", "타", "흥", "겸", "곤", "번", "식", "란", "더", "손", "술", "훔", "반", "빈",
              "실", "직", "흠", "흔", "악", "람", "권", "복", "심", "헌", "엽", "학", "개", "롱", "평", "늘", "늬", "랑", "얀", "향",
              "울", "련"]
lambda_k_name = lambda k: ''.join(random.sample(first_names, k-1))+''.join(random.sample(name_words, k))
lambda_phone = lambda k: '010-'+str(lambda_number(k))+'-'+str(lambda_number(k))
lambda_birth = lambda startyear, endyear: str(random_number(startyear,endyear))+'-'+str(random_number(1,12))+'-'+str(random_number(1,32))
address_list = ["서울","경기","부산","대구","광주"]
job_list = ["회사원","사업가","개발자","자영업자"]
interests_list = ["영화","주식","부동산","독서"]
if __name__ == '__main__':
    user_email = str(lambda_string(4)) + "@test.com"
    password = '1'
    user_name = lambda_k_name(2)
    phone = lambda_phone(4)
    birth = lambda_birth(1985, 2011)
    address = random.choice(address_list)
    job = random.choice(job_list)
    user_interests = random.choice(interests_list)
    print('user_email:'+user_email)
    print('password: ' + password)
    print('user_name: ' + user_name)
    print('phone: ' + phone)
    print('address: ' + address)
    print('job: ' + job)
    print('user_interests: ' + user_interests)
