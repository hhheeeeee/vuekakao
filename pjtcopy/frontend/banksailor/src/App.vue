<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import { useRoute } from "vue-router";
import { navbarLinks } from "./constants/navbarLinks";
const nowpath = useRoute().path;
const store = useCounterStore();

const customlogout = function () {
  window.alert("정말 떠나실건가요..?");
  store.logOut();
};
</script>

<template>
  <header>
    <nav>
      <a class="navbar-brand" href="#">
        <img
          src="@/assets/banksailor_logo.png"
          alt="Logo"
          width="30"
          height="30"
        />
      </a>
      <template v-for="(item, idx) in navbarLinks" key="item">
        <div
          class="navbar-items"
          :class="{ active: $route.fullPath.includes(item.links) }"
        >
          <RouterLink :to="item.links">{{ item.label }}</RouterLink>
        </div>
      </template>
      <div class="auth">
        <template v-if="store.isLogin">
          <form @submit.prevent="customlogout">
            <input type="submit" value="Logout" class="logout" />
          </form>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'LogInView' }" class="login"
            >로그인</RouterLink
          >
          <RouterLink :to="{ name: 'SignUpView' }" class="signup"
            >회원가입</RouterLink
          >
        </template>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
nav {
  border-bottom: 1px solid rgb(28, 54, 89);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 9dvh;
}

a {
  text-decoration: none;
  color: #1c5f82;
}

.navbar-items {
  padding: 0 30px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.login {
  border: 1px solid #1c5f82;
  color: #1c5f82;
  padding: 5px 10px;
  border-radius: 30px;
  font-weight: 600;
}

.signup,
.logout {
  border: 1px solid #1c5f82;
  background-color: rgb(28, 54, 89);
  color: white;
  padding: 5px 12px;
  border-radius: 30px;
}
.active {
  /* border: 1px solid #1c5f82; */
  background-color: rgb(214, 232, 255);
  font-weight: 800;
}

.auth {
  column-gap: 10px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>
