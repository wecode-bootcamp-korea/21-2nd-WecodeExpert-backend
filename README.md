# 21-2nd-WecodeExpert-backend
김민규, 박창현, 정효진

## WecodeExpert 프로젝트 Back-end 소개

- 네이버 Expert [네이버 Expert](https://m.expert.naver.com/)를 모티브로 한 프로젝트 
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 아래 데모 영상에서 보이는 부분은 모두 백앤드와 연결하여 실제 서비스 동작과 비슷하게 개발하였습니다.

### 개발 인원 및 기간

- 개발기간 : 2021/06/21 ~ 2021/7/02
- 개발 인원 : 프론트엔드 2명, 백엔드 3명


### 데모 영상

*추후 추가*

<br>

## 사용 기술 및 구현 기능


### 사용 기술 및 tools
> - Front-End : <img src="https://img.shields.io/badge/ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React.js-61DAFB?style=for-the-badge&logo=React&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React%20Router-CA4245?style=for-the-badge&logo=React-router&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/styled-component-CC6699?style=for-the-badge&logo=sass&logoColor=white"/>
> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2.4-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Mysql 8.0-4479A1?style=for-the-badge&logo=Mysql&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PyJWT 2.1-000000?style=for-the-badge&logo=JsonWebTokens&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Bcrypt 3.2-338000?style=for-the-badge&logo=PyJWT&logoColor=white"/>
> - Common : <img src="https://img.shields.io/badge/AWS RDS/EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=Trello&logoColor=white"/>

<img width="1859" alt="스크린샷 2021-06-18 오전 7 28 39" src="">

[AQueryTool(pw:bup04w)]()

### 구현 기능

#### Users app - 효진
- `Kakao api`를 이용한 소셜 로그인 구현 
- `JWT`를 이용한 User 정보 토큰발행
-  토큰 확인 데코레이터 구현
-  expert 등록, 로그인/회원가입 api 작성

#### Products app - 민규
- 조건에 맞게 쿼리파라미터를 받아서 `Q객체`를 이용한 상품 필터링 및 정렬 (최근등록순, 인기상품순, 가격높은순, 가격낮은순)
- 쿼리파라미터를 이용한 페이징 기능
- 한 개의 상품에 대한 상세 정보, 리뷰 제공

#### Orders app - 창현
- 상품,유저정보 테이블 활용하여 CRUD Create 및 filter로 결제기능 구현.
- AWS : EC2,RDS서버구축 및 배포작업 담당.
- s3를 활용한 사진 업로드
- docker 구축
 
<br>

## Reference

- 이 프로젝트는 [네이버 Expert](https://m.expert.naver.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
