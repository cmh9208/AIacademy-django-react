insert into users(user_email, password, user_name, phone, birth,
                address, job, user_interests)
values ('hong@test.com', '1', '홍길동', '010-1224-5678', '2000-01-01',
                '서울시 강남구', '개발자', '영화감상');

insert into users(user_email, password, user_name, phone, birth,
                address, job, user_interests)
values ('you@test.com', '1', '유관순', '010-3344-5678', '2000-07-01',
                '서울시 강북구', '개발자', '여행');

select * from users;