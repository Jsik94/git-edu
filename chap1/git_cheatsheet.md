# Git 치트시트

## 자주 사용하는 명령어들

### 초기 설정
```bash
git config --global user.name "사용자명"
git config --global user.email "이메일@example.com"
```

### 기본 워크플로우
```bash
# 1. 파일 상태 확인
git status

# 2. 파일 스테이징
git add .                    # 모든 파일 추가
git add <파일명>             # 특정 파일만 추가

# 3. 커밋
git commit -m "커밋 메시지"

# 4. 원격 저장소에 푸시
git push origin main
```

### 브랜치 관리
```bash
# 브랜치 목록 보기
git branch

# 새 브랜치 생성 및 전환
git checkout -b <브랜치명>

# 브랜치 전환
git checkout <브랜치명>

# 브랜치 삭제
git branch -d <브랜치명>
```

### 히스토리 확인
```bash
# 커밋 히스토리 보기
git log

# 간단한 히스토리
git log --oneline

# 변경사항 확인
git diff
```

### 되돌리기
```bash
# 마지막 커밋 취소 (파일은 유지)
git reset --soft HEAD~1

# 마지막 커밋 완전 삭제
git reset --hard HEAD~1

# 특정 파일만 되돌리기
git checkout HEAD -- <파일명>
```
