<template>
  <div>

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


    <main class="tickets-container">
      <h2 class="section-title">Купить билеты</h2>

      <div class="booking-card">
        <div class="controls-row">
          <div class="date-wrapper">
            <input 
              type="date" 
              v-model="selectedDate" 
              min="2026-01-01" 
              max="2026-12-31" 
              class="custom-input date-input" 
            />
            <span class="day-badge">будни</span>
          </div>
        </div>

        <div class="tickets-grid">
          <div v-for="category in categories" :key="category.id" class="ticket-card">
            
            <h3 class="category-name">{{ category.name }}</h3>
            <span class="category-sub">{{ category.sub }}</span>

            <div v-if="category.id === 'student'" class="student-warning">
              ⚠️ При входе необходимо показать студенческий билет!
            </div>

            <div class="counter-box">
              <button class="counter-btn" @click="changeCount(category.id, -1)">-</button>
              <span class="count-value">{{ category.count }}</span>
              <button class="counter-btn" @click="changeCount(category.id, 1)">+</button>
            </div>

            <div class="price-tag">{{ category.price }} ₽</div>
          </div>
        </div>

        <div class="promo-row">
          <input 
            type="text" 
            v-model="promoCode" 
            placeholder="Промокод" 
            class="custom-input promo-input" 
          />
          <button class="action-btn" @click="applyPromo">Применить</button>
        </div>

        <div class="summary-footer">
          <div class="rules-info">
            <p>с 09:00 до 22:00</p>
          </div>

          <div class="total-box">
            <div class="total-price">{{ totalPrice }} ₽</div>
            <button class="action-btn pay-btn" :disabled="totalPrice === 0">Оплатить</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'


const selectedDate = ref('2026-08-27')
const promoCode = ref('')
const discount = ref(0)

const categories = ref([
  {
    id: 'adult',
    name: 'Взрослые',
    sub: 'от 150 см',
    price: 3590,
    count: 0
  },
  {
    id: 'child',
    name: 'Дети',
    sub: '110–150 см',
    price: 2000,
    count: 0
  },
  {
    id: 'student',
    name: 'Студенты',
    sub: 'Очная форма',
    price: 1990,
    count: 0
  }
])

const changeCount = (id, delta) => {
  const item = categories.value.find(c => c.id === id)
  if (item) {
    item.count = Math.max(0, item.count + delta)
  }
}

const applyPromo = () => {
  if (promoCode.value.toUpperCase() === 'SUMMER') {
    discount.value = 0.1
  }
}

const totalPrice = computed(() => {
  const baseTotal = categories.value.reduce((sum, item) => sum + item.price * item.count, 0)
  return Math.round(baseTotal * (1 - discount.value))
})
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
.tickets-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
}

.section-title {
  text-align: center;
  font-size: 2.2rem;
  color: #0f172a;
  margin-bottom: 30px;
  font-weight: 800;
}

.booking-card {
  background: #ffffff;
  border-radius: 24px;
  padding: 32px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  border: 1px solid #f1f5f9;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.controls-row {
  display: flex;
  gap: 16px;
}

.date-wrapper {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
}

.custom-input {
  width: 100%;
  padding: 14px 18px;
  border-radius: 14px;
  border: 1px solid #e2e8f0;
  background-color: #f8fafc;
  font-size: 1rem;
  font-weight: 600;
  color: #0f172a;
  outline: none;
  box-sizing: border-box;
}

.day-badge {
  position: absolute;
  right: 12px;
  background: #ffffff;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #0077b6;
  border: 1px solid #e2e8f0;
}

.tickets-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.ticket-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  justify-content: space-between;
}

.card-image-box {
  width: 100%;
  height: 140px;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 12px;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.category-name {
  margin: 0;
  font-size: 1.2rem;
  color: #0f172a;
}

.category-sub {
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 8px;
}

.student-warning {
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  color: #dc2626;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 6px 10px;
  border-radius: 10px;
  margin-bottom: 12px;
  line-height: 1.2;
}

.counter-box {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #ffffff;
  padding: 6px 16px;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  margin-bottom: 12px;
}

.counter-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  font-weight: 700;
  color: #0077b6;
  cursor: pointer;
  width: 24px;
  height: 24px;
}

.count-value {
  font-weight: 700;
  font-size: 1.1rem;
  color: #0f172a;
}

.price-tag {
  font-size: 1.3rem;
  font-weight: 800;
  color: #0077b6;
}

.promo-row {
  display: flex;
  gap: 12px;
}

.promo-input {
  flex: 1;
}

.action-btn {
  background-color: #0077b6;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.action-btn:hover {
  background-color: #00b4d8;
}

.action-btn:disabled {
  background-color: #cbd5e1;
  cursor: not-allowed;
}

.summary-footer {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-top: 1px solid #e2e8f0;
  padding-top: 20px;
}

.rules-info {
  font-size: 0.85rem;
  color: #64748b;
  line-height: 1.4;
}

.rules-info p {
  margin: 2px 0;
}

.rules-link {
  color: #0077b6;
  text-decoration: underline;
}

.total-box {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.total-price {
  font-size: 2.2rem;
  font-weight: 900;
  color: #0f172a;
}

@media (max-width: 768px) {
  .tickets-grid {
    grid-template-columns: 1fr;
  }

  .controls-row {
    flex-direction: column;
  }

  .summary-footer {
    flex-direction: column;
    align-items: stretch;
    gap: 20px;
  }

  .total-box {
    align-items: stretch;
  }
}
</style>