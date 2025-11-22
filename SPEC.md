# 선행 기술 조사 어플리케이션 (Prior Art Search Application)

## 📋 프로젝트 개요

### 목적
특허 출원을 준비하는 발명자, 연구원, 특허 담당자가 핵심 기술 사항에 대한 선행 기술을 효율적으로 조사할 수 있는 웹 어플리케이션 개발

### 주요 가치
- 특허 출원 전 신규성/진보성 사전 검증
- 선행 기술 조사 시간 및 비용 절감
- 체계적인 조사 결과 관리 및 보고서 생성

---

## 🎯 핵심 기능 (Core Features)

### 1. 기술 입력 및 분석
| 기능 | 설명 |
|------|------|
| 기술 명세 입력 | 발명의 명칭, 기술 분야, 핵심 기술 사항, 해결하고자 하는 과제 입력 |
| 키워드 자동 추출 | AI 기반 핵심 키워드 및 동의어/유사어 자동 도출 |
| IPC/CPC 분류 추천 | 입력된 기술 내용 기반 관련 특허 분류 코드 자동 추천 |
| 검색식 생성 | Boolean 연산자 기반 검색식 자동 생성 및 편집 |

### 2. 선행 기술 검색
| 기능 | 설명 |
|------|------|
| 다중 DB 통합 검색 | KIPRIS, USPTO, EPO, Google Patents 등 주요 특허 DB 연동 검색 |
| 비특허 문헌 검색 | Google Scholar, 학술 DB 연동 (논문, 기술 보고서) |
| 실시간 검색 결과 | 검색 진행 상황 및 결과 실시간 표시 |
| 검색 필터링 | 출원일, 국가, 출원인, 기술 분야별 필터링 |

### 3. 결과 분석 및 평가
| 기능 | 설명 |
|------|------|
| 관련도 스코어링 | AI 기반 선행 기술 관련도 자동 점수화 (0-100) |
| 클레임 대비 분석 | 입력된 핵심 기술과 선행 기술 청구항 비교 분석 |
| 기술 요소 매핑 | 발명의 구성 요소별 선행 기술 매핑 테이블 |
| 인용 관계 시각화 | 선행 기술 간 인용 네트워크 그래프 |

### 4. 보고서 생성
| 기능 | 설명 |
|------|------|
| 선행기술조사 보고서 | 표준 양식의 PDF/Word 보고서 자동 생성 |
| 특허성 평가 의견 | 신규성/진보성에 대한 AI 기반 예비 평가 |
| 회피 설계 제안 | 선행 기술 회피를 위한 설계 방향 제안 |
| 내보내기 | Excel, PDF, Word 형식 다운로드 |

### 5. 프로젝트 관리
| 기능 | 설명 |
|------|------|
| 조사 프로젝트 생성 | 발명별 조사 프로젝트 생성 및 관리 |
| 히스토리 관리 | 검색 이력, 분석 결과 저장 및 버전 관리 |
| 협업 기능 | 팀원 초대, 코멘트, 공유 기능 |
| 알림 | 관련 신규 특허 출원 알림 |

---

## 🏗️ 시스템 아키텍처

### 기술 스택

#### Frontend
```
- Framework: React 18+ / Next.js 14+
- 상태 관리: Zustand / React Query
- UI 라이브러리: Tailwind CSS + shadcn/ui
- 차트/시각화: D3.js, Recharts
- 에디터: TipTap (리치 텍스트 에디터)
```

#### Backend
```
- Runtime: Node.js 20+ / Python 3.11+
- Framework: FastAPI (Python) / Express.js (Node)
- API 설계: RESTful API + GraphQL (복잡한 쿼리용)
- 인증: JWT + OAuth 2.0
```

#### AI/ML
```
- LLM: OpenAI GPT-4 / Claude API
- 임베딩: OpenAI Embeddings / Sentence Transformers
- 벡터 DB: Pinecone / Weaviate / Milvus
- NLP: spaCy, KoNLPy (한국어 처리)
```

