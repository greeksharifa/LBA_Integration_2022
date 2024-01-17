# LBA_2024
LBA 통합시스템(2024 ver.)

## Installation

```
# repository clone
git clone https://github.com/greeksharifa/LBA_2024.git

# 서브모듈 정보를 기반으로 로컬 환경설정 파일을 만들어준다.
git submodule init

# 서브모듈의 리모트 저장소에서 데이터를 가져오고 Checkout을 한다.
git submodule update
```


### git submodule update

```
# 서브모듈이 외부에서 업데이트가 되었을 때 현재 사용하려는 메인 깃에도 반영
git submodule update 

# 서브모듈 명령어 한 번에 실행하기
git submodule foreach 'git pull'
```
