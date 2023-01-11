pip install fastapi 'uvicorn[standard]'
pip install uvicorn
python -m uvicorn main:app --reload
또는 uvicorn main:app --reload


세션(session)이란?
여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법
사용자가 브라우저를 닫아 서버와의 연결을 끝내는 시점까지를 세션
세션은 서비스가 돌아가는 서버 측에 데이터를 저장하고, 세션의 키값만을 클라이언트 측에 남겨둠
브라우저는 필요할 때마다 이 키값을 이용하여 서버에 저장된 데이터를 사용하게 됩니다.
세션은 보안에 취약한 쿠키를 보완해주는 역할

https://davi06000.tistory.com/147
ORM
기존 쿼리문을 직접 작성하여 DB로 날리는 방식-> DB의 Table에 mapping 할 수 있는 형태의 객체를 만들어서 관리하는 방식
불러온 데이터를 파이썬에서 가공할 수 있는 형태로 자동 변환

SQLAlchemy
파이썬에서 ORM이 가능하도록 해주는 툴킷
편하게 파이썬에서 DB를 제어
pip install sqlalchemy

Create a Base class
declarative_base함수로 부터 Base클래스를 리턴받음
나중에 객체를 테이블로 맵핑하는 ORM model이 된다


# create table posts(
#     post_id int(10) AUTO_INCREMENT primary key,
#     title varchar(20),
#     content varchar(20),
#     create_at datetime(20),
#     updated_at datetime(20)
# )charset = utf8;

object 종류
dao - repositories
dto - schemas
vo - models

db권한주기 : mysql -u root -p 다음
grant all privileges on *.* to 'root'@'%' identified by 'root';