#### Database
```
- Primary DB: PostgreSQL 15+
- 검색 엔진: Elasticsearch 8+
- 캐싱: Redis
- 파일 저장: AWS S3 / MinIO
```

#### Infrastructure
```
- 컨테이너: Docker + Kubernetes
- CI/CD: GitHub Actions
- 클라우드: AWS / GCP
- 모니터링: Prometheus + Grafana
```

### 시스템 구성도

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Layer                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Web App   │  │ Mobile App  │  │   API SDK   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway (Kong/AWS)                      │
│                  - Rate Limiting, Auth, Routing                  │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Auth Service │    │ Search Service│    │Analysis Service│
│   (인증/인가)  │    │  (검색 엔진)   │    │  (AI 분석)    │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Data Layer                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │PostgreSQL│  │Elastic   │  │ Vector DB│  │  Redis   │        │
│  │          │  │Search    │  │(Pinecone)│  │ (Cache)  │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   External API Integration                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  KIPRIS  │  │  USPTO   │  │   EPO    │  │ Google   │        │
│  │   API    │  │   API    │  │   API    │  │ Patents  │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 데이터 모델

### 주요 엔티티

#### Project (조사 프로젝트)
```typescript
interface Project {
  id: string;
  userId: string;
  title: string;                    // 프로젝트명
  inventionTitle: string;           // 발명의 명칭
  technicalField: string;           // 기술 분야
  problemToSolve: string;           // 해결하고자 하는 과제
  technicalSolution: string;        // 기술적 해결 방안
  keyFeatures: KeyFeature[];        // 핵심 기술 사항
  status: ProjectStatus;
  createdAt: Date;
  updatedAt: Date;
}

interface KeyFeature {
  id: string;
  description: string;              // 기술 사항 설명
  keywords: string[];               // 관련 키워드
  ipcCodes: string[];              // IPC 분류 코드
}
```

#### SearchSession (검색 세션)
```typescript
interface SearchSession {
  id: string;
  projectId: string;
  searchQuery: SearchQuery;
  results: SearchResult[];
  totalCount: number;
  executedAt: Date;
}

interface SearchQuery {
  keywords: string[];
  booleanExpression: string;        // 검색식
  ipcCodes: string[];
  dateRange: DateRange;
  countries: string[];
  databases: string[];              // 검색 대상 DB
}
```

#### PriorArt (선행 기술)
```typescript
interface PriorArt {
  id: string;
  projectId: string;
  type: 'PATENT' | 'PAPER' | 'OTHER';
  
  // 특허 정보
  publicationNumber: string;        // 공개번호
  applicationNumber: string;        // 출원번호
  title: string;
  abstract: string;
  claims: Claim[];
  applicant: string;
  inventor: string;
  filingDate: Date;
  publicationDate: Date;
  ipcCodes: string[];
  country: string;
  
  // 분석 결과
  relevanceScore: number;           // 관련도 점수 (0-100)
  featureMapping: FeatureMapping[]; // 기술 요소 매핑
  userNotes: string;
  status: 'RELEVANT' | 'NOT_RELEVANT' | 'REVIEW_NEEDED';
}

interface FeatureMapping {
  keyFeatureId: string;
  matchedContent: string;
  matchType: 'IDENTICAL' | 'SIMILAR' | 'PARTIAL' | 'NONE';
  confidence: number;
}
```

#### Report (보고서)
```typescript
interface Report {
  id: string;
  projectId: string;
  type: ReportType;
  content: ReportContent;
  generatedAt: Date;
  format: 'PDF' | 'DOCX' | 'XLSX';
  fileUrl: string;
}

type ReportType = 
  | 'PRIOR_ART_SEARCH'      // 선행기술조사 보고서
  | 'PATENTABILITY'         // 특허성 평가 보고서
  | 'FREEDOM_TO_OPERATE'    // FTO 분석 보고서
  | 'CLAIM_CHART';          // 클레임 차트
```

---

