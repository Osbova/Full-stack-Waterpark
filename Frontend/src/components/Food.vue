<template>
  <div class="menu-page">
    <header id="bot">
      <div class="nav-group left-nav">
        <router-link to="/food" class="navigation">Позиции</router-link>
        <router-link to="/ticket" class="navigation">Билеты</router-link>
      </div>

      <h1 class="logo">
        <span class="let1">А</span>
        <span class="let2">к</span>
        <span class="let3">в</span>
        <span class="let4">а</span>
        <span class="let5">в</span>
        <span class="let6">э</span>
        <span class="let7">й</span>
      </h1>

      <div class="nav-group right-nav">
        <router-link to="/slide" class="navigation">Горки</router-link>
        <a href="https://t.me/ARESTOVAN_ZA_IZBIYENIE" target="_blank" class="navigation support-btn">Поддержка</a>
      </div>
    </header>

    <main class="menu-container">
      <div v-if="isLoading" class="status-msg">Загрузка меню...</div>
      <div v-else-if="hasError" class="status-msg error">
        Не удалось загрузить меню. Попробуйте позже.
      </div>
      <div v-else class="food-grid">
        <div v-for="item in foodList" :key="item.id" class="food-card">
          <div class="image-wrapper">
            <img 
              :src="getImageUrl(item.image_url)" 
              :alt="item.name" 
              referrerpolicy="no-referrer"
              @error="onImageError"
            />
          </div>
          <div class="card-content">
            <h3 class="food-name">{{ item.name }}</h3>
            <p class="food-taste">{{ item.taste || 'Классический вкус' }}</p>
            <div class="card-footer">
              <span class="food-price">{{ item.price }} ₽</span>
              <span class="waiter-notice">Для заказа обратитесь к официанту</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const foodList = ref([]);
const isLoading = ref(true);
const hasError = ref(false);

const defaultImage = "https://placehold.co/600x400/e2e8f0/1e293b?text=Нет+фото";
const API_URL = "http://127.0.0.1:8000";

function getImageUrl(url) {
  if (!url || typeof url !== 'string' || url.trim() === '') {
    return defaultImage;
  }
  
  if (url.startsWith('http://') || url.startsWith('https://')) {
    return url;
  }
  
  return `${API_URL}${url.startsWith('/') ? '' : '/'}${url}`;
}

async function fetchMenu() {
  try {
    const response = await fetch(`${API_URL}/food`, {
      headers: {
        'ngrok-skip-browser-warning': 'true'
      }
    });

    if (response.ok) {
      foodList.value = await response.json();
    } else {
      hasError.value = true;
    }
  } catch (error) {
    console.error("Ошибка при загрузке меню:", error);
    hasError.value = true;
  } finally {
    isLoading.value = false;
  }
}

function onImageError(e) {
  e.target.onerror = null;
  e.target.src = defaultImage;
}

onMounted(() => {
  fetchMenu();
});
</script>

<style scoped>

:global(body) {
  margin: 0;
  padding: 0;
  background-color: #f8fafc;
}

#bot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #e2e8f0;
  padding: 16px 50px;
  background-color: #ffffff;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.05);
  position: relative;
  top: 0;
  z-index: 100;
}

.nav-group {
  display: flex;
  align-items: center;
  gap: 28px;
  flex: 1;
}

.left-nav {
  justify-content: flex-start;
}

.right-nav {
  justify-content: flex-end;
}

.navigation {
  background: transparent;
  border: none;
  cursor: pointer;
  color: #1e293b;
  font-weight: 800;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
  padding: 10px 20px;
  border-radius: 12px;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none; 
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.navigation:hover {
  color: #0077b6;
  background-color: #f0f9ff;
  transform: translateY(-1px);
}

.navigation.router-link-active {
  color: #0077b6;
  background-color: #e0f2fe;
}

.support-btn {
  background-color: #f1f5f9;
  color: #0077b6;
  border: 1px solid #cbd5e1;
}

.support-btn:hover {
  background-color: #0077b6;
  color: #ffffff;
  border-color: #0077b6;
}

.logo {
  font-size: 3.4rem;
  font-weight: 900;
  margin: 0 30px;
  letter-spacing: 8px;
  text-align: center;
  white-space: nowrap;
  line-height: 1;
  user-select: none;
}

.let1 { color: #00b4d8; } 
.let2 { color: #0077b6; } 
.let3 { color: #48cae4; } 
.let4 { color: #52b788; } 
.let5 { color: #ffb703; } 
.let6 { color: #fb8500; }
.let7 { color: #e63946; }

.menu-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.food-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 24px;
}

.food-card {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  display: flex;
  flex-direction: column;
}

.image-wrapper {
  width: 100%;
  height: 180px;
  background-color: #f1f5f9;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 16px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.food-name {
  margin: 0 0 6px 0;
  font-size: 1.15rem;
  color: #0f172a;
}

.food-taste {
  margin: 0 0 16px 0;
  font-size: 0.88rem;
  color: #64748b;
  flex: 1;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: auto;
}

.food-price {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0f172a;
  white-space: nowrap;
}

.waiter-notice {
  font-size: 0.82rem;
  font-weight: 600;
  color: #64748b;
  background-color: #f1f5f9;
  padding: 6px 10px;
  border-radius: 8px;
  text-align: right;
  line-height: 1.2;
}

.status-msg {
  text-align: center;
  padding: 40px;
  font-size: 1.1rem;
  color: #64748b;
}

.status-msg.error {
  color: #ef4444;
}
</style>