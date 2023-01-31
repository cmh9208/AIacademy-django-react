from starlette.responses import JSONResponse
from faker import Faker
from app.admin.utils import between_random_date
from app.database import get_db
from app.cruds.user import UserCrud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.user import UserDTO

router = APIRouter()


@router.get("/page/{request_page}")
def pagination(request_page: int, db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    block_size = 10
    response_page = request_page - 1  # 넘겨받은 page번호를 인덱스 값으로 전환
    page_cnt_mok = row_cnt // page_size
    page_cnt_nmg = row_cnt % page_size
    page_cnt = page_cnt_mok if (page_cnt_nmg == 0) else page_cnt_mok + 1
    block_cnt_mok = page_cnt // page_size
    block_cnt_nmg = page_cnt % block_size
    block_cnt = block_cnt_mok if (block_cnt_nmg == 0) else block_cnt_mok + 1
    start_row_per_page = page_size * (response_page)
    response_block = (response_page) // block_size
    last_row_idx_per_total = row_cnt - 1
    last_row_idx_per_page = page_size - 1
    end_row_per_page = start_row_per_page + last_row_idx_per_page \
        if request_page != page_cnt \
        else last_row_idx_per_total
    start_page_per_block = response_block * block_size
    last_page_idx_per_total = page_cnt - 1
    last_block_idx_per_total = block_cnt - 1
    last_page_idx_per_block = block_size - 1
    end_page_per_block = start_page_per_block + last_page_idx_per_block \
        if response_block != last_block_idx_per_total \
        else last_page_idx_per_total

    print("### 테스트 ### ")
    print(f"start_row_per_page ={start_row_per_page}")
    print(f"end_row_per_page ={end_row_per_page}")
    print(f"start_page_per_block ={start_page_per_block}")
    print(f"end_page_per_block ={end_page_per_block}")

    '''
    row_cnt = 11, page_size = 5
    page  row_start row_end
    1 = 0 ~ 4
    2 = 5 ~ 9
    3 = 10

     | ### 테스트 ###
    api   | row_start =5
    api   | row_end =10 -> 9
    api   | page_start =0
    api   | page_end =2
    api   |  count is 11
    '''
    print(f" count is {row_cnt}")
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=row_cnt))


@router.get("/many")
def insert_many(db: Session = Depends(get_db)):
    print(f" Faker 작동 ")
    [UserCrud(db).add_user(create_faker_user()) for i in range(100)]


def create_faker_user():
    faker = Faker('ko_KR')
    return UserDTO(email=faker.email(), password="11aa",
                   username=faker.name(), birth=between_random_date(),
                   address=faker.city())