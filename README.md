# LBA_platform
문서2: 멀티모달 시계열 데이터 OOD 정보에 대한 불확실성 자각 및 질문 성장 기술 검증 플랫폼 설계

- 기술 검증 플랫폼을 위한 멀티모달 시계열 데이터 장면 이해 및 스토리 학습 태스크 정의
- 기술검증 실험을 위한 OOD 정보를 내포하고 OOD 해결을 위한 올바른 정보도 알고 있는 데이터셋 설계
- 기존 멀티모달 시계열 데이터 관련 데이터셋에 다양한 시구간 길이에 기반한 물체, description 등의 메타정보 데이터셋 구축 계획 수립.


## Installation

```
# repository clone
git clone https://github.com/greeksharifa/LBA_platform.git

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