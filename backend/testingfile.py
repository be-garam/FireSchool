import re

contents = """
Title: 카이스트 의과학대학원

URL Source: https://gsmse.kaist.ac.kr/pages/sub/sub0201

Markdown Content:
#### 입학 전형

**전형 Timeline**

*   ![Image 1](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_04.png)
    
    온라인 원서접수
    
*   ![Image 2](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_05.png)
    
    1단계 서류전형
    
*   ![Image 3](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_06.png)
    
    2단계 면접전형  
    (인성/논문)
    
*   ![Image 4](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_07.png)
    
    최종 합격자 발표
    

**모집전형 및 일정**

| 구 분 | 봄학기(1차) 모집 | 가을학기 모집 |
| --- | --- | --- |
| 원서접수 | 7월 초 | 4월 초 |
| 서류전형 | 8월 초 | 5월 초 |
| 서류전형 합격자 발표 | 8월 중순 | 5월 중순 |
| 면접전형 | 8월 말 | 5월 말 |
| 최종합격자 발표 | 9월 중순 | 6월 중순 |
| 입학시기 | 다음해 3월 | 당해 9월 |

※ 학과 사정에 따라 모집 시기는 변동될 수 있음

**모집분야**

| 모집분야 | 학생구분별 모집여부 |
| --- | --- |
| 국비 장학생 | KAIST 장학생 | 일반 장학생 |
| --- | --- | --- |
| 석·박사통합과정 | O | O | O |
| 박사과정 | O | O | O |

**지원자격**

 
| 모집과정 | 석·박사통합과정 | 박사과정 |
| --- | --- | --- |
| 의사과학자과정 | 학사학위 취득(예정)자로서 의사면허증, 치과의사면허증 또는 한의사면허증 취득(예정)자 | 석사학위 취득(예정)자로서 의사면허증, 치과의사면허증 또는 한의사면허증 취득(예정)자 (석사과정의 전공은 제한 없음) |
| 의과학자과정 | 이공계 분야 학사학위 취득(예정)자 (약학,수의학 전공자 포함) | 이공계 분야 석사학위 취득(예정)자 (약학, 수의학 전공자 포함) |

**장학생 구분 및 혜택**

  
| 구 분 | 설 명 | 장학혜택 |
| --- | --- | --- |
| 국비 장학생 | 학생 교육경비의 일부를 정부출연금에 의하여 KAIST가 지원하는 학생 | 
*   **국비장학생**
    *   **석·박사통합과정**첫 1년은 석사학자금 지급 그 후는 박사학위과정과 동일
        
    *   **박사과정**1년차 ~ 4년차(8학기간) 조교수당 매월 지급
        
*   **수탁연구조사비**학생이 지도교수를 정한 후, 지도교수의 연구 프로젝트에 동참할 시에 소정의 수탁연구비 지급
    
*   **학생복지**입학생 전원 기숙사 입사 기회
    

 |
| KAIST 장학생 | 학생 교육경비의 일부를 KAIST에서 조성한 장학금, 외부출연기금, 교수연구비 등에서 지원하는 학생 |
| 일반 장학생 | 학생 교육경비의 전부 또는 일부를 산업체, 연구기관, 교육기관, 국가기관 등이 부담하는 학생 ※ 산업체, 연구기관 등 소속기관(직장)에 재직 중인 지원자는 국비나 KAIST장학생으로 지원할 수 없으며, 일반 장학생으로 지원하여야 함. (단, 소속기관이 있더라도 합격 후 입학 전까지 퇴직 예정인 자는 지원 가능함.) |

**온라인 입시설명회**

*   **의사과학자과정**
*   **의과학자과정**

[의과학대학원 공식 ![Image 5](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/yotube_t.png) 바로가기](https://www.youtube.com/channel/UCCrlXfD_Fy_DxSo4lhxZTbQ)
Service UnavailableTitle: 카이스트 의과학대학원

URL Source: https://gsmse.kaist.ac.kr/pages/sub/sub0202

Markdown Content:
#### 트랙소개

KAIST 의과학대학원은 의학, 생명과학, 자연과학, 공학 등 다양한 학문적 배경을 가지고 있는 연구자들이 상호간의 경계를 넘나들며 연구를 수행함으로써 선도적인 의과학 연구를 수행하고 세계 수준의 젊은 연구자들을 배출하는 목표를 가지고 있습니다.  
KAIST의과학대학원은 다학제 융합 교육이 가능한 환경을 갖추고 있습니다. 본교의 생명과학과, 바이오및뇌공학과 및 의과학연구센터와 연계하여 학제간의 교육과 연구를 시행하고 있습니다.

KAIST 의과학대학원은 아래와 같은 두 개의 교육 프로그램을 가지고 있습니다. 이것은 행정적인 필요에 의해 구분된 것으로 실제로는 두 교육 프로그램이 융합되어 운영됩니다.

**M.D.를 위한 Ph.D. 과정** 의사과학자과정

의사과학자과정은 의과대학을 졸업한 의사(치과의사, 한의사 포함) 및 전문의를 대상으로 기초과학과 의공학을 전문적으로 교육하는 Medical Science Training Program 과정으로, 최고 수준의 기초 의과학 및 중개연구 교육을 통해 세계 수준의 의과학자를 양성하는 데 목표가 있습니다.

**생명과학자 & 공학자를 위한 Ph.D. 과정** 의과학자과정

의과학자과정은 생명과학, 자연과학 및 공학 등 다양한 학부를 졸업한 학생들을 대상으로 의생명과학과 의공학을 전문적으로 교육하는 학위과정으로, 최고 수준의 기초 의과학 및 중개연구 교육을 통해 세계 수준의 의과학자를 양성하는 데 목표가 있습니다.

*   *   M.D.학생 입학
        
    *   이공계 학생 입학
        
*   의과학대학원
    
    *   의사과학자과정
        
    *   의과학자과정
        
*   *   M.D.-Ph.D. 졸업
        
    *   Ph.D. 졸업
        

*   학문간/학제간 융합을 통한 교육
*   중개 연구 역량 강화
*   과학윤리 교육 강화
Title: 카이스트 의과학대학원

URL Source: https://gsmse.kaist.ac.kr/pages/sub/sub0404_01

Markdown Content:
#### 랩 로테이션

※ 학과 사정에 따라 변경될 수 있으므로, 세부 내용은 학과사무실로 문의 부탁드립니다.

**랩 로테이션이란**

*   의과학대학원의 모든 신입생은 의과학대학원 전임교수 연구실에서 로테이션한 후 지도교수를 선정함
*   신입생 오리엔테이션 때 의과학대학원 교수님들께서 각 연구실에서 어떤 연구를 하는지 소개하는 시간을 가짐
*   개강 2일차부터 총 3개의 랩을 로테이션함 (랩마다 7일 로테이션)

**절차 (구체적인 일자는 매 학기 학과사무실 담당자가 안내)**

*   개강 전까지 학과사무실 담당자에게 로테이션 희망 연구실 통보
*   학과 위원회에서 검토 후 로테이션 연구실 배정 (연구실 사정에 따라 로테이션 학생을 받지 않을 수 있음)
*   개강 2일차부터 연구실별로 7일씩 총 3회 로테이션 시작
*   로테이션 종료 후 안내되는 제출 기한까지 학과사무실 담당자에게 희망 지도교수 신청서 제출 (희망 지도 교수 신청서는 지도교수님과 상의 후 제출해야 함)
*   필요시 학과 위원회에서 신입생 개별 면담 후 지도교수 최종 결정 및 안내

※ 랩 로테이션 및 지도교수 선정과 관련하여 면담이 필요한 학생은 학과장 면담 신청 가능

**관련 양식**

*   [희망 지도교수 신청서](https://gsmse.kaist.ac.kr/resources/wis-layout/file/\(%EC%96%91%EC%8B%9D\)%ED%9D%AC%EB%A7%9D%20%EC%A7%80%EB%8F%84%EA%B5%90%EC%88%98%20%EC%8B%A0%EC%B2%AD%EC%84%9C.hwp)
Title: 카이스트 의과학대학원

URL Source: https://gsmse.kaist.ac.kr/pages/sub/sub0106

Markdown Content:
#### 학술 교류 프로그램

**KAIST - KU Joint Symposium**

2014년부터 일본 Kumamoto University의 세계적인 연구자들을 초청하여 기초, 임상 중개연구, 융합 신기술 개발에 관한 최신 연구 동향과 연구성과를 교류하고 공동연구를 위한 네트워크를 형성하기 위한 심포지엄을 1년에 2차례 개최하고 있습니다.

![Image 1](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/01.jpg)

**KAIST - KU Joint Symposium**

의과학대학원은 2007년부터 서울아산병원과 공동연구기금을 조성하여 의과학대학원과 서울아산병원 연구자들 간의 커뮤니케이션 장을 마련하고 네트워크를 형성하고자 매년 심포지움을 개최하고 있습니다.

![Image 2](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/02.jpg)

#### 학과 행사 프로그램

**Retreat**

의과학대학원의 교수 및 재학생 등 구성원 모두가 참여하는 행사로 최근에는 신입생도 함께 참여하여 본인을 소개하는 시간을 가지는 등 신입생 O.T를 겸하여 진행되고 있습니다.

![Image 3](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/03.jpg)

**학과 졸업식**

학교에서 진행되는 학위수여식 전에 별도로 학과 졸업식을 마련하여, 모든 학과 구성원들이 졸업생을 축하하고, 졸업생들의 학위 취득 소감을 나누며 함께 앞날을 축복하는 시간을 보내고 있습니다.

![Image 4](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/04.jpg)

**홈커밍데이**

2006년 첫 입학생을 선발한 후 지속적인 성장을 하는 의과학대학원에서는 졸업생, 재학생, 교수 및 직원을 초청하여 학과의 발전상을 알리고 졸업생의 활약상을 보고 듣는 장을 마련하고 있습니다. 이를 통해 구성원의 화합 및 유대를 강화하고 상호 일체감을 형성하면서 의과학대학원의 장기적인 발전을 도모하고자 합니다.

![Image 5](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/05.jpg)

**체육대회**

의과학대학원 전 구성원의 체력증진 및 상호 간의 친목 도모와 건전한 학과 분위기 조성을 위하여 매년 체육대회를 실시하고 있습니다.

![Image 6](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/06.jpg)

**송년회**

의과학대학원에서는 연말에 함께 고생한 구성원들과 한 해를 마무리하고 밝은 새해를 맞이하길 소망하며, 매년 송년회를 마련하여 함께 음식을 나누고 간단한 미니 게임을 하는 등 따뜻한 시간을 보내고 있습니다.

![Image 7](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/07.jpg)

**여성 연구자 간담회**

의과학대학원 내 여성 연구자(교수, 학생, 연구원) 누구나 참여할 수 있는 간담회로 여성으로서 학업 및 연구를 진행하면서 느끼는 점을 함께 공유하는 자리이며, 남성 연구자의 참여도 권장하고 있습니다.

![Image 8](https://gsmse.kaist.ac.kr/resources//wis-layout/images/sub/01/08.jpg)
"""

# want to extract files' links with "https://~.pdf" or .jpg, .hwp format
pattern = r"https?://\S+\.(pdf|hwp)"

# 내용에서 모든 매칭되는 링크 찾기
file_links = re.findall(pattern, contents)

if len(file_links) <= 3:
    i_pattern = r"https?://\S+\.(jpg|png)"
    img_links = re.findall(i_pattern, contents)

links = file_links + img_links