## 🔌 외부 API 연동

### 특허 데이터베이스

#### KIPRIS (한국특허정보원)
```yaml
Base URL: http://plus.kipris.or.kr/openapi/rest
인증: API Key
주요 엔드포인트:
  - /patUtiModInfoSearchSevice  # 특허/실용신안 검색
  - /trademarkInfoSearchService # 상표 검색
  - /designInfoSearchService    # 디자인 검색
Rate Limit: 1000 requests/day (기본)
```

#### USPTO (미국특허청)
```yaml
Base URL: https://developer.uspto.gov/api
인증: API Key
주요 엔드포인트:
  - /patent/v1/search           # 특허 검색
  - /patent/v1/publication      # 공보 조회
Rate Limit: 10000 requests/day
```

#### EPO Open Patent Services
```yaml
Base URL: https://ops.epo.org/rest-services
인증: OAuth 2.0
주요 엔드포인트:
  - /published-data/search      # 공개 특허 검색
  - /family/publication         # 패밀리 특허 조회
Rate Limit: 4 requests/second
```

#### Google Patents (BigQuery)
```yaml
Dataset: patents-public-data
테이블: patents.publications
인증: Google Cloud Service Account
쿼리: BigQuery SQL
```

### 학술 데이터베이스

#### Semantic Scholar API
```yaml
Base URL: https://api.semanticscholar.org/graph/v1
인증: API Key (선택)
Rate Limit: 100 requests/5min (인증 시 증가)
```

#### CrossRef API
```yaml
Base URL: https://api.crossref.org
인증: Polite Pool (이메일 제공 시)
Rate Limit: 50 requests/second
```

---

## 🖥️ UI/UX 설계

### 주요 화면

#### 1. 대시보드
- 진행 중인 프로젝트 목록
- 최근 검색 히스토리
- 주요 통계 (검색 수, 발견된 선행기술 수)
- 알림 센터

#### 2. 프로젝트 생성/편집
- 발명 정보 입력 폼
- 핵심 기술 사항 추가 (다중)
- AI 키워드 추천 패널
- IPC/CPC 코드 선택기

#### 3. 검색 화면
- 검색식 빌더 (시각적 Boolean 편집기)
- 데이터베이스 선택
- 필터 패널 (날짜, 국가, 출원인 등)
- 실시간 검색 결과 미리보기

#### 4. 결과 분석 화면
- 선행기술 목록 (카드/테이블 뷰)
- 관련도 기반 정렬
- 상세 보기 모달
- 기술 요소 매핑 매트릭스
- 인용 네트워크 그래프

#### 5. 보고서 생성
- 보고서 템플릿 선택
- 포함할 선행기술 선택
- 미리보기
- 다운로드/공유

### 와이어프레임 구조

```
┌────────────────────────────────────────────────────────────┐
│  🔍 Prior Art Search                    [알림] [프로필]    │
├────────────┬───────────────────────────────────────────────┤
│            │                                               │
│  📁 프로젝트 │  ┌─────────────────────────────────────────┐ │
│            │  │        프로젝트: 스마트 IoT 센서          │ │
│  ▶ 진행중   │  ├─────────────────────────────────────────┤ │
│    - IoT   │  │  [기술입력] [검색] [결과분석] [보고서]   │ │
│    - AI    │  ├─────────────────────────────────────────┤ │
│            │  │                                         │ │
│  ▶ 완료    │  │   핵심 기술 사항                        │ │
│            │  │   ┌─────────────────────────────────┐   │ │
│            │  │   │ 1. 저전력 무선 통신 모듈        │   │ │
│  + 새 프로젝트│  │   │    키워드: BLE, LoRa, 저전력    │   │ │
│            │  │   └─────────────────────────────────┘   │ │
│            │  │   ┌─────────────────────────────────┐   │ │
│            │  │   │ 2. 엣지 컴퓨팅 데이터 처리      │   │ │
│            │  │   │    키워드: edge, 실시간, 처리    │   │ │
│            │  │   └─────────────────────────────────┘   │ │
│            │  │                                         │ │
│            │  │   [+ 기술사항 추가]  [AI 키워드 추천]   │ │
│            │  │                                         │ │
│            │  └─────────────────────────────────────────┘ │
└────────────┴───────────────────────────────────────────────┘
```

