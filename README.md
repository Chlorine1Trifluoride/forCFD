# **인간의 맨몸 비행 가능성에 대한 <br> CFD 시뮬레이션 기반 유체역학적 검증**

<br>

> 2025 시흥고등학교 창의융합눈꽃학술제 - 10423 정승환

<br><br>

## 시뮬레이션 파이프라인

<br>

이것은 제가 실제로 학술제 연구에 사용한 코드들을 압축해둔 레포지토리입니다. OpenFOAM을 활용한 파라메트릭 스윕 과정에서의 불가피한 반복작업을 자동화하여 효율성을 높이기 위하여 설계한 코드입니다.

<br><br>

## 사용 가이드 목차

1. [프로그램 세팅](#1-프로그램-세팅)
   * Windows용
   * Linux용

2. [시작](#2-시작)
   * 폴더 구조 불러오기

3. [파일 관리](#3-파일-관리)
   * 파일/폴더 업데이트 및 삭제 제어

4. [OpenFOAM](#4-openfoam)
   * 시뮬레이션 실행  및 후처리

<br><br><br><br><br>

## 1. 프로그램 세팅

<br>

### **Windows**

>\[OS 버전] 실험자는 **Windows 11** 환경에서 진행하였습니다.

<br>

아래의 링크들을 클릭하여 프로그램들을 설치합니다.

| 프로그램명 | 한줄 설명 |
| - | - |
| [blueCFD-Core 2024](https://github.com/blueCFD/Core/releases/download/blueCFD-Core-2024-1/blueCFD-Core-2024-1-win64-setup.exe) | Windows용 OpenFOAM(<span title='Computational Fluid Dynamics, 전산유체역학'>CFD 소프트웨어</span>) |
| [Python 3.14.0](https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe)                                              | 스크립트 작동에 필수적인 프로그래밍 언어       |
| [Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)                                | 코드 편집기                       |
| [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe)            | 버전 관리 프로그램                   |

<br>

앞의 모든 다운로드 과정을 마친 후 아래의 명령어를 터미널에 입력합니다.

``` Powershell or CMD
Invoke-WebRequest -Uri (TODO:raw 링크 가져올것:SetUp/Windows/PATH.py) -OutFile PATH.py
```

<br>

### **Linux**

>\[OS 버전] 실험자는 Ubuntu 22.04 LTS 환경에서 진행하였습니다.

<br>

아래의 명령어를 터미널에 입력합니다.

``` bash
wget (TODO:raw 링크 가져올것)
bash CFD.sh
```

포함된 프로그램은 Windows 항목과 동일합니다.

<br><br><br><br><br>

## 2. 시작

<br>

#### 1. <span title='CMD, PowerShell, Linux용 터미널 등'>터미널</span>에서 'CFD' 폴더에 접근합니다. 

또는 파일 탐색기에서 'CFD' 폴더에서 우클릭 후 '터미널에서 열기'를 마우스로 선택합니다.

<br>

#### 2. 다음의 명령어를 입력합니다.

   이때, Linux 혹은 Mac OS 운영체제의 경우 'python'명령어 대신 'python3' 명령어를 사용합니다.

   ```terminal

   python start.py

   ```

   실행 직후 'p1','p2','check' 등의 정체를 알 수 없는 폴더들이 생성될 것입니다.

<br><br><br><br><br>

## 3. 파일 관리

<br>

뒤지겠네 시발

<br><br><br><br><br>

## 4. OpenFOAM

<br>

아오 시발 이걸 언제 다 쓰고 자빠졌냐 미치겠네 진짜

<br><br><br><br><br>

## **라이선스**
 ***License***

<br>

이 프로젝트는 GNU 일반 공중 사용 허가서 버전 3(GPL v3.0)에 따라 배포됩니다. <br>자세한 내용은 [LICENSE](./LICENSE) 파일을 참고하세요.

This project is licensed under the GNU General Public License v3.0 <br> see the [LICENSE](./LICENSE) file for details.

<br><br><br><br><br>