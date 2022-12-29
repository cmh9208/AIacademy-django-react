


# ## 대수학(algebra)
# 변수는 feature 와 target 으로 나뉜다.
# 상수는 계수와 편향로 나뉜다.
# 따라서 다음과 같은 식의 구조를 같는다.
# target = 계수 * featureValue + 편향
# 특성변수 = 독립변수 = 외생변수 = x변수
# 목적변수 = 종속변수 = 내생변수 = y변수
# - 계수(係數, coefficient)는 '인자(因子)'라는 뜻으로 쓰인다.
# - 보통 식 앞에 곱해지는 상수를 말한다.
# - 가장 흔한 계수의 개념은 다항식에서 x n 앞에 붙는 수이다.
#
# ## 데이터(Data)
# -- Data has a categorical, numeric.
# 카테고리(categorical) = 이산형 = norminal + ordinal = 정수형
# 숫자형(numeric) = 연속형 = ratio + interval = 실수형
# -- 데이터 분석에는 두 가지의 접근방법이 있다.
# 1) 확증적 데이터 분석(CDA: Confirmatory Data Analysis) = 추론통계 = 가설 -> .. -> 특정 사례 예측 = 연역
# 2) 탐색적 데이터 분석(EDA: Exploratory Data Analysis) = 기술통계 = 데이터 -> .. -> 모델 = 귀납
#
# ## 머신러닝(Machine Learning)
# Machine-Learning has a statistics, deep learning.
# The difference lies in the existence of evidence.
# 머신러닝은 통계와 딥러닝의 집합이다.
# 머신러닝과 딥러닝의 차이점은 신경망의 유무이다.
#
# -- ML 을 위한 통계개념
# 표본
# 우도함수
# 대수의 법칙
# 베이지안
# 분포
# 랜덤
#
# ## 정규화(Normalization)
# https://heeya-stupidbutstudying.tistory.com/entry/%ED%86%B5%EA%B3%84-%EC%A0%95%EA%B7%9C%ED%99%94%EC%99%80-%ED%91%9C%EC%A4%80%ED%99%94
# feature 의 변환은 표준화(Z-score 정규화)와 정규화가 있다.
# 아웃라이어가 있으면 표준화 나머지는 정규화가 낫다.
#
# ## 학습(Learning)
# 통계학에서 학습은 추정문제 해결과정(=추론)이다.
# learning 은 target 을 구하는 modeling 이다.
# -- 학습은 두가지 종류가 있다.
# 지도학습은 샘플을 사용한다.
# 비지도학습은 샘플을 사용하지 않는다.
#
# ## 확률(Probability)
# 선험적 통계 = 사전, 수학적 확률, 식 -> 연역법
# 경험적 통계 = 사후,  통계적 확률, 식 * "큰수의 법칙" -> 귀납법
# 기대값 = 계수 * 변수 + 상수
#
#
# 인코딩
#
# 지도학습 분류 classification / 회귀 regress 로 나뉜다.
# model 은 var 를 잡아내서, class 를 시도한다.
#
# ## (확률) 분포는 함수다
# 리턴값에 따라 정수는 PMF, 실수는 PDF 를 사용한다.
# 인공지능에서는 Dense 레이어를 사용하므로, 리턴값은 실수로 정의한다.
# 확률분포는
# 이산 - 확률질량함수 PMF: 이항분포, 다항분포, 이산균등분포, 푸아송분포, 베르누이분포, (초)기하분포
# 연속 - 확률밀도함수 PDF: 정규분포(=가우스분포), 연속균등분포, 카이제곱분포, 감마분포
#
# # 연역과 귀납
# 연역은 가정된 전제이다.
# 귀납은 개인적 경험이다.
#
# # 편향과 편차
# https://opentutorials.org/module/3653/22071
# 정답 하나를 맞추기 위해 컴퓨터는 여러 번의 예측값 내놓기를 시도하는데,
# 컴퓨터가 내놓은 예측값의 동태를 묘사하는 표현이 '편향' 과 '분산' 입니다.
#
# 예측값들과 정답이 대체로 멀리 떨어져 있으면 결과의 편향(bias)이 높다고 말하고,
# 예측값들이 자기들끼리 대체로 멀리 흩어져있으면 결과의 분산(variance)이 높다고 말합니다.
#
# 회귀 문제이든, 분류 문제이든
# 첫 번째 그림과 같은 상황을 Underfitting = High Bias
# 세 번째 그림과 같은 상황을 Overfitting이라고 합니다. = High Variance
#
# ## 추정에 있어 통계학의 손실함수에는 평균제곱오차 또는 음의 로그 우도함수가 있으며
#    머신러닝에서도 동일한 손실함수를 사용한다.
# ## 우도함수: 우도 함수(가능도 함수로 번역되기도 하고, 영어로는 likelihood function 이라 합니다)
# 는 실현된 데이터(혹은 관찰된 데이터 observed data)로 부터
# 특정 통계 모델의 적합성을 확인하는데 주로 이용됩니다.