---

## 🔐 보안 요구사항

### 인증/인가
- OAuth 2.0 / OpenID Connect 기반 인증
- JWT 토큰 기반 세션 관리
- RBAC (Role-Based Access Control)
- MFA (Multi-Factor Authentication) 지원

### 데이터 보안
- 전송 중 암호화: TLS 1.3
- 저장 시 암호화: AES-256
- 민감 정보 마스킹
- 개인정보 처리방침 준수 (GDPR, 개인정보보호법)

### API 보안
- Rate Limiting
- API Key 관리
- Request 서명 검증
- CORS 정책

---

## 📈 성능 요구사항

| 항목 | 목표 |
|------|------|
| 검색 응답 시간 | < 3초 (단일 DB), < 10초 (통합 검색) |
| 페이지 로드 시간 | < 2초 |
| AI 분석 시간 | < 30초 (건당) |
| 동시 사용자 | 1,000명 이상 |
| 가용성 | 99.5% |
| 데이터 백업 | 일일 자동 백업 |

---

## 🚀 개발 로드맵

### Phase 1: MVP (3개월)
- [ ] 사용자 인증 시스템
- [ ] 프로젝트 생성/관리
- [ ] 기본 키워드 검색 (KIPRIS)
- [ ] 검색 결과 목록 표시
- [ ] 기본 보고서 생성 (PDF)

### Phase 2: 핵심 기능 (3개월)
- [ ] AI 키워드 추출/추천
- [ ] 다중 DB 통합 검색 (USPTO, EPO)
- [ ] 관련도 스코어링
- [ ] 기술 요소 매핑
- [ ] 고급 검색식 빌더

### Phase 3: 고급 기능 (3개월)
- [ ] 비특허 문헌 검색
- [ ] 인용 네트워크 시각화
- [ ] 특허성 평가 AI
- [ ] 협업 기능
- [ ] 신규 특허 알림

### Phase 4: 확장 (지속)
- [ ] 모바일 앱
- [ ] API 제공 (B2B)
- [ ] 다국어 지원
- [ ] 고급 분석 리포트

---

## 💰 비용 추정

### 초기 개발 비용 (MVP)
| 항목 | 비용 (추정) |
|------|------------|
| 개발 인력 (4명 x 3개월) | 1.2억원 |
| 클라우드 인프라 (초기) | 500만원 |
| API 라이선스 | 300만원 |
| 기타 (도구, 라이선스) | 200만원 |
| **합계** | **약 1.4억원** |

### 월간 운영 비용 (예상)
| 항목 | 비용 |
|------|------|
| 클라우드 인프라 | 300-500만원 |
| 외부 API 사용료 | 100-300만원 |
| AI API (OpenAI 등) | 200-500만원 |
| 유지보수 인력 | 500만원 |
| **합계** | **약 1,100-1,800만원/월** |

---

## 📝 참고 사항

### 법적 고려사항
- 특허 데이터 이용 약관 준수
- 저작권 관련 면책 조항
- 서비스 이용약관 및 개인정보처리방침

### 제약사항
- 외부 API 의존성 및 변경 가능성
- 특허청 API Rate Limit
- AI 분석 정확도 한계 (참고용임을 명시)

### 향후 확장 고려
- 특허 번역 서비스 연동
- 특허 출원 대행 연계
- 특허 가치 평가 기능
- 기술 이전/라이선싱 마켓플레이스

---

## 📎 부록

### A. IPC 분류 체계 개요
### B. Boolean 검색식 문법
### C. API 응답 스키마 예시
### D. 용어 정의

---

*문서 버전: 1.0*  
*최종 수정일: 2025년*  
*작성자: Claude AI*