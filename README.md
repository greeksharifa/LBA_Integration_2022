# LBA_Integration
for SNU LBA task


## 각 연구실별 모듈

- 한양대 prof. 김은솔(김영진) repo: Scene-Graph-Extraction
    - https://github.com/youngyoung1021/Scene-Graph-Extraction
    - 221107 현재. 환경설정은 추후 docker 파일로 전달 예정
    - 221107 현재. 생성된 지식체계 공유 예정
- KAIST prof. 김준모(손형욱) repo: ood-diffusion
    - https://github.com/hushon/ood-diffusion
- KAIST prof. 유창동(윤희석) repo: LBA-ARVQA
    - https://github.com/tomyoon2/LBA-ARVQA
- 경희대 prof. 박성배(박규민) repo: LBA-DramaQG
    - https://github.com/gminipark/LBA-DramaQG


---

# Installation

```bash
git clone --recurse-submodules https://github.com/greeksharifa/LBA_Integration.git

```

## update submodules
```bash
# in root directory
git submodule update --remote LBA-ARVQA
git submodule update --remote ood-diffusion
git submodule update --remote LBA-DramaQG
git submodule update --remote Scene-Graph-Extraction
git submodule update --remote DramaQA
```