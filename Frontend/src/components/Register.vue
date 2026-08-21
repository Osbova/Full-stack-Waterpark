<template>
  <div class="page-container">
    <header class="top-bar">
      <h1 class="logo">
        <span class="let1">А</span>
        <span class="let2">к</span>
        <span class="let3">в</span>
        <span class="let4">а</span>
        <span class="let5">в</span>
        <span class="let6">э</span>
        <span class="let7">й</span>
      </h1>
    </header>

    <main class="main-content">
      <div class="register-wrapper">
        <div class="register-card">
          <h2>Регистрация</h2>          
          <form class="register-form" @submit.prevent="handleRegister">
            <div class="input-group">
              <label>Имя</label>
              <input 
                type="text" 
                v-model="name" 
                placeholder="Введите ваше имя" 
                minlength="4" 
                required 
              />
            </div>

            <div class="input-group">
              <label>Ваш пол</label>
              <div class="gender-options">
                <button 
                  type="button" 
                  id="genM" 
                  :class="{ activeM: gender === 'M' }" 
                  @click="gender = 'M'"
                >
                  М
                </button>
                <button 
                  type="button" 
                  id="genW" 
                  :class="{ activeW: gender === 'Ж' }" 
                  @click="gender = 'Ж'"
                >
                  Ж
                </button>
              </div>
            </div>

            <div class="input-group">
              <label>Пароль</label>
              <input 
                type="password" 
                v-model="password" 
                placeholder="••••••••" 
                minlength="6" 
                required 
              />
            </div>

            <button type="submit" class="submit-btn">Зарегистрироваться</button>
          </form>

          <div id="login">
            <span>Уже есть аккаунт?</span>
            <router-link to="/login" class="login-link">Войти</router-link>
          </div>
        </div>
      </div>
    </main>
    
    <footer class="bottom-bar">
      <p id="aj">© 2026 Аквавэй</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const name = ref('')
const gender = ref('')
const password = ref('')

const handleRegister = async () => {
  if (!gender.value) {
    alert('Пожалуйста, выберите ваш пол')
    return
  }

  if (name.value.length < 4 || password.value.length < 6) {
    return
  }

  const userData = {
    name: name.value,
    gender: gender.value,
    password: password.value
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })

    if (response.ok) {
      localStorage.setItem('userName', name.value)
      router.push('/menu')
    }
  } catch (error) {
    console.error('Ошибка при отправке данных:', error)
  }
}
</script>

<style scoped>
.gender-options {
  display: flex;
  gap: 10px;
}

#genM, #genW {
  width: 100px;
  padding: 10px 0;
  border: 1.5px solid #cbd5e1;
  background-color: #ffffff; 
  color: #334155;            
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.activeM {
  background-color: #025886 !important;
  border-color: #0077b6 !important;
  color: #ffffff !important; 
}

.activeW {
  background-color: rgb(154, 7, 154) !important;
  border-color: rgb(139, 5, 139) !important;
  color: #ffffff !important; 
}

.page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.top-bar {
  display: flex;
  justify-content: center; 
  align-items: center;     
  padding: 20px 0;
  background-color: #f8f9fa; 
  border-bottom: 2px solid #e0e0e0; 
}

.logo {
  font-size: 5rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: 4px; 
}

.let1 { color: #00b4d8; } 
.let2 { color: #0077b6; } 
.let3 { color: #48cae4; } 
.let4 { color: #52b788; } 
.let5 { color: #ffb703; } 
.let6 { color: #fb8500; }
.let7 { color: #e63946; }

.main-content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f4f8; 
  padding: 40px 20px;
}

.register-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px;
  border-radius: 20px;
  background-color: #e6edf3;
  box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.1),
              inset -4px -4px 10px rgba(255, 255, 255, 0.8);
}

.register-card {
  width: 100%;
  max-width: 400px; 
  background: #ffffff;
  padding: 35px 30px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
}

.register-card h2 {
  margin-bottom: 25px;
  text-align: center;
  color: #1e293b;
  font-size: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}

.input-group label {
  font-size: 0.9rem;
  margin-bottom: 6px;
  color: #64748b;
}

.input-group input {
  padding: 12px 14px;
  border: 1.5px solid #cbd5e1;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.input-group input:focus {
  border-color: #00b4d8;
  box-shadow: 0 0 0 3px rgba(0, 180, 216, 0.15);
}

.submit-btn {
  width: 100%;
  padding: 12px;
  margin-top: 10px;
  background-color: #00b4d8;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover {
  background-color: #0077b6;
}

#login {
  margin-top: 20px;
  text-align: center;
  font-size: 0.9rem;
  color: #64748b;
}

.login-link {
  margin-left: 6px;
  color: #00b4d8;
  text-decoration: none;
  font-weight: 600;
}

.login-link:hover {
  text-decoration: underline;
}

.bottom-bar {
  padding: 15px 0;
  text-align: center;
  background-color: #f8f9fa;
  border-top: 2px solid #e0e0e0;
}
</style>