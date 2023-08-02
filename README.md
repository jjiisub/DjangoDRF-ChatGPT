# DjangoDRF-ChatGPT

- Django DRF로 ChatGPT API와 연동하는 프로젝트 repository입니다

## 1. 프로젝트 목표

- Django DRF와 ChatGPT API를 이용하여 영어학습 챗봇 서비스 구현

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

#### - 기술 스택

- <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">

- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

- <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">

- <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

- <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">

- <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">

- <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">

- <img src="https://img.shields.io/badge/BootStrap-7952B3?style=for-the-badge&logo=BootStrap&logoColor=white">

#### - 서비스 배포 환경

- <img src="https://img.shields.io/badge/AWS LightSail-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">

- <img src="https://img.shields.io/badge/Github Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white">

### 2.2 배포 URL

- ~~http://13.209.37.52:8000/~~

## 3. 프로젝트 구조와 개발 일정

### 3.1 ERD model

![ERD](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/3166f898-6544-4c9e-862c-8dd934391038)

### 3.2 폴더 구조

```bash
django-chat
├── account
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chat
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```

### 3.3 개발 일정

- 2023.07.26 ~ ing

## 4. 페이지 화면

### 4.1 Main & 채팅

| 메인 페이지                                                                                               | 채팅 화면                                                                                                 |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ![main](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/42924f22-8b05-4b6d-9364-ae8d3a69067d) | ![chat](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/1b1848d5-067a-439f-a037-ab924123b4ce) |

### 4.2 User 계정

| 로그인                                                                                                     | 회원가입                                                                                                      |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ![login](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/f50b23ca-3197-4d0f-ad60-ec9a2ba659ba) | ![register](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/e98b279a-0054-4bd7-84bc-928e2d64d5be) |

## 5. 기능

### 5.1 URL 리스트

| URL                 | 기능        |
| ------------------- | ----------- |
| 'list'              | 채팅방 목록 |
| 'chatbot/chat'      | 채팅        |
| '/account/register' | 회원가입    |
| '/account/login'    | 로그인      |
| '/account/logout'   | 로그아웃    |

### 5.2 세부 기능

- 회원가입

    <img width=1000 src="https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/98249414-ef65-4be8-8a49-7a7f73b0d0ba">

  ```js
  document.getElementById("register-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:8000/account/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.state) {
          alert("회원가입이 완료되었습니다.");
          window.location.replace("./login.html");
        } else {
          const error_msg = JSON.stringify(data.error);
          alert(error_msg);
        }
      })
      .catch((error) => {
        alert("회원가입 실패: " + error.message);
      });
  });
  ```

  입력된 username과 password로 새로운 User를 저장하고, 해당 user에 연결된 token을 생성한다. 정상적으로 회원가입이 된 경우에는 state가 True로 전달된다. front-end에서 state를 확인하고, true이면 로그인 페이지도 이동한다.

- 로그인 로그아웃

  | 로그인                                                                                                          | 로그아웃                                                                                                           |
  | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
  | ![로그인](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/5d278bb3-28d0-420c-83b4-39a4468076b8) | ![로그아웃](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/5cb8a36f-2598-498c-84c2-4eca197eedcc) |

  username과 password를 입력받아서 "/account/login/"로 POST 요청을 보낸다. 서버에서 로그인 인증에 성공하면 state True와 함께 해당 user의 token을 전달한다. 브라우저에서는 state가 ture인지 확인하고 username와 token을 쿠키에 저장한 후 메인 페이지로 이동한다.

  ```js
  function checkToken() {
    const loginToken = document.cookie.match("(^|;) ?" + "loginToken" + "=([^;]*)(;|$)");
    if (loginToken) {
      alert("이미 로그인된 상태입니다.");
      window.location.replace("./index.html");
    }
  }
  ```

  로그인 페이지로 이동하면 우선 쿠키에 token이 저장되어 있는지를 확인하여 현재 로그인 상태인지 체크한다. 만약 이미 로그인된 상태이면 alert로 이를 알려주고 메인 페이지로 이동한다.

