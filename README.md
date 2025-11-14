# **인간의 맨몸 비행 가능성에 대한 CFD 시뮬레이션 기반 유체역학적 검증**

> 2025 시흥고등학교 창의융합눈꽃학술제 - 10423 정승환

## 시뮬레이션 파이프라인

이것은 제가 실제로 학술제 연구에 사용한 코드들을 압축해둔 레포지토리입니다. OpenFOAM을 활용한 파라메트릭 스윕 과정에서의 불가피한 반복작업을 자동화하여 효율성을 높이기 위하여 설계한 코드입니다.

---

## 사용 가이드 목차

1. 프로그램 세팅
   * Windows용
   * Linux용

2. 시작
   * 폴더 구조 불러오기

3. 파일 관리
   * 파일/폴더 업데이트 및 삭제 제어

4. OpenFOAM
   * 시뮬레이션 실행  및 후처리

---
## 1\. 프로그램 세팅

###  **Windows**

>\[OS 버전] 실험자는 **Windows 11** 환경에서 진행하였습니다.

아래의 링크들을 클릭하여 프로그램들을 설치하시기 바랍니다.

| 프로그램명                                                                                                                          | 한줄 설명                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| [blueCFD-Core 2024](https://github.com/blueCFD/Core/releases/download/blueCFD-Core-2024-1/blueCFD-Core-2024-1-win64-setup.exe) | Windows용 OpenFOAM(CFD 소프트웨어) |
| [Python 3.14.0](https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe)                                              | 스크립트 작동에 필수적인 프로그래밍 언어       |
| [Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)                                | 코드 편집기                       |
| [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe)            | 버전 관리 프로그램                   |

앞의 모든 다운로드 과정을 마친 후 아래의 명령어를 터미널에 입력합니다.

``` 
curl -L -o PATH.py https://raw.githubusercontent.com/s2510423/2025-2-CFD/main/SetUp/Windows/PATH.py
python PATH.py
```
### **Linux**

>\[OS 버전] 실험자는 Ubuntu 22.04 LTS 환경에서 진행하였습니다.

아래의 명령어를 터미널에 입력합니다.

```
wget https://raw.githubusercontent.com/s2510423/2025-2-CFD/main/SetUp/Linux/CFD.sh
bash CFD.sh
```

포함된 프로그램은 Windows 항목과 동일합니다.

---