# ## 손실함수 혹은 비용함수(cost function)는 같은 용어로 통계학, 경제학 등에서 널리 쓰이는 함수로
#     머신러닝에서도 손실함수는 예측값과 실제값에 대한 오차를 줄이는 데 사용된다.
#
# ## MSE vs. CCEE
# 회귀ML 의 손실함수는 MSE 이다
# 분류ML 의 손실함수는 CCEE 이다. 활성화함수로 Softmax 를 사용한다.
#
# ## 데이터셋
# https://for-my-wealthy-life.tistory.com/19
# 여태까지 공부를 할 때는 train set과 test set 두개로만 데이터를 나누었다.
# 다만 이렇게 train, test 두개로만 분리하는 것은 기초적인 수준이고,
# 보통 현업에서 모델을 만들 때는 train, test, validation set 세개로 나눈다.
#
# validation dataset is a sample of data held back from training your model that is used to give an estimate of model skill while tuning model’number hyperparameters.
# The validation dataset is different from the test dataset that is also held back from the training of the model, but is instead used to give an unbiased estimate of the skill of the final tuned model when comparing or selecting between final models.
# There is much confusion in applied machine learning about what a validation dataset is exactly and how it differs from a test dataset.
#
# ##  기계학습의 관점에서 보았을때 Ground-truth는 학습하고자 하는 데이터의 원본 혹은 실제 값을 표현할때 사용됩니다
# https://eair.tistory.com/16
#
# ## DecisionTree Learning 에서 불순도를 계산하는 3가지 방법
# https://m.blog.naver.com/samsjang/220978650404
# 지니 인덱스
# 엔트로피
# 분류오류
#
# ## 불순도란 다양한 범주들의 개체들이 얼마나 포함되었는가 정도이다.
# 여러가지 클래스가 섞여있는 정도이다. 반대로 순수도(purity)는 같은 클래스끼리
# 얼마나 많이 포함되어 있는지를 말한다.
# https://computer-science-student.tistory.com/60
#
# ## criterion 은 표준이다. 동의어로는
# standard, normal, norm, average, level 이 있다.
#
# ## 엔트로피(영어: entropy, 독일어: entropie):https://ko.wikipedia.org/wiki/%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BC
# 열역학적 계의 유용하지 않은 (일로 변환할 수 없는) 에너지의 흐름을 설명할 때 이용되는 상태 함수다.
# 통계역학적으로, 주어진 거시적 상태에 대응하는 미시적 상태의 수의 로그로 생각할 수 있다.
# 엔트로피는 일반적으로 보존되지 않고, 열역학 제2법칙에 따라 시간에 따라 증가한다.
# 독일의 물리학자 루돌프 클라우지우스가 1850년대 초에 도입하였다.
# 대개 기호로 라틴 대문자 S를 쓴다.
#
# ## 산술급수 와 기하급수



# 기술통계 - 추론통계 =학습(Learning)

# 가설(hypothesis)
# p-value (확률값)