- 네비게이션 바

  | 로그인                                                                                                              | 로그아웃                                                                                                               |
  | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
  | ![로그인_nav](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/b76cdc95-e423-42ce-ba35-4d162e64a4d6) | ![로그아웃_nav](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/4c465a04-0e1e-4d39-98d6-018a7c7db6f6) |

  ```js
  const loginToken = getCookie("loginToken");
  const navBtnList = document.querySelector(".nav-btn");
  if (loginToken) {
    navBtnList.innerHTML = `
      <li class="nav-item">
          <span class="navbar-text"> 환영합니다 ${username} 님 | </span>
      </li>
      <li class="nav-item">
          <a class="nav-link" onclick="logout()" href="./index.html">로그아웃</a>
      </li>`;
  } else {
    navBtnList.innerHTML = `
      <li class="nav-item">
          <a class="nav-link" href="./login.html">로그인</a>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="./register.html">회원가입</a>
      </li>
      `;
  }
  ```

  로그인이 성공적으로 이루어지면 브라우저 쿠키에 token과 username을 저장한다. 쿠키에 loginToken이 저장되어 있는지 확인하여 로그인 여부를 알 수 있고, 로그인 상태이면 네비게이션 바에 username과 함께 로그아웃 버튼을 출력한다. 로그아웃된 상태이면 로그인과 회원가입 버튼을 출력한다.

- 채팅방 목록

  | 로그인 전                                                                                                   | 로그인 후                                                                                                  |
  | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
  | ![logout](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/59a30d6b-8dbb-4fb4-9086-ec4edf1204d8) | ![login](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/dec3f654-0641-4101-b4ce-e33e098d227d) |

  로그인이 성공적으로 이루어지면 메인화면으로 연결된다. 로그인된 상태에서는 메인화면에 해당 유저가 생성한 채팅방 목록이 출력되며, 클릭하여 해당 채팅방으로 이동할 수 있다. 로그인되지 않은 상태에서는 채팅방 목록이 출력되지 않는다.

- 채팅
  |불러오기|채팅|
  |--|--|
  |![채팅불러오기](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/0235c8cd-3d85-470a-b2eb-34d3fb6f732b)|![채팅](https://github.com/vBORIv/DjangoDRF-ChatGPT/assets/89283288/181e49e9-2e0e-400e-be37-7a00dd4dcdae)|

  ```js
  function loadChat() {
    fetch("http://127.0.0.1:8000/?room=" + room)
      .then((response) => response.json())
      .then((data) => {
        // 요청이 성공적으로 완료된 후에 실행될 코드
        const response = document.getElementById("response");
        data.forEach((element) => {
          makeUserChatBox(element.prompt);
          makeAIChatBox(element.response);
        });
        keepScrollDown();
      })
      .catch((error) => {
        // 요청 중 에러가 발생했을 때 실행될 코드
        console.error("요청 에러:", error);
      });
  }
  ```

  채팅방 목록에서 하나를 선택하면, 서버의 '/chatbot/chat/'으로 GET 요청을 보내서 현재 로그인된 유저와 선택된 채팅방 정보를 전달한다. 서버에서는 유저와 채팅방 이름으로 선택한 채팅방을 찾고, 해당 채팅방에 연결된 모든 메시지를 DB로부터 시간순으로 찾아 브라우저로 전달한다. 브라우저에서는 prompt와 response를 구분하여 UserChatBox와 AIChatBox를 생성하고, keepScrollDown 함수를 통해 채팅 화면을 아래로 스크롤하여 가장 최신 메시지가 출력되도록 한다.

  ```js
  function askQuestion() {
    switchLoad();
    const questionInput = document.getElementById("question");
    const question = questionInput.value;
    questionInput.value = "";
    if (question) {
      makeUserChatBox(question);
      fetch("http://127.0.0.1:8000/?room=" + room, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: question, token: loginToken }),
      })
        .then((response) => response.json())
        .then((data) => {
          switchLoad();
          makeAIChatBox(data[0]["response"]);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  }
  ```

  채팅을 입력하고 제출하면 해당 element의 value를 post로 서버에 전달한다. 이때 제출 후 답변이 출력되기 전까지 switchLoad() 함수를 통해 loading modal을 화면에 출력한다.

## 6. 향후 개선 사항

### 6.1 코드 에러

- 채팅 화면 CSS

  채팅 화면은 HTML, CSS, JavaScript를 이용한 지난 프로젝트의 화면을 사용하였다. 이때 bootstrap을 적용하지 않고 순수 CSS로

### 6.2 코드 개선

- DB 중복 요청

### 6.3 추가 기능 구현

-

- 채팅방 추가 및 삭제

- auth2 적용 (카카오, github)

## 7. 개발 과정에서 느낀점
