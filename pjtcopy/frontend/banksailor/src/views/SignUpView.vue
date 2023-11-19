<template>
  <div class="container1">
    <h1>Signup</h1>
    <form @submit.prevent="signUp" class="form">
      <label for="username"> 아이디 </label>
      <p class="wrongusername" v-show="!isValidUsername">
        다른 아이디를 입력해주세요
      </p>
      <input
        type="text"
        v-model.trim="username"
        class="input"
        id="username"
        @blur="isDuplicated"
      />
      <label for="password">비밀번호 </label>
      <input
        type="password"
        v-model.trim="password1"
        class="input"
        id="password"
      />
      <label for="password2">비밀번호 확인</label>
      <input
        type="password"
        v-model.trim="password2"
        class="input"
        id="password2"
      />
      <input type="submit" value="가입하기" class="submit" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import axios from "axios";

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const isValidUsername = ref(true);

const isDuplicated = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/find/duplicateID/${username.value}`,
  })
    .then((res) => {
      if (res.data.message === "fail") {
        isValidUsername.value = false;
        alert("이미 등록된 ID입니다!");
      } else {
        isValidUsername.value = true;
      }
    })
    .catch((err) => {
      console.log(err);
    });
};

const signUp = function () {
  if (isValidUsername.value === false) {
    alert("이미 등록된 ID입니다! == 이건 signup 함수에서 걸린거");
    console.log("이미 등록된 ID입니다! == 이건 signup 함수에서 걸린거");
    return;
  } else {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    };

    store.signUp(payload);
  }
};
</script>

<style scoped>
.container1 {
  width: 100%;
  height: 100vh;
  background-color: #c3bfbf;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #1c5f82;
}

h1 {
  font-size: 2em;
  color: #1c5f82;
  margin-bottom: 20px;
  font-weight: 800;
}

.form {
  display: flex;
  flex-direction: column;
  width: 40%;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background-color: #f5f5f5;
}

label {
  margin-bottom: 5px;
}

.input {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #1c5f82;
  border-radius: 5px;
}

.submit {
  padding: 10px;
  background-color: #1c5f82;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit:hover {
  background-color: #4db7e5;
}

.wrongusername {
  color: red;
}
</style>
